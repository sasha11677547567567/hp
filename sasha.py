import pygame
pygame.init()
import random

window = pygame.display.set_mode((500,500))
back_color =(255,225,0)
game = True
clock = pygame.time.Clock()
player1 = pygame.Rect(100,100,50,50)
bullets = []
bullets2 = []
while game:

    
    window.fill(back_color)
    pygame.draw.rect(window,(0,0,255),player1)
    for even in pygame.event.get():
        if even. type  == pygame.QUIT:
            game = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player1.x -= 3
    if keys[pygame.K_s]:
        player1.y += 3
    if keys[pygame.K_w]:
        player1.y -= 3
    if keys[pygame.K_d]:
        player1.x += 3

    if  random.randint(0,200) < 10:
        x = random.randint(0,480)
        y = -10
        bullets.append(pygame.Rect(x,y,20,20))


    for b in bullets:
        pygame.draw.rect(window,(0,0,0),b)

    for b in bullets:
        b.y += 10
        if b.colliderect(player1):
            game = False
    
    if  random.randint(0,200) < 10:
        x = -10
        y = random.randint(0,480)
        bullets2.append(pygame.Rect(x,y,20,20))


    for b in bullets2:
        pygame.draw.rect(window,(0,0,0),b)

    for b in bullets2:
        b.x += 10
        if b.colliderect(player1):
            game = False

    pygame.display.update()
    clock.tick(30)









