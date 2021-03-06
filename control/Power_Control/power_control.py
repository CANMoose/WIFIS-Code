

#relies on dlipower.py, (from https://pypi.python.org/pypi/dlipower)  which is 
#uploaded here as well gui to control web power switches
#updates to show changes made from other places than this app but LAGS so no 
#pressing buttons a lot without being patient.

# Miranda Jarvis Oct 2015

import dlipower
from pylab import *
from Tkinter import *
from time import *
import ttk
from sys import exit

class MainApplication(Frame): 
    #this class holds all of the gui into and button functions. 
    
    def __init__(self,master,switch1,switch2): #sets up gui stuff 
        Frame.__init__(self, master)
        self.grid()
        self.switch1 = switch1
        self.switch2 = switch2
        self.create_widgets()
        self.update()

    def create_widgets(self): 

        #label columns 
        Label(self, text="Outlet", font='bold').grid(row=0, column=0, \
            padx=15)
        Label(self, text="Hostname", font='bold').grid(row=0, column=1, \
            padx=15)
        Label(self, text="State", font='bold').grid(row=0, column=2, padx=15)
        Label(self, text="Toggle", font='bold').grid(row=0, column=3, padx=15)


        #outlet number this is is slihglty useful
        Label(self, text="1").grid(row=1, column=0, padx=15)
        Label(self, text="2").grid(row=2, column=0, padx=15)
        Label(self, text="3").grid(row=3, column=0, padx=15)
        Label(self, text="4").grid(row=4, column=0, padx=15)
        Label(self, text="5").grid(row=5, column=0, padx=15)
        Label(self, text="6").grid(row=6, column=0, padx=15)
        Label(self, text="7").grid(row=7, column=0, padx=15)

        #seperate power control 1 from two, should probalby label which is 
        #which but haven't for now.
        ttk.Separator(self,orient=HORIZONTAL).grid(row=8, columnspan=4, \
            sticky="ew")

        Label(self, text=" 1").grid(row=9, column=0, padx=15)
        Label(self, text=" 2").grid(row=10, column=0, padx=15)
        Label(self, text=" 3").grid(row=11, column=0, padx=15)
        #Label(self, text=" 4").grid(row=12, column=0, padx=15)

        #gets description from power bars of which plug is which, to change 
        #this log on to their IP addresses in web browser (IP should be writtin
        #on bars and later in this code) 
        Label(self, text=self.switch2[0].description).grid(row=1, column=1, padx=15)
        Label(self, text=self.switch2[1].description).grid(row=2, column=1, padx=15)
        Label(self, text=self.switch2[2].description).grid(row=3, column=1, padx=15)
        Label(self, text=self.switch2[3].description).grid(row=4, column=1, padx=15)
        Label(self, text=self.switch2[4].description).grid(row=5, column=1, padx=15)
        Label(self, text=self.switch2[5].description).grid(row=6, column=1, padx=15)
        Label(self, text=self.switch2[6].description).grid(row=7, column=1, padx=15)

        Label(self, text=self.switch1[0].description).grid(row=9, column=1, padx=15)
        Label(self, text=self.switch1[1].description).grid(row=10, column=1, \
            padx=15)
        Label(self, text=self.switch1[2].description).grid(row=11, column=1, \
            padx=15)
        #Label(self, text=switch1[3].description).grid(row=12, column=1, 
            #padx=15)


        #look if each plug is currently on or off, print status to reflect this
        #look at each for on or off to get colour right 
        c=strs = ["" for x in range(7)]
        for i in arange(7):
            if self.switch2[i].state=='OFF': c[i]='red'
            else: c[i]='green'
        self.status1 = Label(self, text=self.switch2[0].state, fg =c[0] )
        self.status1.grid(row=1, column=2)
        self.status2 = Label(self, text=self.switch2[1].state, fg =c[1])
        self.status2.grid(row=2, column=2)
        self.status3 = Label(self, text=self.switch2[2].state,fg =c[2])
        self.status3.grid(row=3, column=2)
        self.status4 = Label(self, text=self.switch2[3].state,fg =c[3])
        self.status4.grid(row=4, column=2)
        self.status5 = Label(self, text=self.switch2[4].state,fg =c[4])
        self.status5.grid(row=5, column=2)
        self.status6 = Label(self, text=self.switch2[5].state,fg =c[5])
        self.status6.grid(row=6, column=2)
        self.status7 = Label(self, text=self.switch2[6].state,fg =c[6])
        self.status7.grid(row=7, column=2)
        #self.status8 = Label(self, text=switch2[7].state)
        #self.status8.grid(row=8, column=2)

        #have to look at colours again for power bar 1  
        c=strs = ["" for x in range(4)]         
        for i in arange(4):
            if self.switch1[i].state=='OFF': c[i]='red'
            else: c[i]='green'

        self.status8 = Label(self, text=self.switch1[0].state, fg =c[0] )
        self.status8.grid(row=9, column=2)
        self.status9 = Label(self, text=self.switch1[1].state, fg =c[1])
        self.status9.grid(row=10, column=2)
        self.status10 = Label(self, text=self.switch1[2].state,fg =c[2])
        self.status10.grid(row=11, column=2)
        #self.status11 = Label(self, text=switch1[3].state,fg =c[3])
        #self.status11.grid(row=12, column=2)

        #make buttons to toggle on or off state, each has to have own function 
        #defined later
        Button(self, text="On/Off", command=self.toggle_plug1, width=5).grid(\
            row=1, column=3)
        Button(self, text="On/Off", command=self.toggle_plug2, width=5).grid(\
            row=2, column=3)
        Button(self, text="On/Off", command=self.toggle_plug3, width=5).grid(\
            row=3, column=3)
        Button(self, text="On/Off", command=self.toggle_plug4, width=5).grid(\
            row=4, column=3)
        Button(self, text="On/Off", command=self.toggle_plug5, width=5).grid(\
            row=5, column=3)
        Button(self, text="On/Off", command=self.toggle_plug6, width=5).grid(\
            row=6, column=3)
        Button(self, text="On/Off", command=self.toggle_plug7, width=5).grid(\
            row=7, column=3)
        #Button(self, text="On/Off", command=self.toggle_plug8, width=5).grid(
            #row=8, column=3)
        

        Button(self, text="On/Off", command=self.toggle_plug8, width=5).grid(\
            row=9, column=3)
        Button(self, text="On/Off", command=self.toggle_plug9, width=5).grid(\
            row=10, column=3)
        Button(self, text="On/Off", command=self.toggle_plug10, width=5).grid(\
            row=11, column=3)
        #Button(self, text="On/Off", command=self.toggle_plug11, width=5).grid(\
            #row=12, column=3)


    def update_labels(self): 
        #this guy gets looped over eternally to update status of plugs as they 
        #get changed in other places (IE at the bar itself, in the web browser
        #or via other guis written for control purposes. This is what makes the
        #whole code lag a bit...
        
        #check if each plug on or off again and set colour and text apropriatly

        c=strs = ["" for x in range(7)]         
        
        for i in arange(7):
            if self.switch2[i].state=='OFF': c[i]='red'
            else: c[i]='green'

        self.status1['text']=self.switch2[0].state
        self.status1['fg']=c[0]

        self.status2['text']=self.switch2[1].state
        self.status2['fg']=c[1]

        self.status3['text']=self.switch2[2].state
        self.status3['fg']=c[2]

        self.status4['text']=self.switch2[3].state
        self.status4['fg']=c[3]

        self.status5['text']=self.switch2[4].state
        self.status5['fg']=c[4]

        self.status6['text']=self.switch2[5].state
        self.status6['fg']=c[5]

        self.status7['text']=self.switch2[6].state
        self.status7['fg']=c[6]



        c=strs = ["" for x in range(4)]     
        for i in arange(4):
            if self.switch1[i].state=='OFF': c[i]='red'
            else: c[i]='green'

        self.status8['text']=self.switch1[0].state
        self.status8['fg']=c[0]

        self.status9['text']=self.switch1[1].state
        self.status9['fg']=c[1]

        self.status10['text']=self.switch1[2].state
        self.status10['fg']=c[2]

        #self.status11['text']=switch1[3].state
        #self.status11['fg']=c[3]



        #print 'doing things'
        self.update() #update gui
        self.after(100,self.update_labels) 


