
from numpy import *
import numpy as np
from scipy.interpolate import griddata
import math 
import matplotlib.pyplot as plt

def grid(points, data):
    grid_x, grid_y = np.mgrid[0:math.pi:300j, 0:2* math.pi:300j]
    shapes = points.shape
    #rint("shape")
    #rint(shapes)
    #rint("points")
    #print(points[1,1,0])
    #print("data")
    #print(data)
    cells = int(shapes[0]*shapes[1])
    #print("cells")
    #print(cells)
    points_anglesa = np.zeros(cells)
    points_anglesb = np.zeros(cells)
    data_angles = np.zeros(cells)
    points_angles = np.zeros((cells,2))
    #t = 0
    
    for i in range(shapes[0]) :
        #print(i)
        print(points[i,0,0])
        for j in range(shapes[1]) :
            
            #print(j)
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
            points_anglesa[j+(i*shapes[1])] = math.acos((points[i,j,1])/(math.sqrt((points[i,j,0]-15)**2+points[i,j,1]**2+(-7.5+(points[i,j,0]-15)**2+points[i,j,1]**2)**2)))
            #phi
            points_anglesb[j+(i*shapes[1])] = math.acos(-(points[i,j,0]-15)/(sin( points_anglesa[j+(i*shapes[1])])*(math.sqrt((points[i,j,0]-15)**2+points[i,j,1]**2+(-7.5+(points[i,j,0]-15)**2+points[i,j,1]**2)**2)))) 
            
            
            data_angles[j+(i*shapes[1])] = data[i,j]
    for i in range(size(points_anglesa)) :
        points_angles[i,0] = points_anglesa[i]
        points_angles[i,1] = points_anglesb[i]
    
    #print("angled data")
    #print(points_angles)
    #print("data angles")
    #print(data_angles)
    grided = griddata(points_angles, data_angles, (grid_x, grid_y), method='linear')
    
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
    gridz = grid(points,data)
    plt.imshow(gridz)
    #plt.imshow(data)
    return (gridz)
    

