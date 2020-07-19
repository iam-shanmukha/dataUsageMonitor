#!/usr/bin/python
from tkinter import *
import os
root=Tk()
root.geometry("300x100")

def dataMonitor():
	os.system("cat /proc/net/dev | grep wlo1  >> wlo1Log")
	strings =os.popen("cat /proc/net/dev | grep wlo1").read()
	strings = strings.split(" ")[3]
	mb =int(strings)/(1024*1024) #converting Bytes into MegaBytes
	print("Data used is {:.2f} MB".format(mb))
	label = Label(root, text= "You have consumed {:.2f} MB since restart".format(mb))
	label.pack()
dataMonitor()
root.mainloop()