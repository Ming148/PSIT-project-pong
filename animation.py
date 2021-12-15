"""pong"""
import pygame, sys

# setup
pygame.init()
clock = pygame.time.Clock()

# หน้าต่างเกมหลัก
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

# Game object
## pygame.Rect(ตำแหน่ง_ก, ตำแหน่ง_ย, ขนาด_ก, ขนาด_ย)
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player_1 = pygame.Rect(10, screen_height/2 - 70, 10, 140)
player_2 = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)

## ball
ball_speed_x = 7
ball_speed_y = 7

## color
bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)
red = (255, 0, 0)
blue = (0, 0, 255)

while True:
    # input
    for event in pygame.event.get():
        # ถ้ามีการกดที่ปุ่ม QUIT ให้ออกเกม
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1

    # color
    screen.fill(bg_color)
    pygame.draw.rect(screen, red, player_1)
    pygame.draw.rect(screen, blue, player_2)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2, 0), (screen_width/2, screen_height))

    # updating display
    pygame.display.flip()
    clock.tick(60)
