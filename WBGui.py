#Winged Boots GUI manager, by DaBoaz
#Version 0.16

from tkinter import *

class WBGui(Frame):
	
	def __init__(self, parent=None, server=None):
	#basic setting of the GUI
		Frame.__init__(self, parent)
		self.server = server
		self.pack(expand=YES, fill=BOTH)
		
		text = Text(self, state=DISABLED)
		text.pack(side=TOP)
		self.text = text
		text.config(state=DISABLED)
		
		ent = Entry(self)
		ent.pack(fill=BOTH)
		self.ent = ent
		
		self.msg = ""
		self.bind_all('<Return>', self.sendMsg)
		self.bind_all('<<PrintMsg>>', self.printMsg)
		
	def printMsg(self, event):
	#printing message
		msg = self.server.message
		self.printCon(msg+'\n')
	
	def sendMsg(self, event):
	#sending message to the other side
		msg = self.ent.get()
		self.ent.delete(0, END)
		self.printCon(msg+'\n')
		self.server.send(msg)
		
	def printCon(self, textToPrint):
	#printing text in the GUI field
		self.text.config(state=NORMAL)
		self.text.insert(END, textToPrint)
		self.text.config(state=DISABLED)