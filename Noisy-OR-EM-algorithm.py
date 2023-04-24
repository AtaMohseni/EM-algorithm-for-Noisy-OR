# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 12:44:05 2023

@author: ATA
"""

from DataLoader import data_loader
import numpy as np

def NoisyOr_CPT(Xobservation,pi):
    """ this function calculate and return P(Y=1 | X=x) using Noisy OR 
    algorithm as well as P(Y=0 | X=x) where Y∈{0,1} , X∈{0,1} of length n .
    
    Xobservation is list of binary ∈ {0,1} with length n
    pi is list with length n"""
    
    product = 1
    for index, pr in enumerate(pi):
        product *= (1 - pr)**Xobservation[index]
    probY1 = 1 - product 
    probY0 = 1 -probY1
    return probY1 , probY0
def log_likelihood(data,pi):
    """ function to calculate log-likelihood using entire dataset and given 
    noisy-or probablity vector Pi"""
    L = 0
    
    for index, item in enumerate(data):
        probY1 , probY0 = NoisyOr_CPT(item[0], pi) 
        L += (1 - item[1])*np.log(probY0) + item[1]*np.log(probY1)   
    
    return L/len(data)


if __name__ == "__main__" :
    
    XY = data_loader()
    