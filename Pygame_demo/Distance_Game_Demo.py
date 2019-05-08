import pygame, sys

#math import
import math

pygame.init()

#vars
FPS = 30 #refresh rate
fps_clock = pygame.time.Clock()
circle_x = 500
circle_y = 500
#Keys used
a = False
s = False
w = False
d = False

UP = False
DOWN = False
LEFT = False
RIGHT = False

#Colors here
BLACK = (0, 0, 0)
GREEN = (0,192,44)

#set up window
screen = pygame.display.set_mode((1000, 700))#Width 1000px #Height 700px
pygame.display.set_caption('Collect the Stars')

#Background Image.  (Cant open)
img = pygame.image.load('space_2.png')
img_x = 0 #whatever x-coordinate you want it to start at
img_y = 0 #whatever y-coordinate you want it to start at

#Main Star
img_2 = pygame.image.load("star_2.png")
img_x_2 = 50
img_y_2 = 50

#new
star_center = [100, 100]

img = pygame.transform.scale(img, (1000, 700))
img_2 = pygame.transform.scale(img_2, (100, 100))
#print(img)

#Other Stars
img_3 = pygame.image.load("star_2.png")
img_x_3 = 300
img_y_3 = 500

img_3 = pygame.transform.scale(img_3, (100, 100))


img_4 = pygame.image.load("star_2.png")
img_x_4 = 700
img_y_4 = 400

img_4 = pygame.transform.scale(img_4, (100, 100))


img_5 = pygame.image.load("star_2.png")
img_x_5 = 100
img_y_5 = 400

img_5 = pygame.transform.scale(img_5, (100, 100))


img_6 = pygame.image.load("star_2.png")
img_x_6 = 300
img_y_6 = 500

img_6 = pygame.transform.scale(img_6, (100, 100))


img_7 = pygame.image.load("star_2.png")
img_x_7 = 700
img_y_7 = 100

img_7 = pygame.transform.scale(img_7, (100, 100))


img_8 = pygame.image.load("star_2.png")
img_x_8 = 450
img_y_8 = 150

img_8 = pygame.transform.scale(img_8, (100, 100))


img_9 = pygame.image.load("star_2.png")
img_x_9 = 550
img_y_9 = 550

img_9 = pygame.transform.scale(img_9, (100, 100))

#circle
def draw_circle(x, y):
	pygame.draw.circle(screen, GREEN, (x, y), 50)
	return pygame.Rect(x-50, y-50, 100, 100)

#plan: Collect stars from space, some may be explosive

#distance function
def distance(point1, point2):
    number = (point2[1] - point1[1]) **2 + (point2[0] - point1[0]) **2
    result = math.sqrt(number)
    return result

dead = False

#Game loop
while True:
	#sets the background color to black
	screen.fill(BLACK)
	
	#draw stuff here


	#loads image
	screen.blit(img, (img_x, img_y))
	
	#stars
	screen.blit(img_2, (img_x_2, img_y_2))

	screen.blit(img_3, (img_x_3, img_y_3))
	
	screen.blit(img_4, (img_x_4, img_y_4))
	
	screen.blit(img_5, (img_x_5, img_y_5))
	
	screen.blit(img_6, (img_x_6, img_y_6))
	
	screen.blit(img_7, (img_x_7, img_y_7))
	
	screen.blit(img_8, (img_x_8, img_y_8))
	
	screen.blit(img_9, (img_x_9, img_y_9))
	
	#set-up rects for collision detection
	top_wall = pygame.Rect(0,0, 1000, 1)
	bottom_wall = pygame.Rect(0,700, 1000, 1)
	left_wall = pygame.Rect(0, 0, 1, 700)
	right_wall = pygame.Rect(1000, 0, 1, 700) 
	
	circle_center = [circle_x, circle_y]
	
	circle_x = circle_x - 0

	print(distance(star_center, circle_center))
	d = distance(star_center, circle_center)
	#draws player
	
	if d < 75:
		dead = True
	
	if not dead:
		circle_rect = draw_circle(circle_x, circle_y)
	
	#new
	

	#Keys wasd
	keystate = pygame.key.get_pressed()
	if keystate[pygame.K_a]:
		if not circle_rect.colliderect(left_wall):
			circle_x = circle_x - 4
	if keystate[pygame.K_s]:
		if not circle_rect.colliderect(bottom_wall):
			circle_y = circle_y + 4
	if keystate[pygame.K_w]:
		if not circle_rect.colliderect(top_wall):
			circle_y = circle_y - 4
	if keystate[pygame.K_d]:
		if not circle_rect.colliderect(right_wall):
			circle_x = circle_x + 4
	
	#Event
	if dead == True:
		pygame.quit()
		sys.exit()
		
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	
	pygame.display.update()
	fps_clock.tick(FPS)	
	

