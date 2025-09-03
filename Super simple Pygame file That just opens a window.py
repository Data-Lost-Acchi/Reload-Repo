import pygame

pygame.init()

height =  720
width = 1000


screen = pygame.display.set_mode((width,height))
run = True
while run == True:

    for event  in pygame.event.get():
        if event.type == pygame.QUIT:
            run =  False
