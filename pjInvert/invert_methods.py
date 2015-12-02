# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 20:49:14 2015
solutions to the inverse problem
relies on other classes in pjInvert

USF Geodesy Fall 2015

Nick Voss
"""
from numpy.linalg import inv
import numpy as np 
import pandas as pd 

def weightedDampedLeastSquares(greensfnc,Wm,We,epsilon,m_init,data):
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
    G = greensfnc.matrixDF.as_matrix()
    GT = greensfnc.matrixDF.transpose().as_matrix()
    first = np.dot(np.dot(GT,We),G) + np.dot(epsilon.square(),Wm)
    firstInv = inv(first)
    #make second half
    second = np.dot(np.dot(GT,We),data.dataS.values) + np.dot(np.dot(epsilon.square(),Wm),m_init.modelS.values)
    solution = np.dot(firstInv,second)
    #make m object from solution
    m_est = pd.Series(solution,index = m_init.modelS.index)
    return m_est

def LeastSquares(greensfnc,data):
    '''
    preforms simple Least Squares inversiton 
    m^<est> = [G^TG]^-1G^Td
    inputs:
        greensfnc= greensfngc objet
        d = data object
    returns:
        m_est = estimate of model paramaters
    '''
    G = greensfnc.matrixDF.as_matrix()
    GT = greensfnc.matrixDF.transpose().as_matrix()
    solution = np.dot(np.dot(inv(np.dot(GT,G)),GT),data.dataS.values)   
    m_est = pd.Series(solution)
    return m_est
    
def weightedLeastSquares(greensfnc,data):
    '''
    performs a weighted Least Squares inversion
    m^{est}=[G^TW_eG ]^{-1}[G^{T}W_ed$
    
    inputs:
        greensfnc = greens function object
        data = data object with weight attribute
    returns:
        m_est = estmates model paramaters 
    '''
    #make first hald of equation
    G = greensfnc.matrixDF.as_matrix()
    GT = greensfnc.matrixDF.transpose().as_matrix()
    first = np.dot(np.dot(GT,data.weight2matrix()),G)
    firstInv = inv(first)
    #make second half
    second = np.dot(np.dot(GT,data.weight2matrix()),data.dataS.values)
    solution = np.dot(firstInv,second)
    #make m object from solution
    m_est = pd.Series(solution)
    return m_est

def covariance(greensfnc,data):
    '''
    get the covariance of the inversion problem given the greensfnc, and data covariance
    [cov m]=sigma^2[GTG]^-1
    and sigma^2= 1/n-m sum(error^2)
    inputs : 
        greensfnc = greens function object
        data = data object with data weights
    '''
    e = data.weights.values
    G = greensfnc.matrixDF.as_matrix()
    GT = greensfnc.matrixDF.transpose().as_matrix()
    n = len(e)
    m = np.shape(G)[1]
   # sigma2  = 1.0/(n-m)*np.sum([error**2 for error in e])
    sigma2 = 0.5
    covariance = np.multiply(sigma2,inv(np.dot(GT,G)))
    return covariance
    
    