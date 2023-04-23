# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 14:08:51 2023

@author: ATA
"""

def data_loader():
    """ function that read X and Y data for each example and store
    them together on a list and return the list"""
    
    try:
        X = open('./spectX.txt')
        Y = open('./spectY.txt')
    except:
        print ('one or more the files do not exist')
        return None
    
    datasetX = []
    datasetY = []
    datasetXY = []
    for line in X : 
        datasetX.append(list(map(int,list (line.split()) )))
    for line in Y:
        datasetY.append(int(line))
    for index, item in enumerate(datasetX):
        datasetXY.append([item,datasetY[index]])
        
    return datasetXY
        

if __name__ == "__main__" :
    
    XY = data_loader()