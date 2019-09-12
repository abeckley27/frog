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
    s = str(bin(pattern))
    l = list(s)[2:]
    
    #convert to numbers
    for k in range(len(l)):
        l[k] = int(l[k])
        
    #The probability of the first jump (uniform)
    output = 1.0 / (npads + 1)
        
    #If there is more than one jump...
    if (l.count(1) != 0):
        pad = 0
        
        #find the first jumping point
        while (l[pad] == 0):
            pad += 1
        
        while (pad < len(l)):
            npads_forward = npads + 1 - pad
            
            #If we're not at the end, jump to the next visited pad
            # (if one exists)
            if ( pad < len(l) - 1):
                pad += 1
                while (l[pad] == 0 and pad < len(l)-1):
                    pad += 1
            #If if does exist, multiply by the probability of landing there
            if (l[pad]):
                output *= ( 1.0 / npads_forward )
            
            #If it doesn't that means we're at the other end
            else:
                break
            
            #If the last pad is landed on, break in that case too
            if ( pad == len(l) - 1 ):
                break
        
    return output * (s.count('1') + 1)


def do_the_thing(npads):
    x = 0

    for k in range(np.power(2, npads)):
        x += calculate_probability(k, npads)
    
    return x


def make_plot(start, end):
    t0 = time.time()
    x = np.array( range(start, end) )
    y = np.zeros(len(x))
    for k in range(len(x)):
        y[k] = do_the_thing(x[k])
    plt.plot(x,y)
    plt.xlabel("number of pads")
    plt.ylabel("average number of jumps")
    plt.show()
    return "%.3f s" %(time.time() - t0)

