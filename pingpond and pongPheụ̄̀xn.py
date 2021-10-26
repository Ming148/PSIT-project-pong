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

def ballanimation(): #ลูกบอล
    global ball_speed_x, ball_speed_y, player_score_1, player_score_2, score_time
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    if ball.top <= 0 or ball.bottom >= screen_height: #ถ้าบอลแตะขอบบนหรือล่างจะกลับด้าน
        ball_speed_y *= -1
    
    if ball.right >= screen_width: #นับคะแนน
        player_score_2 += 1
        score_time = pygame.time.get_ticks()
    
    if ball.left <= 0: #นับคะแนน
        player_score_1 += 1
        score_time = pygame.time.get_ticks()
    
    if ball.colliderect(player_1) or ball.colliderect(player_2):
        ball_speed_x *= -1
        if ball_speed_x < 0:
            ball_speed_x -= 1
        elif ball_speed_x > 0:
            ball_speed_x += 1

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
    global ball_speed_x, ball_speed_y, score_time

    ball.center = (screen_width/2, screen_height/2)
    current_time = pygame.time.get_ticks()

    if current_time - score_time < 700:
        number_three = game_font.render("3",False,light_grey)
        screen.blit(number_three,(screen_width/2 - 10, screen_height/2 + 20))
    if 700 < current_time - score_time < 1400:
        number_two = game_font.render("2",False,light_grey)
        screen.blit(number_two,(screen_width/2 - 10, screen_height/2 + 20))
    if 1400 < current_time - score_time < 2100:
        number_one = game_font.render("1",False,light_grey)
        screen.blit(number_one,(screen_width/2 - 10, screen_height/2 + 20))
    
    if current_time - score_time < 2100:
        ball_speed_y, ball_speed_x = 0,0
    else:
        randomball = [1, -1]
        randomspeedball_y = [3, 4, 5, 6, 7]
        ball_speed_x = 7 * random.choice(randomball)
        ball_speed_y = random.choice(randomspeedball_y) * random.choice(randomball)
        score_time = None

## ball
randomball = [1, -1]
randomspeedball_y = [3, 4, 5, 6, 7]
ball_speed_x = 7 * random.choice(randomball)
ball_speed_y = random.choice(randomspeedball_y) * random.choice(randomball)
player_1speed = 0
player_2speed = 0
bot_speed = 15

# Text variables
player_score_1 = 0
player_score_2 = 0
game_font = pygame.font.Font('freesansbold.ttf', 32)

# Score timer
score_time = True

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
    player_1animation()
    #opponentanimation_1()

    # color
    screen.fill(bg_color)
    pygame.draw.rect(screen, red, player_1)
    pygame.draw.rect(screen, blue, player_2)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2, 0), (screen_width/2, screen_height))

    if score_time:
        ball_restart()

    player_text_1 = game_font.render(f"{player_score_1}", False, light_grey)
    screen.blit(player_text_1,(660,470))

    player_text_2 = game_font.render(f"{player_score_2}", False, light_grey)
    screen.blit(player_text_2,(600,470))

    # updating display
    pygame.display.flip()
    clock.tick(60)
