
import umomemtum
import include 
import usettings
import math


class TEngine:

    def __init__(self):
		self._objlist = []


    def addobject(self, obj):
		self._objlist.append(obj);

    def gravity(self, item):
		item.xspeed = item.xspeed - include.gravityx;
		item.yspeed = item.yspeed - include.gravityy;
		
		

			
    def move(self):
		for item in self._objlist:
			if usettings.settings.gravity:
				self.gravity(item);
			item.move();
		for index1, item1 in enumerate(self._objlist):
			for index2, item2 in enumerate(self._objlist):
				if index2>index1:
					if item1.collide(item2):
						newstate = umomemtum.apply_elastic_collision(item1, item2)
						item1.move();
						item2.move();

    def dampen(self, wall, obj):
		if (wall == "EAST") | (wall == "WEST"):
			speed = obj.xspeed
		else:
			speed = obj.yspeed
		relativeenergybefore = speed * speed

		if usettings.settings.dampening == include.DAMPEN_CONVECTION: 
			#SOUTH wall is hot to the EAST and cold to the WEST
			#NORTH wall is cold
			if wall == "SOUTH":
				multiplier = (obj._xpos / include.xmax) #0..1
				multiplier = multiplier * 2 + 0.5 #0.5..2.5
				energyafter = relativeenergybefore * multiplier
				#energyafter = relativeenergybefore * 4.0
			elif wall == "NORTH":
				energyafter = relativeenergybefore * 0.5
			elif wall == "EAST":
				energyafter = relativeenergybefore * 2
			elif wall == "WEST":
				energyafter = relativeenergybefore 
			else:
				energyafter = relativeenergybefore
		elif usettings.settings.dampening == include.DAMPEN_20PCNT:
			energyafter = relativeenergybefore * 0.8
		elif usettings.settings.dampening == include.DAMPEN_NONE:
			energyafter = relativeenergybefore 
			
		newspeed = math.sqrt(energyafter)
		if speed > 0:
			multiplier = -1
		else:
			multiplier = 1
	
		if (wall == "EAST") | (wall == "WEST"):
			obj.xspeed = newspeed * multiplier
		else:
			obj.yspeed = newspeed * multiplier


engine = TEngine()
