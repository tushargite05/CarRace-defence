import pygame

pygame.init()

screen=pygame.display.set_mode((400,300))
done=False


x=30
y=30

clock=pygame.time.Clock()

while not done:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            print("Space has been pressed")

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -=3
    if pressed[pygame.K_DOWN]: y +=3
    if pressed[pygame.K_LEFT]: x -=3
    if pressed[pygame.K_RIGHT]: x +=3

    screen.fill((0,0,0))
    pygame.draw.rect(screen, (0,128,0), pygame.Rect(x,y,60,60))
    pygame.display.flip()

    clock.tick(60)






import pygame
pygame.init()
screen=pygame.display.set_mode((400,300))


done=False

clock=pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
            
        screen.fill((255,255,255))
        screen.blit(pygame.image.load('circle.png'),(20,20))

        pygame.display.flip()
        clock.tick(60)