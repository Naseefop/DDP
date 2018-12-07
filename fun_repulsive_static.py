# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 18:29:41 2018

@author: Naseef
"""
import numpy as np
from numpy import linalg as LA
def repulsive_static(a,b,pos):    
    obs=[]
    for i in range(a[0],a[1]+1):
        for j in range(b[0],b[0]+1):
            obs.append([i,j])
            #find vector from obstacle to pos add them together to find the resultant 
            #return  the given vector
            # add it to the accelaration vector
    rep=0        
    for i in obs:
        dist=np.linalg.norm(np.array(pos)-np.array(obs[i]))
        if (dist<100):
            rep1=[pos[0]-i[0],pos[1]-i[1]]/LA.norm([pos[0]-i[0],pos[1]-i[1]])
            rep+=rep1
    return rep/LA.norm(rep)     
        
        
    
#    for i in range(a[0],a[1]):
#def repulsive_dynamic(pos1,pos2):
    