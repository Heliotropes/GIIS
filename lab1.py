from tkinter import *

choice = 0
number=0

def ahead():
    global number
    number+=1
    make_choice()
    
def back():
    global number
    if number > 0:
        number-=1
    make_choice()
    
def zero():
    global number
    number = 0
    c.create_rectangle(0,0,1920,1080, fill='white')
    net()
    
def set_DDA():
    global choice
    choice = 1
    
def set_B():
    global choice
    choice = 2
    
def set_WU():
    global choice
    choice = 3
    
def make_choice():
    global choice
    if choice == 1:
        create_segment_DDA(number)
    if choice == 2:
        create_segment_B(number)
    if choice == 3:
        create_segment_WU(number)
    
def get_point():
    x1 = float(e1.get())
    y1 = float(e2.get())
    x2 = float(e3.get())
    y2 = float(e4.get())
    return x1,y1,x2,y2

def net():
    x,y = 0,0
    while(x != 1000):
        c.create_line(x, 0, x, 1000)
        x+=50
    while(y != 1000):
        c.create_line(0, y, 1000, y)
        y+=50
    
def create_segment_DDA(number):
    c.create_rectangle(0,0,1920,1080, fill='white')
    net()
    x_start,y_start,x_end,y_end = get_point()
    x1,y1 = x_start,y_start
    c.create_rectangle(x1*50,y1*50,(x1+1)*50,(y1+1)*50, fill='black')
    delta_x,delta_y = (x_end - x_start), (y_end - y_start)
    N = abs(delta_x) if abs(delta_x) > abs(delta_y) else abs(delta_y)
    if number == 0:
        i = N
    else:
        i = number   
    while (i != 0):
        x1= x1 + delta_x/N
        y1= y1 + delta_y/N
        c.create_rectangle(round(x1)*50,round(y1)*50,(round(x1)+1)*50,(round(y1)+1.)*50, fill='black')
        i-=1
        
def create_segment_B(number):
    c.create_rectangle(0,0,1920,1080, fill='white')
    net()
    x1,y1,x2,y2 = get_point()
    X=  x1
    Y=  y1 
    Px= x2 - x1 
    Py= y2 - y1 
    E=  2*Py - Px 
    if number == 0:
        i=  Px
    else:
        i = number 
    c.create_rectangle(X*50, Y*50,(X+1)*50, (Y+1)*50, fill='black')    
    while (i >= 0): 
        if (E  >=  0): 
            X= X + 1 
            Y= Y + 1 
            E= E + 2*(Py - Px) 
        else:
            X= X + 1 
            E= E + 2*Py 
        c.create_rectangle(X*50, Y*50,(X+1)*50, (Y+1)*50, fill='black')   
        i-=1  
 
def plot(x, y, a):
    if a >= 0.75:
        c.create_rectangle(x*50,y*50,(x+1)*50,(y+1)*50,fill='#000000')
    elif a >= 0.50:
        c.create_rectangle(x*50,y*50,(x+1)*50,(y+1)*50,fill='#666666')
    elif a >= 0.25:
        c.create_rectangle(x*50,y*50,(x+1)*50,(y+1)*50,fill='#808080')
    elif a >= 0.0:
        c.create_rectangle(x*50,y*50,(x+1)*50,(y+1)*50,fill='#a0a0a0')
 
def fpart(x):  
    return x%1

def create_segment_WU(number):
    c.create_rectangle(0,0,1920,1080, fill='white')
    net()
    x1,y1,x2,y2 = get_point()  
    if x2 < x1:
        t = x1
        x1 = x2
        x2 = t
        t = y1
        y1 = y2
        y2 = t
    dx= x2 - x1
    dy = y2 - y1
    gradient= dy / dx
    
    xend= round(x1) 
    yend= y1 + gradient * (xend - x1)
    xgap= 1 - fpart(x1 + 0.5)
    xpxl1= xend
    ypxl1= yend - fpart(yend)
    plot(xpxl1, ypxl1, (1 - fpart(yend)) * xgap)
    plot(xpxl1, ypxl1 + 1, fpart(yend) * xgap)
    intery= yend + gradient 
    
    xend= round(x2)
    yend= y2 + gradient * (xend - x2)
    xgap= fpart(x2 + 0.5)
    xpxl2= xend 
    ypxl2= yend - fpart(yend)
    plot(xpxl2, ypxl2, (1 - fpart(yend)) * xgap)
    plot(xpxl2, ypxl2 + 1, fpart(yend) * xgap)
    
    if number == 0:
        i = xpxl2 - ( xpxl1 + 1)
    else:
        i = number 
    
    for x in range(xpxl1 + 1,xpxl1 + 1 +i ):
        plot(x, intery- fpart(intery), 1 - fpart(intery))
        plot(x, intery- fpart(intery) + 1, fpart(intery))
        intery = intery + gradient
        
root = Tk()

mainmenu = Menu(root) 
root.config(menu=mainmenu)
segmentMenu = Menu(mainmenu, tearoff=0)
segmentMenu.add_command(label="ЦДА", command=set_DDA)
segmentMenu.add_command(label="Целочисленный алгоритм Брезенхема", command=set_B)
segmentMenu.add_command(label="Алгоритм Ву", command=set_WU)

mainmenu.add_cascade(label="Отрезок", menu=segmentMenu)

e1 = Entry(width=10)
e2 = Entry(width=10)
e3 = Entry(width=10)
e4 = Entry(width=10)

c = Canvas(width=1000, height=1000, bg='white')
net()

b1 = Button(text="Ввод", command=make_choice)
b2 = Button(text="<<",width = 4, command=back)
b3 = Button(text="0",width = 4, command=zero)
b4 = Button(text=">>",width = 4, command=ahead)

e1.grid(row=0, column=0)
e2.grid(row=0, column=1)
e3.grid(row=1, column=0)
e4.grid(row=1, column=1)

b1.grid(row=2, column=1)
b2.grid(row=3, column=0)
b3.grid(row=3, column=1)
b4.grid(row=3, column=2)

c.grid(row=4, column=4)


root.mainloop()