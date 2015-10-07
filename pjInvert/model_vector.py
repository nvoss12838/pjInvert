# -*- coding: utf-8 -*-
"""
class for holding the model_paramaters for inversion problems

USF Geodesy Lab Fall 2015

Nick Voss
"""

class paramaters(object):
    '''
    holds the model paramaters and contains methods for manipulation
    
    Attributes:
        modelS = pandas series with model paramaters, index should be th paramater names
    Methods:
    '''    
    def __init__(self,modelS):
        self.modelS = modelS

