# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 08:44:35 2018

@author: Naseef
"""
import numpy as np
from numpy import linalg as LA
import xlsxwriter
#import matplotlib.pyplot as plt
xvalues = np.array([x for x in range(600)])
yvalues = np.array([x for x in range(600)])
xx, yy = np.meshgrid(xvalues, yvalues)
goal = [500,400]
start=[150,200]
x1=start[0]
y1=start[1]
vx=0
vy=0
maxvel=5
deltat=0.1
A=[[1,0,deltat,0],[0,1,0,deltat],[0,0,1,0],[0,0,0,1]]
B=[[0.5*(deltat**2),0],[0,0.5*(deltat**2)],[deltat,0],[0,deltat]]
mA=np.matrix(A)
mB=np.matrix(B)
rf=[[x1,y1]]
while (LA.norm([x1-goal[0],y1-goal[1]])>100):
    attractive=[goal[0]-x1,goal[1]-y1]/LA.norm([goal[0]-x1,goal[1]-y1])
    ax=attractive[0]
    ay=attractive[1]
    x1=x1+vx*deltat+0.5*ax*(deltat**2)
    y1=y1+vy*deltat+0.5*ay*(deltat**2)
    vx=vx+deltat*ax
    vy=vy+deltat*ay

#    print(LA.norm([vx,vy]))
#    print([vx,vy])
    normm = LA.norm([vx,vy])
    if LA.norm([vx,vy])>20:
        vx=(vx/normm)*20
        vy=(vy/normm)*20

    R=[x1,y1]
    rf.append(R)
    

   
# CREATING EXCEL
# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('RFnew.xlsx')
worksheet = workbook.add_worksheet()

# Some data we want to write to the worksheet.

# Start from the first cell. Rows and columns are zero indexed.
row = 0
col = 0

# Iterate over the data and write it out row by row.
for x in (rf):
    worksheet.write(row, col,x[0])
    worksheet.write(row, col + 1,x[1])
    row += 1
# Write a total using a formula.
#worksheet.write(row, 0, 'Total')
#worksheet.write(row, 1, '=SUM(B1:B4)')

workbook.close()        
        