# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 20:49:14 2015
solutions to the inverse problem
relies on other classes in pjInvert

USF Geodesy Fall 2015

Nick Voss
"""
from numpy.linalg import inv
import pandas as pd 

def weightedLeastSquares(greensfnc,Wm,We,epsilon,m_init,data):
    '''
    performs a weighted Least Squares inversion
    m^{est}=[G^TW_mG + \varepsilon^2W_m]^{-1}[G^{T}W_ed +\varepsilon^2W_m\langle m \rangle]$
    
    inputs:
        greensfnc = greens function object
        Wm = regularization matrix 
        epsilon = factor contoling regularization enforcement
        m_init = initial guess, a model oject
        data = data object
    returns:
        m_est = estmates model paramaters 
    '''
    #make first hald of equation
    G = greensfnc.as_matrix()
    GT = greensfnc.transpose().as_matrix()
    first = GT*Wm*G + epsilon.squared()*Wm
    firstInv = inv(first)
    #make second half
    second = GT*We*data.values + epsilon.squared()*Wm*m_init.values
    solution = firstInv*second
    #make m object from solution
    m_est = pd.Series(solution,index = m_init.index)
    return m_est
    
    
    