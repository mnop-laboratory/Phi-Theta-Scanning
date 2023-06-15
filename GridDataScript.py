#!/usr/bin/env python
# coding: utf-8

# In[1]:



from numpy import *
import numpy as np
from scipy.interpolate import griddata
import math 
import matplotlib.pyplot as plt



def grid(points, data, grid_points):
    global min_theta, max_theta, min_phi, max_phi

    #grid_x, grid_y = np.mgrid[0:math.pi:30j, 0:2* math.pi:30j]
    points = np.array(points)
    data = np.array(data)
    #print("Data")
    #print(data)
    points_shapes = points.shape
    data_shapes = data.shape
    #rint("shape")
    #rint(shapes)
    #rint("points")
    #print(points[1,1,0])
    #print("data")
    #print(data)
    cells = int(points_shapes[0]*points_shapes[1])
    cells_data = int(data_shapes[0]*data_shapes[1])
    #print("cells")
    #print(cells)
    points_anglesa = np.zeros(cells)
    points_anglesb = np.zeros(cells)
    data_angles = np.zeros(cells_data)
    points_angles = np.zeros((cells,2))
    #print("Points Size")
    #print(points.shape)
    #print("Data Size")
    #print(data.shape)
    #print("Angled data Size")
    #print(data_angles.shape)
    temp = 0
    for i in range(points_shapes[0]) :
        for j in range(points_shapes[1]) :
            
            pf = 7.5    #parent focal length
            ef = 15     #effective focal length
            cf = (ef)**2/(pf)
            
            #cf = 1
            
            b = points[i,j,1]
            a = points[i,j,0]
            
            x = a-15
            y = b
            ########
            #change so that phi is now phi'
            #temp = x
            #y=temp
            #x=y
            #change so that phi is now phi'
            ########
            z = -pf+(x**2+y**2)/(cf)
            ########
            #change so that phi is now phi'
            #z=-z
            #change so that phi is now phi'
            ########
            p = math.sqrt(x**2+y**2+z**2)
            
            
            
            
            
            #theta
            points_anglesa[j+(i*points_shapes[1])] = math.acos(y/p)
            
            #phi
            points_anglesb[j+(i*points_shapes[1])] = math.asin((z/p)*(1/(sin(points_anglesa[j+(i*points_shapes[1])]))))
            
            
            #points_anglesa[j+(i*shapes[1])] = math.atan((points[i,j,0]+15)**2/(30+points[i,j,0]))
            #points_anglesb[j+(i*shapes[1])] = math.atan((points[i,j,1])/(15-points[i,j,0]))
            #points_anglesa[j+(i*shapes[1])] = math.atan((points[i,j,0])**(1/2)/(15-points[i,j,0]))
            #points_anglesb[j+(i*shapes[1])] = math.atan((points[i,j,1])**(1/2)/(15-points[i,j,1]))
            #points_anglesa[j+(i*shapes[1])] = math.atan(math.sqrt(abs(points[i,j,0]))/(15-points[i,j,0]))+math.atan(points[i,j,1]/(points[i,j,1]**2/15 +1))
            #points_anglesb[j+(i*shapes[1])] = math.asin(points[i,j,1]**2/15)
            
            # pssobile correct for cubic or linear
           # points_anglesa[j+(i*shapes[1])] = math.atan(math.sqrt(abs(points[i,j,0]))/(15-points[i,j,0])) + math.atan(points[i,j,1]/15) 
            #points_anglesb[j+(i*shapes[1])] = math.atan(points[i,j,1]**2/15)
 
            #points_anglesa[j+(i*shapes[1])] = math.atan((points[i,j,0]+15)**2/(15+points[i,j,0])) +math.atan(points[i,j,1]**2/15)  
            #points_anglesb[j+(i*shapes[1])] = math.atan(points[i,j,1]/15) 
            
            #theta
            #points_anglesa[j+(i*points_shapes[1])] = math.acos((points[i,j,1])/(math.sqrt((points[i,j,0]-15)**2+points[i,j,1]**2+(-7.5+(points[i,j,0]-15)**2+points[i,j,1]**2)**2)))
            #(retyped them ADDING IN PARABOLIC CORRECTION FACTOR)
 #           points_anglesa[j+(i*points_shapes[1])] = math.acos((points[i,j,1])/(math.sqrt((points[i,j,0]-15)**2+points[i,j,1]**2+(-7.5+((points[i,j,0]-15)**2+points[i,j,1]**2))*(1/30)**2)))
            #small angle approximation
            #points_anglesa[j+(i*points_shapes[1])] = math.acos((points[i,j,1])/(math.sqrt((points[i,j,0]-15)**2+points[i,j,1]**2+(-7.5+(points[i,j,0]-15)**2+points[i,j,1]**2)**2)))
            
            
            
            
            #phi
            #points_anglesb[j+(i*points_shapes[1])] = math.acos(-(points[i,j,0]-15)/(sin(math.acos((points[i,j,1])/(math.sqrt((points[i,j,0]-15)**2+points[i,j,1]**2+(-7.5+(points[i,j,0]-15)**2+points[i,j,1]**2)**2))))*(math.sqrt((points[i,j,0]-15)**2+points[i,j,1]**2+(-7.5+(points[i,j,0]-15)**2+points[i,j,1]**2)**2)))) 
            #(retyped them ADDING IN PARABOLIC CORRECTION FACTOR)
  #          points_anglesb[j+(i*points_shapes[1])] = math.acos(-(points[i,j,0]-15)/(sin(points_anglesa[j+(i*points_shapes[1])])*math.sqrt((points[i,j,0]-15)**2+points[i,j,1]**2+(-7.5+((points[i,j,0]-15)**2+points[i,j,1]**2)*(1/30))**2)))
            #small angle approximation 
            #points_anglesb[j+(i*points_shapes[1])] = math.acos(-(points[i,j,0]-15)/(points_anglesa[j+(i*points_shapes[1])]*math.sqrt((points[i,j,0]-15)**2+points[i,j,1]**2+(-7.5+(points[i,j,0]-15)**2+points[i,j,1]**2)**2)))
            
            
    print("Phi")
    print(points_anglesb)
    for i in range(data_shapes[0]) :    
        for j in range(data_shapes[1]):
            data_angles[j+(i*data_shapes[1])] = data[i,j]
    for i in range(size(points_anglesa)) :
        points_angles[i,0] = points_anglesa[i]
        points_angles[i,1] = points_anglesb[i]
    
    
    min_theta = min(points_anglesa)
    max_theta = max(points_anglesa)
    #print(max_theta)
    
    min_phi = min(points_anglesb)
    max_phi = max(points_anglesb)
    
    grid_points = complex(0,grid_points)
    
    grid_x, grid_y = np.mgrid[min_theta:max_theta:grid_points, min_phi:max_phi:grid_points]
    
    #print("angled data")
    #print(points_angles)
    #print("data angles")
    #print(data_angles)
    grided = griddata(points_angles, data_angles, (grid_x, grid_y), method='linear',fill_value=NaN)
    # 'nearest', 'cubic', or 'linear'

    return grided