#These are the toggle plug buttons. each is the same turns the right plug 
#on or off and changes the status to reflect this change
    def toggle_plug1(self):
        self.update()
        n=0
        status=self.switch2[n].state
        if status=='ON': 
            self.switch2[n].state='OFF'
            self.status1["text"] = "OFF"
            self.status1["fg"] = "red"
        else: 
            self.switch2[n].state='ON'
            self.status1["text"] = "ON"
            self.status1["fg"] = "green"
        self.update()

    def toggle_plug2(self):
        self.update()
        n=1
        status=self.switch2[n].state
        if status=='ON': 
            self.switch2[n].state='OFF'
            self.status2["text"] = "OFF"
            self.status2["fg"] = "red"
        else: 
            self.switch2[n].state='ON'
            self.status2["text"] = "ON"
            self.status2["fg"] = "green"
        self.update()

    def toggle_plug3(self):
        self.update()
        n=2
        status=self.switch2[n].state
        if status=='ON': 
            self.switch2[n].state='OFF'
            self.status3["text"] = "OFF"
            self.status3["fg"] = "red"
        else: 
            self.switch2[n].state='ON'
            self.status3["text"] = "ON"
            self.status3["fg"] = "green"
        self.update()

    def toggle_plug4(self):
        self.update()
        n=3
        status=self.switch2[n].state
        if status=='ON': 
            self.switch2[n].state='OFF'
            self.status4["text"] = "OFF"
            self.status4["fg"] = "red"
        else: 
            self.switch2[n].state='ON'
            self.status4["text"] = "ON"
            self.status4["fg"] = "green"
        self.update()

    def toggle_plug5(self):
        self.update()
        n=4
        status=self.switch2[n].state
        if status=='ON': 
            self.switch2[n].state='OFF'
            self.status5["text"] = "OFF"
            self.status5["fg"] = "red"
        else: 
            self.switch2[n].state='ON'
            self.status5["text"] = "ON"
            self.status5["fg"] = "green"
        self.update()

    def toggle_plug6(self):
        self.update()
        n=5
        status=self.switch2[n].state
        if status=='ON': 
            self.switch2[n].state='OFF'
            self.status6["text"] = "OFF"
            self.status6["fg"] = "red"
        else: 
            self.switch2[n].state='ON'
            self.status6["text"] = "ON"
            self.status6["fg"] = "green"
        self.update()

    def toggle_plug7(self):
        self.update()
        n=6
        status=self.switch2[n].state
        if status=='ON': 
            self.switch2[n].state='OFF'
            self.status7["text"] = "OFF"
            self.status7["fg"] = "red"
        else: 
            self.switch2[n].state='ON'
            self.status7["text"] = "ON"
            self.status7["fg"] = "green"
        self.update()


    def toggle_plug8(self):
        self.update()
        n=0
        status=self.switch1[n].state
        if status=='ON': 
            self.switch1[n].state='OFF'
            self.status8["text"] = "OFF"
            self.status8["fg"] = "red"
        else: 
            self.switch1[n].state='ON'
            self.status8["text"] = "ON"
            self.status8["fg"] = "green"
        self.update()

    def toggle_plug9(self):
        self.update()
        n=1
        status=self.switch1[n].state
        if status=='ON': 
            self.switch1[n].state='OFF'
            self.status9["text"] = "OFF"
            self.status9["fg"] = "red"
        else: 
            self.switch1[n].state='ON'
            self.status9["text"] = "ON"
            self.status9["fg"] = "green"
        self.update()

    def toggle_plug10(self):
        self.update()
        n=2
        status=self.switch1[n].state
        if status=='ON': 
            self.switch1[n].state='OFF'
            self.status10["text"] = "OFF"
            self.status10["fg"] = "red"
        else: 
            self.switch1[n].state='ON'
            self.status10["text"] = "ON"
            self.status10["fg"] = "green"
        self.update()

    def toggle_plug11(self):
        self.update()
        n=2
        status=self.switch1[n].state
        if status=='ON': 
            self.switch1[n].state='OFF'
            self.status11["text"] = "OFF"
            self.status11["fg"] = "red"
        else: 
            self.switch1[n].state='ON'
            self.status11["text"] = "ON"
            self.status11["fg"] = "green"
        self.update()


    #def toggle_plug8(self):
    #   n=7
    #   status=switch2[n].state
    #   if status=='ON': 
    #       switch2[n].state='OFF'
    #       self.status8["text"] = "OFF"
    #   else: 
    #       switch2[n].state='ON'
    #       self.status8["text"] = "ON"

