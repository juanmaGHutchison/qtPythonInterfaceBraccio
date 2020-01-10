#!/usr/bin/python3
import sys, serial
from GUIBrazo import *

class Formulario(Ui_MainWindow):
	first = None
	movementFrom = None
	movementTo = None
	INITIAL_LEFT_LABEL = None
	INITIAL_RIGHT_LABEL = None
	arduino = None
	
	def __init__(self, window):
		self.first = True;
		self.movementFrom = ""
		self.movementTo = ""
		#arduino = serial.Serial('', 9600) #DEFINIR PUERTO DE ARDUINO
		self.setupUi(window)
		self.INITIAL_LEFT_LABEL = self.labelL.text();
		self.INITIAL_RIGHT_LABEL = self.labelR.text();
		self.b0m1.clicked.connect(lambda: self.select("(0,-1)"))
		self.b00.clicked.connect(lambda: self.select("(0,0)"))
		self.b01.clicked.connect(lambda: self.select("(0,1)"))
		self.b1m1.clicked.connect(lambda: self.select("(1,-1)"))
		self.b10.clicked.connect(lambda: self.select("(1,0)"))
		self.b11.clicked.connect(lambda: self.select("(1,1)"))
		
		self.reset.clicked.connect(self.resetAction)
		self.commitOperation.setEnabled(False)
		self.commitOperation.clicked.connect(self.commitAction)

	def select(self, buttonText):
		if(self.first):
			self.labelL.setText(buttonText)
		else:
			self.labelR.setText(buttonText)
			
		self.first = not(self.first)
		
		if(self.labelL.text() == self.labelR.text() 
		  or self.labelL.text() == self.INITIAL_LEFT_LABEL 
		  or self.labelR.text() == self.INITIAL_RIGHT_LABEL):
			self.commitOperation.setEnabled(False)
		else:
			self.commitOperation.setEnabled(True)
		
	def resetAction(self):
		self.labelL.setText(self.INITIAL_LEFT_LABEL)
		self.labelR.setText(self.INITIAL_RIGHT_LABEL)
		self.movementFrom = ""
		self.movementTo = ""
		self.commitOperation.setEnabled(False)
		
	def commitAction(self):
		#SEND TO ARDUINO
		self.movementFrom = self.labelL.text()
		self.movementTo = self.labelR.text()
		whatToSend = self.movementFrom + ">" + self.movementTo;
		arduino = serial.Serial('/dev/ttyACM0', 9600)
		arduino.write(bytes(whatToSend, 'utf-8'))
		arduino.close()
		print(whatToSend)
		print("SENDED")
	
if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	
	myapp = Formulario(MainWindow)
	
	MainWindow.show()
	sys.exit(app.exec_())

