from operator import itemgetter
from tkinter import *
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt

active_edge = []
pointsMax =[]
choice = 0
 
def zero():
    global active_edge, pointsMax
    active_edge = []
    pointsMax =[]
    c.create_rectangle(0,0,1920,1080, fill='white') 
    
def get_point():
    with open('points.txt', "r") as file:
        points = []
        for line in file:
            point = line.split()
            result = [int(item) for item in point]
            points.append(result)
        return points
       
     

def Delone(event):
    global pointsMax
    point = []
    point.append(event.x) 
    point.append(event.y)
    c.create_oval(point[0]-5,point[1]-5,point[0]+5,point[1]+5, fill='black')
    pointsMax.append(point)
    triangulate(point)
    
    
def triangulate(point_new):
    global active_edge
    if len(pointsMax) > 2:
        test = active_edge
        test = sorted(test, key = lambda point: ((point_new[1]-point[0][1])**2+(point_new[0]-point[0][0])**2)**0.5 + ((point_new[1]-point[1][1])**2+(point_new[0]-point[1][0])**2)**0.5)
        c.create_line(test[0][0][0],test[0][0][1],point_new[0],point_new[1])
        c.create_line(test[0][1][0],test[0][1][1],point_new[0],point_new[1])
        edge1 = [test[0][0],point_new]
        edge2 = [test[0][1],point_new]
        active_edge.append(edge1)
        active_edge.append(edge2)
        active_edge.remove(test[0])
    elif len(pointsMax) == 2:
        c.create_line(pointsMax[0][0],pointsMax[0][1],pointsMax[1][0],pointsMax[1][1])
        edge = [pointsMax[0],pointsMax[1]]
        active_edge.append(edge)
        
def close(event):
    global active_edge
    for edge1 in active_edge:
        for edge2  in active_edge:
            if edge1 != edge2:
                if edge1[0] == edge2[0]:
                    c.create_line(edge1[1][0],edge1[1][1],edge2[1][0],edge2[1][1])
                    active_edge.remove(edge1)
                    active_edge.remove(edge2)
                elif edge1[1] == edge2[0]:
                    c.create_line(edge1[0][0],edge1[0][1],edge2[1][0],edge2[1][1])
                    active_edge.remove(edge1)
                    active_edge.remove(edge2)
                    
def Voron(event):
    vor = Voronoi(pointsMax)
    print(vor.vertices)
    fig = voronoi_plot_2d(vor)
    plt.show()
        
    

        
root = Tk()

mainmenu = Menu(root) 
root.config(menu=mainmenu)
segmentMenu = Menu(mainmenu, tearoff=0)
segmentMenu.add_command(label="Очистить", command=zero)


mainmenu.add_cascade(label="Алгоритм", menu=segmentMenu)


c = Canvas(width=1000, height=1000, bg='white')

c.bind("<Button-1>", Delone)
c.bind("<Button-2>", close)
c.bind("<Button-3>", Voron)

c.grid(row=6, column=3)


root.mainloop()