def test():
    size = 300
    points = np.zeros((size,size,2))
    data = np.zeros((size,size))
    for i in range(size):
        for j in range(size):
            points[i,j] = [(i-size/2)/10,(j-size/2)/10]
            if (((i-150))**2 + (j-150)**2 < 150**2) :
                 data[i,j] = 1 #np.random.randint(0,99)
            else:
                data[i,j] = 0
    print(points)
    print(data)        
    #gridz = grid(array([[[1,1],[2,1],[3,1]],[[1,2],[2,2],[3,2]],[[1,3],[2,3],[3,3]]]), array([[2,10,1],[2,9,3],[4,8,3]]))
    gridz = grid(points,data,3000)
    plt.imshow(gridz)
    #plt.imshow(data)
    return (gridz)

def ntest():
    pointsfilex = open(r"C:\Users\mnopl\OneDrive\Documents\Images (Hayden-Devon)\RawData\f5_6-13-2023 Big Scan LHS afm calibration_PointsX","r")
    pointsfiley = open(r"C:\Users\mnopl\OneDrive\Documents\Images (Hayden-Devon)\RawData\f5_6-13-2023 Big Scan LHS afm calibration_PointsY","r")
    datafile = open(r"C:\Users\mnopl\OneDrive\Documents\Images (Hayden-Devon)\RawData\f5_6-13-2023 Big Scan LHS afm calibration_Data","r")
    
    
    pointsx = np.loadtxt(pointsfilex)
    pointsy = np.loadtxt(pointsfiley)
    
    print(pointsx)
    shapesy = pointsy.shape
    points = np.zeros((shapesy[0],shapesy[1],2))
    
    points_positive = np.zeros((shapesy[0],shapesy[1],2))
    points_negative = np.zeros((shapesy[0],shapesy[1],2))
    
    data_pos = np.zeros((shapesy[0],shapesy[1]))
    data_neg = np.zeros((shapesy[0],shapesy[1]))
    
    data = np.loadtxt(datafile)
    
    for i in range(shapesy[0]):
        u = 0
        k = 0
        for j in range(shapesy[1]):
            points[i,j,0] = pointsx[i,j]
            points[i,j,1] = pointsy[i,j]
            if pointsx[i,j] < 0 :
                points_negative[i,j,0] = pointsx[i,j]
                points_negative[i,j,1] = pointsy[i,j]
                data_pos[i,u] = data[i,j]
                u = u+1
            else :
                points_positive[i,j,0] = pointsx[i,j]
                points_positive[i,j,1] = pointsy[i,j]
                data_neg[i,k] = data[i,j]
                k = k+1
                
    
    print("points")
    print(points.shape)
    print("Data")
    print(data.shape)
    gridz = grid(points,data,3000)
    print("gridded data")
    print(gridz)
    #plt.imshow(data)
    pointsfilex.close()
    pointsfiley.close()
    datafile.close()
    
    print("POINTS POSITIVE")
    print(points_negative)
    print("POINTS NEGATIVE")
    print(points_positive)
    print('POINTS')
    print(points)
    
    plt.imshow(gridz)
    #fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(nrows=2, ncols=2)
    
    #grid_pos = grid(points_positive, data_pos, 3000)
    #grid_neg = grid(points_negative, data_neg, 3000)
    #ax1.imshow(data)
    #ax1.set_title("Data")
    #ax2.imshow(gridz)
    #ax2.set_title("Full Data Set")
    #ax3.imshow(grid_neg)
    #ax3.set_title("Positive Data")
    #ax4.imshow(grid_pos)
    #ax1.axes.get_xaxis().set_visible(False)
    #ax2.axes.get_xaxis().set_visible(False)
    #ax4.set_title("Negative Data")
    #plt.show()
    return()
    
def OffsetAndMult(grid_points):
    offset_theta = min_theta
    offset_phi = min_phi
    
    theta_range = max_theta - min_theta
    phi_range = max_phi - min_phi
    
    theta_mult = theta_range/grid_points
    phi_mult = phi_range/grid_points
    
    info = [offset_theta, theta_mult, offset_phi, phi_mult]
    return(info)