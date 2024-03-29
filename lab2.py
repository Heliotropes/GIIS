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
    
    
def set_circle():
    global choice
    choice = 1
    
def set_elips():
    global choice
    choice = 2
        
def set_gip():
    global choice
    choice = 3

def set_par():
    global choice
    choice = 4
    
def make_choice():
    global choice
    if choice == 1:
        create_circle(number)
    if choice == 2:
        create_elips(number)
    if choice == 3:
        create_gip(number)
    if choice == 4:
        create_par(number)
    
def get_cor():
    x1 = float(e1.get())
    y1 = float(e2.get())
    return x1,y1

def net():
    x,y = 0,0
    while(x != 1000):
        c.create_line(x, 0, x, 1000)
        x+=30
    while(y != 1000):
        c.create_line(0, y, 1000, y)
        y+=30
    
def create_circle(number):
    c.create_rectangle(0,0,1920,1080, fill='white')
    
    R,R = get_cor()
    d = 3-2*R
    x = 0
    y = R
    if number == 0:
        i=  y
    else:
        i = number 
    while(x <=i):
        c.create_rectangle(x*30 + (R+1)*30, y*30 + (R+1)*30,(x+1)*30 + (R+1)*30, (y+1)*30 + (R+1)*30, fill='black')
        c.create_rectangle(y*30+ (R+1)*30, x*30+ (R+1)*30,(y+1)*30+ (R+1)*30, (x+1)*30+ (R+1)*30, fill='black')
        c.create_rectangle(-x*30 + (R+1)*30, y*30 + (R+1)*30,-(x+1)*30 + (R+1)*30, (y+1)*30 + (R+1)*30, fill='black')
        c.create_rectangle(-y*30+ (R+1)*30, x*30+ (R+1)*30,-(y+1)*30+ (R+1)*30, (x+1)*30+ (R+1)*30, fill='black')
        c.create_rectangle(x*30 + (R+1)*30, -y*30 + (R+1)*30,(x+1)*30 + (R+1)*30, -(y+1)*30 + (R+1)*30, fill='black')
        c.create_rectangle(y*30+ (R+1)*30, -x*30+ (R+1)*30,(y+1)*30+ (R+1)*30, -(x+1)*30+ (R+1)*30, fill='black')
        c.create_rectangle(-x*30 + (R+1)*30, -y*30 + (R+1)*30,-(x+1)*30 + (R+1)*30, -(y+1)*30 + (R+1)*30, fill='black')
        c.create_rectangle(-y*30+ (R+1)*30, -x*30+ (R+1)*30,-(y+1)*30+ (R+1)*30, -(x+1)*30+ (R+1)*30, fill='black')
        if d < 0:
            d+= 4*x + 6
        else:
            d+=4*(x-y)+10
            y-=1
            i-=1 
        x+=1
              
def create_elips(number):
    c.create_rectangle(0,0,1920,1080, fill='white')
    
    a,b = get_cor()
    x = 0
    y = b
    d = 4*b*b*(x+1)*(x+1)+a*a*(2*y-1)*(2*y-1)-4*b*b*a*a
    if number == 0:
        i= y
    else:
        i = number 
    while(a*a*(2*y-1) > 2*b*b*(x+1)):
        c.create_rectangle(x*30 + (a+2)*30, y*30 + (a+2)*30,(x+1)*30 + (a+2)*30, (y+1)*30 + (a+2)*30, fill='black')
        c.create_rectangle(-x*30 + (a+2)*30, y*30 + (a+2)*30,-(x+1)*30 + (a+2)*30, (y+1)*30 + (a+2)*30, fill='black')
        c.create_rectangle(x*30 + (a+2)*30, -y*30 + (a+2)*30,(x+1)*30 + (a+2)*30, -(y+1)*30 + (a+2)*30, fill='black')
        c.create_rectangle(-x*30 + (a+2)*30, -y*30 + (a+2)*30,-(x+1)*30 + (a+2)*30, -(y+1)*30 + (a+2)*30, fill='black')
        if d < 0:
            d+= 4*b*b*(2*x+3)
        else:
            d+= 4*b*b*(2*x+3) - 8*a*a*(y-1)
            y-=1
            i-=1
            if i == 0:
                break 
        x+=1
    d = b*b*(2*x+1)*(2*x+1)+4*a*a*(y+1)*(y+1)-4*b*b*a*a
    while(i >= 0):
        c.create_rectangle(x*30 + (a+2)*30, y*30 + (a+2)*30,(x+1)*30 + (a+2)*30, (y+1)*30 + (a+2)*30, fill='black')
        c.create_rectangle(-x*30 + (a+2)*30, y*30 + (a+2)*30,-(x+1)*30 + (a+2)*30, (y+1)*30 + (a+2)*30, fill='black')
        c.create_rectangle(x*30 + (a+2)*30, -y*30 + (a+2)*30,(x+1)*30 + (a+2)*30, -(y+1)*30 + (a+2)*30, fill='black')
        c.create_rectangle(-x*30 + (a+2)*30, -y*30 + (a+2)*30,-(x+1)*30 + (a+2)*30, -(y+1)*30 + (a+2)*30, fill='black')
        if d < 0:
            y-=1
            d+= 4*a*a*(2*y+3)
        else:
            y-=1
            d+= -8*b*b*(x+1) + 4*a*a*(2*y+3)
            x+=1 
        i-=1
        

def create_gip(number):
    c.create_rectangle(0,0,1920,1080, fill='white')
    
    a,b = get_cor()
    x = 0
    y = 0
    if number == 0:
        i=  c.winfo_width()
    else:
        i = number 
    while x < i:
            x = x + 0.1
            y = b / (x + a)* 20
            c.create_rectangle(x*20, y*20,(x+1)*20, ( y+1)*20, fill='black')

def create_par(number):
    c.create_rectangle(0,0,1920,1080, fill='white')
    
    p,p = get_cor()
    x = 0 
    y=0 
    if number == 0:
        i=  c.winfo_width()
    else:
        i = number 
    while x < i:
            x = x + 0.1
            y = pow(2*p*x, 0.5) 
            c.create_rectangle(x*30, y*30 +400,(x+1)*30, ( y+1)*30+400, fill='black')
            c.create_rectangle(x*30, -y*30 + p*25 +400,(x+1)*30, -( y+1)*30 +p*25+400, fill='black')
        
root = Tk()

mainmenu = Menu(root) 
root.config(menu=mainmenu)
segmentMenu = Menu(mainmenu, tearoff=0)
segmentMenu.add_command(label="Окружность", command=set_circle)
segmentMenu.add_command(label="Элипс", command=set_elips)
segmentMenu.add_command(label="Гипербола", command=set_gip)
segmentMenu.add_command(label="Парабола", command=set_par)

mainmenu.add_cascade(label="Линии", menu=segmentMenu)

e1 = Entry(width=10)
e2 = Entry(width=10)

c = Canvas(width=1000, height=1000, bg='white')


b1 = Button(text="Ввод", command=make_choice)
b2 = Button(text="<<",width = 4, command=back)
b3 = Button(text="0",width = 4, command=zero)
b4 = Button(text=">>",width = 4, command=ahead)

e1.grid(row=0, column=0)
e2.grid(row=0, column=1)

b1.grid(row=2, column=1)
b2.grid(row=3, column=0)
b3.grid(row=3, column=1)
b4.grid(row=3, column=2)

c.grid(row=4, column=4)


root.mainloop()