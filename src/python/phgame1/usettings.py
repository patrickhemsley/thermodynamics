
import include

class TSettings:

	def __init__(self):
			
		self.ball_quantity = 0
		self.containerxmin=0
		self.containerxmax=include.xmax
		self.containerymin=0
		self.containerymax=include.ymax
		self.step=1
		ans = raw_input("Enter type of container: 1) no dampening 2) 20% wall dampening 3) saucepan (default)")
		if ans == "1":
			print "DAMPEN_NONE"
			self.dampening = include.DAMPEN_NONE
		elif ans == "2":
			print "DAMPEN_20PCNT"
			self.dampening = include.DAMPEN_20PCNT
		else:
			print "DAMPEN_CONVECTION"
			self.dampening = include.DAMPEN_CONVECTION
			self.ball_quantity = 700
			self.containerymax=int(include.ymax*1/3)
			self.step = 1


		print "container ("+str(self.containerxmin)+", "+str(self.containerymin)+")..("+str(self.containerxmax)+", "+str(self.containerymax)+")"


		if self.ball_quantity == 0:
			self.ball_quantity = int("0"+raw_input ("How many balls? (default 100) "))
		if self.ball_quantity == 0:
			self.ball_quantity = 100

		ans = raw_input ("Gravity (y/n)? (default y) ")
		self.gravity = (ans == 'y') | (ans =='')
		if self.gravity:
			print("Gravity is ON")
		else:
			print("Gravity is OFF")
			



settings = TSettings()

