# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://programarcadegames.com/
# http://simpson.edu/computer-science/
 
# Explanation video: http://youtu.be/vRB_983kUMc
 
import pygame
import include 
import uball
import random
import uphysicsengine
import usettings



pygame.init()
  
# Set the width and height of the screen [width,height]
size=[include.xmax,include.ymax]
screen=pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
#Loop until the user clicks the close button.
done=False
 
# Used to manage how fast the screen updates
clock=pygame.time.Clock()

random.seed()


balls = []
xmin=usettings.settings.containerxmin
xmax=usettings.settings.containerxmax
ymin=usettings.settings.containerymin
ymax=usettings.settings.containerymax

for i in xrange(usettings.settings.ball_quantity):
	if usettings.settings.dampening == include.DAMPEN_CONVECTION: 
		if i > usettings.settings.ball_quantity-12:
			colour = include.red
		else:
			colour = include.lightblue
		ball  = uball.TBall("Ball"+str(i), colour,   
	          random.randint(0, xmax), random.randint(0, ymax), 10, random.randint(-1, 1), random.randint(-1, 1))
	else:
		ball  = uball.TBall("Ball"+str(i), include.colours[random.randint(0, 4)],   
	          random.randint(0, xmax), random.randint(0, ymax), random.randint(10, 40), random.randint(-10, 10), random.randint(-10, 10))
	balls.append(ball)
	uphysicsengine.engine.addobject(ball)


 
# -------- Main Program Loop -----------
iteration=0
while done==False:

    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
    # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
  
  
    # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
    uphysicsengine.engine.move()
    
 
    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
     
     
    # ALL CODE TO DRAW   
    iteration=iteration+1
    if iteration==usettings.settings.step:
		iteration=0
		# First, clear the screen to white. Don't put other drawing commands
		# above this, or they will be erased with this command.
		screen.fill(include.black)
		for i in xrange(usettings.settings.ball_quantity):
			balls[i].draw(screen)
		#print stats
		if (usettings.settings.dampening == include.DAMPEN_CONVECTION): 
			EastHeight = 0
			WestHeight = 0
			QtyEast = 0
			QtyWest = 0
			#for i in xrange(usettings.settings.ball_quantity):
			#	if balls[i].xspeed > 0:
			#		EastHeight=EastHeight + usettings.settings.containerymax-balls[i]._ypos
			#		QtyEast = QtyEast + 1
			#	else:
			#		WestHeight=WestHeight + usettings.settings.containerymax-balls[i]._ypos
			#		QtyWest = QtyWest + 1
			#print "Av Height: cooler={0}, hotter={1}, difference={2}".format(int(EastHeight/QtyEast), int(WestHeight/QtyWest), int((WestHeight/QtyWest)-(EastHeight/QtyEast)))
     
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 20 frames per second
    clock.tick(40)
     
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit ()

