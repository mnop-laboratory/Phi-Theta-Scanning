# -*- coding: utf-8 -*-
"""
Created on Wed May 24 09:51:16 2023

@author: mnopl
"""

import numpy as np

def savedata(points, data):
   
    points = np.array(points)
    data = np.array(data)
    points_shapes = points.shape
    data_shapes = data.shape
    ###SAVING TO TEXT FILES###
    pointsx = np.zeros((points_shapes[0],points_shapes[1]))
    pointsy = np.zeros((points_shapes[0],points_shapes[1]))

    for i in range(points_shapes[0]) :
        for j in range(points_shapes[1]):
            pointsx[i,j] = points[i,j,0]
            pointsy[i,j] = points[i,j,1]
    pointsfilex = open(r"C:\Users\mnopl\OneDrive\Desktop\PointsX.txt","w")
    pointsfiley = open(r"C:\Users\mnopl\OneDrive\Desktop\PointsY.txt","w")
    np.savetxt(pointsfilex,pointsx)
    np.savetxt(pointsfiley,pointsy)
    datafile = open(r"C:\Users\mnopl\OneDrive\Desktop\DataV2.txt","w", encoding='utf8')
    np.savetxt(datafile,data,encoding='utf8')
    pointsfilex.close()
    pointsfiley.close()
    datafile.close()
    return(data) 
    