import pygame
import include 
import umomemtum
import math
import uphysicsengine
import usettings


class TBall:

	def __init__(self, objname, colour=include.black, xpos=100, ypos=100, size=100, xspeed_=0.0, yspeed_=0.0):
		self.objname = objname
		self._colour = colour
		self._xpos = xpos
		self._ypos = ypos
		self._size = size
		self.xspeed = 0.0+xspeed_
		self.yspeed = 0.0+yspeed_
		self._radius = size/2
		self.mass = size*size
		_speed=math.sqrt(xspeed_*xspeed_ + yspeed_*yspeed_)
		#print "{0} has size {1}, speed {2:.3f}.".format(self.objname, _speed, size)


	
	def draw(self, scr):
		if (usettings.settings.dampening <> include.DAMPEN_CONVECTION):
			pygame.draw.circle(scr, self._colour, (int(self._xpos), int(self._ypos)), int(self._size*0.55))
		elif (self._colour <> include.red):
			pygame.draw.circle(scr, include.green, (int(self._xpos), int(self._ypos)), 5)
		elif self.yspeed > 0:
			pygame.draw.circle(scr, include.red, (int(self._xpos), int(self._ypos)), 5)
		else:
			pygame.draw.circle(scr, include.red, (int(self._xpos), int(self._ypos)), 5)

	def move(self):
		xmax=usettings.settings.containerxmax
		ymax=usettings.settings.containerymax

		self._xpos = self._xpos + self.xspeed
		if self._xpos+self._radius > xmax:
			self._xpos = xmax-self._radius
			uphysicsengine.engine.dampen("EAST", self)
		elif self._xpos < self._radius:
			self._xpos = self._radius
			uphysicsengine.engine.dampen("WEST", self)

		self._ypos = self._ypos + self.yspeed
		if self._ypos > ymax-self._radius:
			self._ypos = ymax-self._radius
			uphysicsengine.engine.dampen("SOUTH", self)
		elif self._ypos < self._radius:
			self._ypos = self._radius
			uphysicsengine.engine.dampen("NORTH", self)
		
		if usettings.settings.dampening == include.DAMPEN_CONVECTION: 
			self.xspeed = self.xspeed * 0.999
			self.yspeed = self.yspeed * 0.999

	
	def collide(self, ball):
		dx = (self._xpos - ball._xpos)
		dy = (self._ypos - ball._ypos)
		d = math.sqrt(dx*dx + dy*dy)
		return d <= self._radius + ball._radius
