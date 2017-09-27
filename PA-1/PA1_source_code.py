import numpy as np
import pandas as pd
import math as m
import matplotlib.pyplot as plt
import cvxopt
from scipy.stats import multivariate_normal

# cd D:\\OneDrive\\文档\\cityu\\MachineLearning\\MLAssignment\\PA-1\\PA-1-data-text

# define the polynomial function
def poly_function(x,order = 1):
    return np.array([m.pow(x,i) for i in range(0,order+1) ])

# load file from txt
def load_file(filename = 'polydata_data_polyx.txt'):
    return np.genfromtxt(filename,dtype='double')

# transpose 
def T(x):
    if(len(x.shape)>1):
        return np.transpose(x)
    else:
        return x.reshape(1,x.shape[0])

# x is a set of column vectors, get the transpose form of Φ matrix
def PHIx(x,order=1,function='poly'):
    if(function == 'poly'):
        mat = [poly_function(item,order) for item in x ]
        #return np.transpose(np.array(mat))
        return T(np.array(mat))

# return objective function according to different methods.
def obj_function(y,PHI,theta,Lambda=0,method='LS'):
    if method == 'LS':
        return np.linalg.norm(y-np.dot(T(PHI),theta),ord=2)
    if method == 'RLS':
        return np.linalg.norm(y-np.dot(T(PHI),theta),ord=2) + Lambda * np.linalg.norm(theta,ord=2)
    if method == 'LASSO':
        return np.linalg.norm(y-np.dot(T(PHI),theta),ord=2) + Lambda * np.linalg.norm(theta,ord=1)
    if method == 'RR':
        return np.linalg.norm(y-np.dot(T(PHI),theta),ord=1)

# Generate prediction according to the theta
def predict(x,theta,function='poly'):
    if(function=='poly'):
        PHIX=PHIx(x,order=theta.shape[0]-1,function=function)
        predections = np.dot(T(PHIX),theta)
        return predections

# parameter estimate , all input vectors are column vectors
def para_estimate(y,PHI,Lambda=0,method='LS'):
    if method == 'LS':
        return np.dot(np.dot(np.linalg.inv(np.dot(PHI,T(PHI))),PHI),y)
    if method == 'RLS':
        return np.dot(np.dot(np.linalg.inv(np.dot(PHI,T(PHI))+Lambda*np.eye(PHI.shape[0])),PHI),y)

# define posterior of Bayesian Regression
def posterior_BR(x,y,PHI,alpha=0,sigma=0):
    SIGMA_theta = np.linalg.inv(1/(sigma*sigma)*np.dot(PHI,T(PHI)+1/alpha*np.eye(PHI.shape[0])))
    MIU_theta = 1/(sigma*sigma)*np.dot(np.dot(SIGMA_theta,PHI,y)) 
    posterior = multivariate_normal(x,MIU_theta,SIGMA_theta)
    return posterior,MIU_theta,SIGMA_theta

def predict_BR(x,MIU_theta,SIGMA_theta):

    return

# Generate Plots with
def plot_f_s(x,y,sampx,sampy,label):
    plt.plot(x, y, label=label)
    plt.legend()
    plt.plot(sampx, sampy,'ro',label='data')
    plt.legend()
    plt.show()
    return 

# Experimen of LS
def expriment_LS():
    polyx = load_file(filename = 'polydata_data_polyx.txt')
    polyy = load_file(filename = 'polydata_data_polyy.txt')
    sampx = load_file(filename = 'polydata_data_sampx.txt')
    sampy = load_file(filename = 'polydata_data_sampy.txt')

    return

def main():
    polyx = load_file(filename = 'polydata_data_polyx.txt')
    polyy = load_file(filename = 'polydata_data_polyy.txt')
    sampx = load_file(filename = 'polydata_data_sampx.txt')
    sampy = load_file(filename = 'polydata_data_sampy.txt')

    theta_LS = para_estimate(sampy,PHIx(sampx,order=5,function='poly'),method='LS')
    prediction_LS = predict(polyx,theta_LS,function='poly')
    plot_f_s(polyx,prediction_LS,sampx,sampy,label='Least-squares Regression')

    theta_RLS = para_estimate(sampy,PHIx(sampx,order=5,function='poly'),Lambda=1,method='RLS')
    prediction_RLS = predict(polyx,theta_RLS,function='poly')
    plot_f_s(polyx,prediction_RLS,sampx,sampy,label='Regularize LS Regression')

    # my code here

if __name__ == "__main__":
    main()