def run_power_gui(mainloop = False):

    #connect to power bars
    print('Connecting to a DLI PowerSwitch at http://192.168.0.120 and '+\
        'another at http://192.168.0.110 ')  
    switch2 = dlipower.PowerSwitch(hostname="192.168.0.120", userid="admin",\
        password='9876')
    switch1 = dlipower.PowerSwitch(hostname="192.168.0.110", userid="admin",\
        password='9876')
    
    switch1[2].state='ON'

    root = Tk() 
    root.title("Power Switch Control") #name gui
    root.geometry("500x375") #gui size

    app = MainApplication(root,switch1,switch2) #initialize gui 
    
    #tell it to start doing the update_labels function after a few seconds
    app.after(5,app.update_labels)  

    return root,switch1,switch2

def run_power_gui_standalone():

    #connect to power bars
    print('Connecting to a DLI PowerSwitch at http://192.168.0.120 and '+\
        'another at http://192.168.0.110 ')  
    switch2 = dlipower.PowerSwitch(hostname="192.168.0.120", userid="admin",\
        password='9876')
    switch1 = dlipower.PowerSwitch(hostname="192.168.0.110", userid="admin",\
        password='9876')

    root = Tk() #something about gui
    root.title("Power Switch Control") #name gui
    root.geometry("500x375") #gui size

    app = MainApplication(root,switch1,switch2) #initialize gui 

    #tell it to start doing the update_labels function after a few seconds
    app.after(5,app.update_labels)  

    root.mainloop() #loop over gui until closed

if __name__ == '__main__':
    #run_power_gui()
    pass



    
