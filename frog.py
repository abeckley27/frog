#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 14:06:17 2019

@author: Aidan Beckley
"""

import time
import numpy as np
from matplotlib import pyplot as plt

def calculate_probability(pattern, npads):
    
    # create a list of 1s and 0s for jump or no jump at each pad
    ls = list(str(bin(pattern)))[2:]
    
    l = list(range(npads))
    for k in range(npads):
        l[k] = 0
    
    if (len(ls) < npads):
        for k in range( npads - len(ls), npads ):
            l[k] = int(ls[k + len(ls) - npads])
        
    else:
        #convert to numbers
        for k in range(npads):
            l[k] = int(ls[k])
        
    #The probability of the first jump (uniform)
    prob = 1.0
    remaining = l
    pad = 0
    npads_forward = npads
    i = 0
        
    if (l.count(1) == 0):
        prob = 1.0 / (npads + 1)
    
    while (remaining.count(1)):
        prob *= ( 1.0 / (npads_forward + 1) )
        if ( l[pad + 1:].count(1) == 0 ):
            break
            
        pad += 1
        
        #If we're not at the end, jump to the next visited pad
        while (l[pad] == 0):
            pad += 1
        
        npads_forward = npads - pad
        remaining = l[pad:]
        
        i += 1
        
    return prob * (l.count(1) + 1)


def do_the_thing(npads):
    x = 0

    for k in range(np.power(2, npads)):
        x += calculate_probability(k, npads)
    
    return x

def harmonic(n):
    x = 0
    for k in range(1, n + 2):
        x += 1.0 / k
    return x

def make_plot(start, end):
    t0 = time.time()
    x = np.array( range(start, end) )
    y = np.zeros(len(x))
    for k in range(len(x)):
        y[k] = harmonic(x[k])
    plt.plot(x,y)
    plt.xlabel("number of pads")
    plt.ylabel("average number of jumps")
    plt.show()
    return "%.3f s" %(time.time() - t0)

