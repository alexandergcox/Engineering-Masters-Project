#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *#import tkinter  


# In[ ]:


from tkinter import ttk  


# In[ ]:


import os.path #import os.path module 


# In[ ]:


import os  


# In[ ]:


path= 'C:/Users/SysAdmin/Desktop'#specify the path for the text file  
file=os.path.join(path,"gcode_movement.txt")# name the text file  


# In[ ]:


def Movement(*args):#define the movement function  
with open (file, "w") as f:#open the text file to write to  
cycles=int(CycInp.get())#get the number of cycles from UI  
for i in range(cycles):#define the for loop to run the code over the number of cycle
z_input = int(Zinp.get()) #get the nozzle height from the UI  
    
    if z_input <= 160 and z_input >= 0:  
z_height = "Nozzle Height: %dmm " % (z_input)      
 gcode_z = "G0 Z%d \n" % (z_input) #write the gcode command for nozzle height to the text file  
f.write (gcode_z)  
      
pcb_x = int(Xinp.get())#get the substrate width from the UI  
if pcb_x <= 220 and pcb_x > 0: # define the starting position of the nozzle  
       pcb_X_startpoint=110 - (pcb_x/2)  # start point of X if pcb in center  
        gcode_x_start="G0 X%d\n" %(pcb_X_startpoint)  
        f.write (gcode_x_start)#write the X coordinate of the startpoint to the text file  
        gcode_xmove = pcb_x + pcb_X_startpoint#define the forward movement in X plane  


# In[ ]:



def Movement(*args):#define the movement function  
with open (file, "w") as f:#open the text file to write to  
cycles=int(CycInp.get())#get the number of cycles from UI  
 for i in range(cycles):#define the for loop to run the code over the number of cycles  
    z_input = int(Zinp.get()) #get the nozzle height from the UI  
  
 if z_input <= 160 and z_input >= 0:  
z_height = "Nozzle Height: %dmm " % (z_input)      
gcode_z = "G0 Z%d \n" % (z_input) #write the gcode command for nozzle height to the text file  
      f.write (gcode_z)  
        
    pcb_x = int(Xinp.get())#get the substrate width from the UI  
    if pcb_x <= 220 and pcb_x > 0: # define the starting position of the nozzle  
        pcb_X_startpoint=110 - (pcb_x/2)  # start point of X if pcb in center   
        gcode_x_start="G0 X%d\n" %(pcb_X_startpoint)  
        f.write (gcode_x_start)#write the X coordinate of the startpoint to the text file  
        gcode_xmove = pcb_x + pcb_X_startpoint#define the forward movement in X plane  
        pcb_y = int(Yinp.get())# get the substrate height from the UI  

    if pcb_y <= 220 and pcb_y >= 0: # define the Y start point  
        pcb_y_startpoint = 110 - (pcb_y/2) #start point of Y if pcb in center  
        gcode_y_startpoint = "G0 Y%d \n" %(pcb_y_startpoint)  
        f.write(gcode_y_startpoint)#write the Y coordinateof the start point to the text file  
        y_increment=pcb_y_startpoint#set the y increment to be equal to the start point   
  
      
        x_reverse = pcb_X_startpoint #define the reverse movement in X  
        g_code_x_reverse = "G0 X%d \n" % (x_reverse)  
          
            y_div = int(Ydiv.get())#get the substrate height division from the UI  
            speed = int(Sinp.get())#get the speed value from the UI  
            
        if speed <=180 and speed >= 1:  
            gcode_speed = int(speed*(1000/15))#convert real speed into the gcode speed  
            delay = float(DelInp.get())#get the delay value from the UI  
            servo=int(ServoInp.get())   #get the servo turn angle from the UI  
            servo_init="M05\n"#servo reverse movement  
            f.write ("M03 s{0}\n".format(servo))#write the servo forward movement command to the text file  
            
        while y_increment < (pcb_y+pcb_y_startpoint):#start path creating loop  
        gcode_xwidth = "G1 X{0} F{1} \n".format(gcode_xmove,gcode_speed)#forward in X  
        f.write (gcode_xwidth)  
          
        y_increment = y_increment + (pcb_y/y_div)  
        gcode_y_increment = "G1 Y{0} F{1} \n".format(y_increment,gcode_speed)#move by 1 y increment  
        f.write(gcode_y_increment)  
  
        g_code_x_reverse = "G1 X{0} F{1} \n".format(x_reverse,gcode_speed)#reverse in x  
        f.write(g_code_x_reverse)  
          
        y_increment = y_increment +(pcb_y/y_div)  
        gcode_y_increment = "G1 Y{0} F{1} \n".format(y_increment,gcode_speed)  
        f.write(gcode_y_increment)  
  
        gcode_xwidth = "G1 X{0} F{1} \n".format(gcode_xmove,gcode_speed)  
        f.write (gcode_xwidth)  
         
  
         
    f.write (servo_init)#reset servo  
    f.write ("G0 X0 Y0\n")#go to X and Y origin  
    f.write ("G0 Z0\n")#go to Z origin  
    f.write ("G4 P{0}\n".format(delay))#write the delay command to the file  
     


