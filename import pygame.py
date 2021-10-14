import pygame
pygame.init()
screen = pygame.display.set_mode((1000, 1000))
done = False
x=60
y=60
x_1 = 0
y_1 = 0
width = 40
height = 60
vel = 0.5
while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= vel
        if keys[pygame.K_RIGHT]:
            x += vel
        if keys[pygame.K_UP]:
            y -= vel
        if keys[pygame.K_DOWN]:
            y += vel
        x_1 += 0.2
        y_1 += 0.2
        screen.fill((0,0,0))
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(x, y, width, height))
        pygame.draw.circle(screen, (255,255,255), (x_1,y_1),40,10)
        pygame.display.flip()
pygame.quit()