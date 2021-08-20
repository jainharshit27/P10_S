import pygame, pymunk
import pymunk.pygame_util

pygame.init()

height = 600
width = 300
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

#pymunk space
gravity = 100
wind = 0
space = pymunk.Space()
space.gravity = wind, gravity
draw_options = pymunk.pygame_util.DrawOptions(screen)

body1 = pymunk.Body(1,200)
shape1 = pymunk.Circle(body1, 25)
body1.position = 50, 0
space.add(body1, shape1)

body2 = pymunk.Body(10,50)
shape2 = pymunk.Circle(body2, 50)
body2.position = 150, 30
space.add(body2, shape2)

body3 = pymunk.Body(100,100)
shape3 = pymunk.Circle(body3, 5)
body3.position = 250, 20
space.add(body3, shape3)

while True:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    space.debug_draw(draw_options)
    pygame.display.update()
    
    #space reload
    space.step(1/60)
    clock.tick(60)