# In[ ]:


def validateZ(text):#define a validation function  
    if text=="":  
    return True  
    try:  
    value= int(text)#accept only integers  
    except ValueError:  
    return False  
    return 0 < value <=160#accept integers in this range  
  


# In[ ]:


def validateX(text1):  
    if text1=="":  
    return True  
    try:  
    value= int(text1)  
    except ValueError:  
    return False  
    return 0 < value <=220    


# In[ ]:


def validateY(text2):  
    if text2=="":  
    return True  
    try:  
    value= int(text2)  
    except ValueError:  
    return False  
    return 0 < value <=220  
  
def validateYdiv(text3):  
    if text3=="":  
    return True  
    try:  
        value= int(text3)  
    except ValueError:  
    return False  
    return 0 < value <=220  
  
def validateSpeed(text4):  
    if text4=="":  
    return True  
    try:  
    value= int(text4)  
    except ValueError:  
    return False  
    return 0 < value <=180  
117.	      
118.	def validateCycles(text5):  
119.	  
120.	    if text5=="":  
121.	     return True  
122.	    try:  
123.	      value= int(text5)  
124.	    except ValueError:  
125.	     return False  
126.	    return 0 < value  
127.	  
128.	def validateDelay(text6):  
129.	    if text6=="":  
130.	     return True  
131.	    try:  
132.	      value= float(text6)  
133.	    except ValueError:  
134.	     return False  
135.	    return 0.0 < value <100000000000.0  
136.	  
137.	def validateServo(text7):  
138.	    if text7=="":  
139.	     return True  
140.	    try:  
141.	     value= int(text7)  
142.	    except ValueError:  
143.	     return False  
144.	    return 0< value <80  
145.	  
146.	def Draw(*args):#define the draw function  
147.	    root= Tk()#create the main window  
148.	    root.resizable(False,False)#make window not resizable  
149.	    root.columnconfigure(0,weight=1)#configure window geometry  
150.	    root.rowconfigure(0,weight=1)  
151.	    root.geometry('430x300')  
152.	    canvas = Canvas(root)#start new canvas  
153.	    canvas.grid(column=0, row=0, sticky=(N, W, E, S))  
154.	    canvas.create_rectangle(10,10,230,230,width=2)#create a rectangle to illustrate the limits of motion  
155.	      
156.	    x=int(Xinp.get())#get the user inputs   
157.	    if x <= 220 and x > 0:  
158.	     pXstart=120 - (x/2)   
159.	     gXmove = x + pXstart  
160.	          
161.	    y=int(Yinp.get())  
162.	      
163.	    pYstart = 120 - (y/2) #start point of Y if pcb in center  
164.	    y_increment = pYstart  
165.	    x_reverse = pXstart  
166.	  
167.	    ydiv=int(Ydiv.get())  
168.	  
169.	    canvas.create_text(330,10,fill="black",font="Times 8 bold",text="Substrate width : {0} mm".format(x))#create text entities that show key values  
170.	    canvas.create_text(330,30,fill="black",font="Times 8 bold",text="Substrate height : {0} mm".format(y))  
171.	    canvas.create_text(330,50,fill="black",font="Times 8 bold",text="Substrate height division : {0} mm".format(ydiv))  
172.	  
173.	    canvas.create_line(10,10,pXstart,pYstart,fill="red",width=1)#create a line from the origin to the start point  
174.	  
175.	    coordinates=[pXstart,pYstart]#create a list for the path coordinates  
176.	      
177.	    while y_increment < (y+pYstart):#start a path creating loop similar to the one in Movement  
178.	     y_increment = y_increment + (y/ydiv)  
179.	     lasty=y_increment - (y/ydiv)  
180.	     a=[gXmove,lasty]  
181.	     coordinates.append(a)  
182.	     b=[gXmove,y_increment]  
183.	     coordinates.append(b)  
184.	     y_increment = y_increment + (y/ydiv)  
185.	     lasty=y_increment - (y/ydiv)  
186.	     c=[x_reverse,lasty]  
187.	     coordinates.append(c)  
188.	     d=[x_reverse,y_increment]  
189.	     coordinates.append(d)  
190.	    else:  
191.	     e=[gXmove,y_increment]  
192.	     coordinates.append(e)  
193.	  
194.	    path = canvas.create_line(coordinates,fill="red",width=1)#build a path from the list of coordinates  
195.	      
196.	           
197.	    root.mainloop()#start the main loop  
198.	      
199.	root= Tk()#creat the main window  
200.	root.title("XYZ Motion System")#title the window  
201.	root.resizable(False,False)#make window not resizable  
202.	  
203.	mainframe = ttk.Frame(root, padding="3 3 12 12")#create a new frame  
204.	mainframe.grid(column=0, row=0, sticky=(N, W, E, S))#configure the frame  
205.	mainframe.columnconfigure(0, weight=1)  
206.	mainframe.rowconfigure(0, weight=1)  
207.	  
208.	vZ=(mainframe.register(validateZ),'%P')#register the validation functions  
209.	vX=(mainframe.register(validateX),'%P')  
210.	vY=(mainframe.register(validateY),'%P')  
211.	vYd=(mainframe.register(validateYdiv),'%P')  
212.	vS=(mainframe.register(validateSpeed),'%P')  
213.	vC=(mainframe.register(validateCycles),'%P')  
214.	vd=(mainframe.register(validateDelay),'%P')  
215.	vServo=(mainframe.register(validateServo),'%P')  
216.	  
217.	Zinp = IntVar ()#create variables for user input  
218.	Xinp = IntVar ()  
219.	Yinp = IntVar ()  
220.	Ydiv = IntVar ()  
221.	Sinp = IntVar ()  
222.	CycInp = IntVar ()  
223.	DelInp = DoubleVar ()  
224.	ServoInp = IntVar ()  
225.	  
226.	Z_entry=ttk.Entry(mainframe,validate = "key",validatecommand=vZ,width=10,textvariable = Zinp)#create user entry widgets  
227.	Z_entry.grid(column = 2,row = 1, sticky=(W,E))#position widgets  
228.	  
229.	ttk.Label(mainframe,text="Z height in mm (min:0 , max: 160)").grid(column=3,row=1, sticky=(W,E))#create label widgets to describe the entry windows  
230.	  
231.	X_entry=ttk.Entry(mainframe,validate = "key",validatecommand=vX,width=10,textvariable = Xinp)  
232.	X_entry.grid(column=2,row=3,sticky=(W,E))  
233.	  
234.	ttk.Label(mainframe,text="Substrate Width in mm (min:0 , max:220)").grid(column=3,row=3, sticky=(W,E))  
235.	  
236.	Y_entry=ttk.Entry(mainframe,validate = "key",validatecommand=vY,width=10,textvariable = Yinp)  
237.	Y_entry.grid(column = 2,row = 5, sticky=(W,E))  
238.	   
239.	ttk.Label(mainframe,text="Substrate Height in mm (min:0 , max:220)").grid(column=3,row=5, sticky=(W,E))  
240.	   
241.	Ydiv_entry=ttk.Entry(mainframe,validate = "key",validatecommand=vYd,width=10,textvariable = Ydiv,)  
242.	Ydiv_entry.grid(column = 2,row = 7, sticky=(W,E))  
243.	  
244.	ttk.Label(mainframe,text="Substrate Height Division").grid(column=3,row=7, sticky=(W,E))  
245.	  
246.	Speed_entry=ttk.Entry(mainframe,validate = "key",validatecommand=vS,width=10,textvariable = Sinp)  
247.	Speed_entry.grid(column = 2,row = 9, sticky=(W,E))  
248.	  
249.	ttk.Label(mainframe,text="Spray Speed in mm/s (min:1, max:180)").grid(column=3,row=9, sticky=(W,E))  
250.	  
251.	Cycles_entry=ttk.Entry(mainframe,validate = "key",validatecommand=vC,width=10,textvariable = CycInp)  
252.	Cycles_entry.grid(column = 2,row = 11, sticky=(W,E))  
253.	  
254.	ttk.Label(mainframe,text="Number of Cycles").grid(column=3,row=11, sticky=(W,E))  
255.	  
256.	Delay_entry=ttk.Entry(mainframe,validate = "key",validatecommand=vd,width=10,textvariable = DelInp)  
257.	Delay_entry.grid(column = 2,row = 13, sticky=(W,E))  
258.	  
259.	ttk.Label(mainframe,text="Delay Between Cycles in Seconds").grid(column=3,row=13, sticky=(W,E))  
260.	  
261.	Servo_entry=ttk.Entry(mainframe,validate = "key",validatecommand=vServo,width=10,textvariable = ServoInp)  
262.	Servo_entry.grid(column = 2,row = 15, sticky=(W,E))  
263.	  
264.	ttk.Label(mainframe,text="Servo rotation angle(min :0 , max :80)").grid(column=3,row=15, sticky=(W,E))  
265.	  
266.	ttk.Button(mainframe,text="Run",command = Movement).grid(column = 4,row = 17,sticky=W)#create a button that starts the Movement function  
267.	  
268.	ttk.Button(mainframe,text="Draw",command = Draw).grid(column = 4,row = 19,sticky=W)#create a button that starts the Draw function  
269.	  
270.	for child in mainframe.winfo_children():#add additional horizontal and vertical padding to all elements of UI  
271.	    child.grid_configure(padx=5, pady=5)  
272.	  
273.	root.mainloop()#start the main loop  


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




