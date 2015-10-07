# -*- coding: utf-8 -*-
"""
Class for holding greens functions for inversion problems

USF geodesy Fall 2015

Nick Voss
"""
import pandas as pd

class greenfnc(object):
    """AObject containing the greens functions relating model to obervations

    Attributes:
        name: string desribin the greens functions
        matrixDF : dataframe containt greens funtions columns should be 
                   the paramater names, index is the observation names 
    methods:
        transpose : return the transpose of the greenfunction matrix
        
    """
    def __init__(self, name,matrixDF):
        self.name = name
        self.matrixDF = matrixDF
    
    def transpose(self):
        return self.matrixDF.transpose()
        
        
