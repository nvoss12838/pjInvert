# -*- coding: utf-8 -*-
"""
class for holding the data_vector for inversion problems

USF Geodesy Lab Fall 2015

Nick Voss
"""
import pandas as pg
import numpy as np 

class data(object):
    '''
    holds the data vector and contains methods for manipulation
    
    Attributes:
        dataS = pandas series with observations index should be th observation names
        weight = pandas series with weights for observations, index is observation names
    Methods:
        
    '''
    def __init__(self,dataS,weightS):
        self.dataS = dataS
        self.weights = weightS
    
    def weight2matrix(self):
        return np.diag(self.weights)
        
    

