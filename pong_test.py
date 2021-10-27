"""pong"""
import pygame, sys, random

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

## color
bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)
red = (255, 0, 0)
blue = (0, 0, 255)
def player_2animation():
    player_2.y += player_2speed
    if player_2.top <= 0:
        player_2.top = 0
    if player_2.bottom >= screen_height:
        player_2.bottom = screen_height
def player_1animation():
    player_1.y += player_1speed
    if player_1.top <= 0:
        player_1.top = 0
    if player_1.bottom >= screen_height:
        player_1.bottom = screen_height
def ballanimation(): #ลูดบอล
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_restart()
    if ball.colliderect(player_1) or ball.colliderect(player_2):
        ball_speed_x *= -1
def opponentanimation_1(): #bot
    if player_1.top < ball.y:
        player_1.top += bot_speed
    if player_1.bottom > ball.y:
        player_1.bottom -= bot_speed
    if player_1.top <= 0:
        player_1.top = 0
    if player_1.bottom >= screen_height:
        player_1.bottom = screen_height
def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width / 2, screen_height / 2)
    ball_speed_y *= random.choice(randomball)
    ball_speed_x *= random.choice(randomball)
## ball
randomball = [1, -1]
ball_speed_x = 7 * random.choice(randomball)
ball_speed_y = 7 * random.choice(randomball)
player_1speed = 0
player_2speed = 0
bot_speed = 7

while True:
    # input
    for event in pygame.event.get():
        # ถ้ามีการกดที่ปุ่ม QUIT ให้ออกเกม
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_2speed += 7
            if event.key == pygame.K_UP:
                player_2speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_2speed -= 7
            if event.key == pygame.K_UP:
                player_2speed += 7
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                player_1speed += 7
            if event.key == pygame.K_w:
                player_1speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                player_1speed -= 7
            if event.key == pygame.K_w:
                player_1speed += 7
    # ball
    ballanimation()
    player_2animation()
    #player_1animation()
    opponentanimation_1()

    # color
    screen.fill(bg_color)
    pygame.draw.rect(screen, red, player_1)
    pygame.draw.rect(screen, blue, player_2)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2, 0), (screen_width/2, screen_height))

    # updating display
    pygame.display.flip()
    clock.tick(60)
