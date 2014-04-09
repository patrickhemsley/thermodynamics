
ball_quantity = 100

# Define some colors
black    = (   0,   0,   0)
blue     = (   0,   0, 255)
lightblue= (   0, 255, 255)
green    = (   0, 255,   0)
white    = ( 255, 255, 255)
red      = ( 255,   0,   0)

colours=[blue, lightblue, green, white, red]

xmax=640
ymax=480


#gravitational acceleration
gravityx=0.0
gravityy=-6.67398 * 0.01

#how much energy is lost when colliding with wall
#0.0 for no loss, 1.0 for total loss
walldampenx=0.2
walldampeny=0.2
DAMPEN_NONE =1
DAMPEN_CONVECTION =2
DAMPEN_20PCNT = 3
