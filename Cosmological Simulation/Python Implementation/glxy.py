'''
NOTE:
For the python implementation of the algorithm the program works but it doesn't take into
account elastic collision meaning if the particles are too close the particles manage to achieve 
infinite velocity.
simply add to the program yourself in the check body to see whether the distance between objects
is less that the sum of their radii.
If it is combine the two objects into one to prevent them reaching infinite velocity.
Have Fun!
'''

import time
import pygame
from particle import Particle
import random
import math as Math

pygame.init()

# Presets for solar system according to Hermann Bjorgvins 2d
# var star = spacetime.addObject({
# 				cameraFocus: true,
# 				x: 200,
# 				y: 200,
# 				velX: 0,
# 				velY: 0,
# 				deltaVelX: 0,
# 				deltaVelY: 0,
# 				mass: 500,
# 				density: 0.3,
# 				path: []
# 			});
# 			var mercury = spacetime.addObject({
# 				x: 230,
# 				y: 200,
# 				velX: 0,
# 				velY: Math.sqrt(500/30),
# 				deltaVelX: 0,
# 				deltaVelY: 0,
# 				mass: 0.5,
# 				density: 1,
# 				path: []
# 			});
# 			var mars = spacetime.addObject({
# 				x: 0,
# 				y: 200,
# 				velX: 0,
# 				velY: -Math.sqrt(500/200),
# 				deltaVelX: 0,
# 				deltaVelY: 0,
# 				mass: 3,
# 				density: 1,
# 				path: []
# 			});
# 			var earth = spacetime.addObject({
# 				x: 550,
# 				y: 200,
# 				velX: 0,
# 				velY: Math.sqrt(500/350),
# 				deltaVelX: 0,
# 				deltaVelY: 0,
# 				mass: 6,
# 				density: 0.6,
# 				path: []
# 			});
# 			var moon = spacetime.addObject({
# 				x: 570,
# 				y: 200,
# 				velX: 0,
# 				velY: Math.sqrt(500/350) + Math.sqrt(6/20),
# 				deltaVelX: 0,
# 				deltaVelY: 0,
# 				mass: 0.1,
# 				density: 1,
# 				path: []
# 			});

#Presets for a black-hole
# // var starmass = 10000;
# 		/*var blackhole = spacetime.addObject({
# 			x: 0,
# 			y: 0,
# 			velX: 0,
# 			velY: 0,
# 			deltaVelX: 0,
# 			deltaVelY: 0,
# 			mass: starmass,
# 			density: 0.0001,
# 			path: []
# 		});*/


BODIES = 100
WIDTH, HEIGHT = 1000, 1000
white = pygame.Color(255, 255, 255)
blue = pygame.Color(0, 0, 255)
pygame_circles = []
camera_focus = 0.1
n_bodies = []


#n_bodies.append(Particle(x=450, y=250, vX=0, vY=0, mass=500, density=0.3))
#n_bodies.append(Particle(x=480, y=250, vX=0, vY=Math.sqrt(500/30), mass=0.1, density=1))
#n_bodies.append(Particle(x=420, y=250, vX=0, vY=-Math.sqrt(500/200), mass=3, density=1))
#n_bodies.append(Particle(x=550, y=250, vX=0, vY=Math.sqrt(500/350), mass=6, density=0.6))
#n_bodies.append(Particle(x=570, y=250, vX=0, vY=Math.sqrt(500/350) + Math.sqrt(6/20), mass=0.1, density=1))
#n_bodies.append(Particle(random.randint(400, 500), random.randint(200, 300), random.randint(5, 10), 0, 0))


for i in range(BODIES):
    n_bodies.append(Particle(random.randint(0 + 200, WIDTH//2), random.randint(0 + 200, HEIGHT//2),  0, 0, mass=random.randint(50, 100), density=10))

win = pygame.display.set_mode((WIDTH, HEIGHT))

run = True

def draw():
    for i in range(len(n_bodies)):
        for j in range(1, len(n_bodies), 1):
            if i == j:
                continue

            other = n_bodies[j]
            x, y = n_bodies[i]._main(other=other)
            mass = n_bodies[i].mass

            if mass > 100:
                pygame.draw.circle(win, white, (x, y), mass * 0.01)
            elif mass < 1:
                pygame.draw.circle(win, white, (x, y), mass )
            else:
                pygame.draw.circle(win, white, (x, y), mass * camera_focus)



while run:

    win.fill((0, 0, 0))
    draw()
    pygame.display.flip()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
