# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 12:44:05 2023

@author: ATA
"""

from DataLoader import data_loader
import numpy as np

def NoisyOr_CPT(Xobservation,P):
    """ this function calculate and return P(Y=1 | X=x) using Noisy OR 
    algorithm as well as P(Y=0 | X=x) where Y∈{0,1} , X∈{0,1} of length n .
    
    P is list with length n"""
    
    product = 1.0
    for index, pr in enumerate(P):
        product *= (1 - pr)**Xobservation[index]
    probY1 = 1 - product 
    probY0 = 1 - probY1
    
    return probY1 , probY0

def log_likelihood(data,P):
    """ function to calculate log-likelihood using entire dataset and given 
    noisy-or probablity list P"""
    L = 0
    
    for index, item in enumerate(data):
        probY1 , probY0 = NoisyOr_CPT(item[0], P) 
        L += (1 - item[1])*np.log(probY0) + item[1]*np.log(probY1)   
    
    return L/len(data)

def E_step(Xobservation, y, P, index):
    
    if y==0 or Xobservation[index]==0 or P[index] == 0:
        return 0
    else:
        probY1, probY0 = NoisyOr_CPT(Xobservation, P)
        return y * Xobservation[index] * P[index] / probY1
    
def M_step(XY,P):
    P_update = []
    for index, prob in enumerate(P):
        M_step_numunator = 0
        for data in XY:
            M_step_numunator += E_step(data[0], data[1], P, index)
        P_update.append(M_step_numunator /sum(row[0][index] for row in XY))     
    return P_update
   
def error(XY, P):
    count = 0
    for observation in XY:
        probY1, _ = NoisyOr_CPT(observation[0], P)
        
        # false negative:
        if probY1 <= 0.5 and observation[1] == 1:
            count += 1
        #false positive    
        if probY1 > 0.5 and observation[1] == 0:
            count += 1
    return count

if __name__ == "__main__" :
    """each observation: Y∈{0,1} , X∈{0,1} of length n, Z∈{0,1} of length n"""
    
    XY = data_loader() # list of all data, format for each datapoint [x1,x2,..xn],y 
    Probability_vec = [1/len(XY[0][0]) for item in XY[0][0]]  # list length n
    printing_iter = [0] + [2**n for n in range(9)]
    
    for iteration in range(257):
        if iteration in printing_iter:
            L = log_likelihood(XY, Probability_vec)
            E = error(XY,Probability_vec)
            print(iteration,E, L)
            
        Probability_vec = M_step(XY, Probability_vec)
        
            