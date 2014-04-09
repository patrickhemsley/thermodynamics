


class TCollisionDim:

	def __init__(self, dimension, obj1, obj2):
		if dimension == "x":
			self.u1 = obj1.xspeed;
			self.u2 = obj2.xspeed;
			self.v1 = 0.0;
			self.v2 = 0.0;
			self.m1 = obj1.mass;
			self.m2 = obj2.mass;
		elif dimension == "y":
			self.u1 = obj1.yspeed;
			self.u2 = obj2.yspeed;
			self.v1 = 0.0;
			self.v2 = 0.0;
			self.m1 = obj1.mass;
			self.m2 = obj2.mass;

	def collide(self):
		initialenergyx=(self.m1*self.u1*self.u1 + self.m2*self.u2*self.u2)/2;
		self.v1 = (self.u1 * (self.m1-self.m2) + 2*self.m2*self.u2)  / (self.m1+self.m2);
		self.v2 = (self.u2 * (self.m2-self.m1) + 2*self.m1*self.u1)  / (self.m1+self.m2);
		finalenergyx=(self.m1*self.v1*self.v1 + self.m2*self.v2*self.v2)/2;



def apply_elastic_collision(obj1, obj2):	
	#print "collision of {0} with {1}:".format(obj1.objname, obj2.objname) 
		
	c  = TCollisionDim("x", obj1, obj2)
	c.collide()
	obj1.xspeed = c.v1 
	obj2.xspeed = c.v2 

	c  = TCollisionDim("y", obj1, obj2)
	c.collide()
	obj1.yspeed = c.v1 
	obj2.yspeed = c.v2 


