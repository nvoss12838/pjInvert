# -*- coding: utf-8 -*-
"""
classes for holding the regularization schemes for inversion problems

USF Geodesy Lab Fall 2015

Nick Voss
"""
import numpy as np 

class flat(object):
    """
    class for the D matrix for the flat matrix
    Attributes:
        name = flat 
        D = D numpy matrix for the flat solution
    Methods:
        to_Wd : creates the weight matrix from the D matrix
    """
    def __init__(self,D):
        self.name = 'flat'
        self.D = D
    
    def to_Wm(self):
        '''
        create the Wd matrix DTD
        '''
        return np.dot(self.D.T,self.D)

class epsilon(object):
    """
    class for the weight factor epsilon
    Attributes:
        e = weighting factor
    methods
        sqaure : return the square of the matrix
    """
    def __init__(self,e):
        self.e = e
    def square(self):
        return np.square(self.e)