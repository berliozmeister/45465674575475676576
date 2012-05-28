'''
Created on 24.05.2012

@author: berlioz

some auxilary functions and classes to be defined here
'''

import networkx.utils as nu
import numpy as np

#def is_valid_degree_sequence(sequence):
    

def powelawArray(n, beta, mean_degree):
    powerLawSequence = nu.powerlaw_sequence(n, beta)
    powerLawArr = np.array(powerLawSequence)
    initialSum = np.sum(powerLawArr)
    expectedSum = mean_degree * n
    if initialSum == expectedSum:
        return powerLawArr
    else:
        for i in range(n):
            powerLawArr[i] *= (expectedSum / initialSum)
        return powerLawArr

def parsum(s):
    count = 0
    yield 0
    for i in s:
        count += i
        yield count

def partSum(arr):
    count = 0
    yield 0
    for i in range(arr.size - 1):
        count += arr[i]
        yield count

def partialSum(arr):
    tmpArray = np.cumsum(arr)
    yield tmpArray
        


