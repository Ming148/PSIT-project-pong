"""pong"""
import pygame
import sys
import random

from pygame.constants import MOUSEBUTTONDOWN

# set up
pygame.init()
font_l = pygame.font.Font('depixelhalbfett.ttf', 35)
font_s = pygame.font.Font('depixelhalbfett.ttf', 20)
clock = pygame.time.Clock()
click = False
key_arrow = pygame.image.load('key_arrow.png')
key_wasd = pygame.image.load('key_wasd.png')

# หน้าต่างเกมหลัก
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

# Game object
## pygame.Rect(ตำแหน่ง_x, ตำแหน่ง_y, ขนาด_ก, ขนาด_ย)
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player_1 = pygame.Rect(10, screen_height/2 - 70, 10, 140)
player_2 = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)

# color
bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)
red = (240, 84, 84)
blue = (84, 84, 240)

# menu

def draw_text(text, font, color, surface, x, y):
    """draw text"""
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def main_manu():
    """main manu"""
    while True:
        screen.fill((bg_color))
        draw_text("Pingpond and PongPheun", font_l,
                  (255, 255, 255), screen, 320, 220)
        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(540, 350, 200, 50)
        button_2 = pygame.Rect(540, 450, 200, 50)
        button_3 = pygame.Rect(540, 550, 200, 50)
        button_4 = pygame.Rect(540, 650, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                one_player()
        if button_2.collidepoint((mx, my)):
            if click:
                two_player()
        if button_3.collidepoint((mx, my)):
            if click:
                how_to_play()
        if button_4.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()
        click = False
        pygame.draw.rect(screen, red, button_1)
        pygame.draw.rect(screen, red, button_2)
        pygame.draw.rect(screen, red, button_3)
        pygame.draw.rect(screen, red, button_4)
        draw_text("1 Player", font_s, (255, 255, 255), screen, 585, 362)
        draw_text("2 Player", font_s, (255, 255, 255), screen, 585, 462)
        draw_text("How to play", font_s, (255, 255, 255), screen, 558, 562)
        draw_text("Exit", font_s, (255, 255, 255), screen, 615, 662)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        # updating display
        pygame.display.update()

def how_to_play():
    """how_to_play"""
    while True:
        mx, my = pygame.mouse.get_pos()
        screen.fill(bg_color)
        screen.blit(key_arrow, (170, 350))
        screen.blit(key_arrow, (860, 350))
        screen.blit(key_wasd, (580, 339))

        button = pygame.Rect(540, 800, 200, 50)
        if button.collidepoint((mx, my)):
            if click:
                main_manu()
        click = False
        pygame.draw.rect(screen, red, button)
        draw_text("How to play", font_l, (255, 255, 255), screen, 490, 120)
        draw_text("Control paddle :", font_s,
                  (255, 255, 255), screen, 170, 210)
        draw_text("1 player", font_s, blue, screen, 237, 310)
        draw_text("2 player", font_s, red, screen, 800, 310)
        draw_text("Press \"P\" to pause", font_s,
                  (255, 255, 255), screen, 517, 580)
        draw_text("Press \"C\" to continue", font_s,
                  (255, 255, 255), screen, 495, 650)
        draw_text("Press \"Q\" to exit", font_s,
                  (255, 255, 255), screen, 528, 720)
        draw_text("Main menu", font_s, (255, 255, 255), screen, 562, 812)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()

def pause():
    """pause"""
    paused = True
    while paused:
        screen.fill(bg_color)
        draw_text("Pause", font_l, (255, 255, 255), screen, 565, 220)
        draw_text("Press \"C\" to continue", font_s,
                  (255, 255, 255), screen, 495, 320)
        draw_text("Press \"Q\" to exit", font_s,
                  (255, 255, 255), screen, 528, 420)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        pygame.display.update()

# base game
def player_1animation():
    """player 1 animetion"""
    player_1.y += player_1speed
    if player_1.top <= 0:
        player_1.top = 0
    if player_1.bottom >= screen_height:
        player_1.bottom = screen_height

def player_2animation():
    """player 2 animetion"""
    player_2.y += player_2speed
    if player_2.top <= 0:
        player_2.top = 0
    if player_2.bottom >= screen_height:
        player_2.bottom = screen_height

def ballanimation():  # ลูดบอล
    """ballanimetion"""
    global ball_speed_x, ball_speed_y, player_score_1, player_score_2, score_time

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        pygame.mixer.Sound.play(pong_sound)
        ball_speed_y *= -1

    if ball.left <= 0:
        pygame.mixer.Sound.play(score_sound)
        player_score_1 += 1
        score_time = pygame.time.get_ticks()

    if ball.right >= screen_width:
        pygame.mixer.Sound.play(score_sound)
        player_score_2 += 1
        score_time = pygame.time.get_ticks()

    # ลูกบอลโดนไม้
    if ball.colliderect(player_2) and ball_speed_x > 0:
        pygame.mixer.Sound.play(pong_sound)
        if abs(ball.right - player_2.left) < 10:
            ball_speed_x *= -1
        elif abs(ball.bottom - player_2.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - player_2.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1

    if ball.colliderect(player_1) and ball_speed_x < 0:
        pygame.mixer.Sound.play(pong_sound)
        if abs(ball.left - player_1.right) < 10:
            ball_speed_x *= -1
        elif abs(ball.bottom - player_1.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - player_1.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1

def opponentanimation_1():  # bot
    """opponentanimation_1"""
    if player_1.top < ball.y:
        player_1.top += bot_speed
    if player_1.bottom > ball.y:
        player_1.bottom -= bot_speed
    if player_1.top <= 0:
        player_1.top = 0
    if player_1.bottom >= screen_height:
        player_1.bottom = screen_height

def ball_restart():
    """ball restart"""
    global ball_speed_x, ball_speed_y, ball_moving, score_time

    ball.center = (screen_width/2, screen_height/2)
    current_time = pygame.time.get_ticks()

    if current_time - score_time < 700:
        number_three = game_font.render("3", False, light_grey)
        screen.blit(number_three, (screen_width/2 - 10, screen_height/2 + 20))
    if 700 < current_time - score_time < 1400:
        number_two = game_font.render("2", False, light_grey)
        screen.blit(number_two, (screen_width/2 - 10, screen_height/2 + 20))
    if 1400 < current_time - score_time < 2100:
        number_one = game_font.render("1", False, light_grey)
        screen.blit(number_one, (screen_width/2 - 10, screen_height/2 + 20))

    if current_time - score_time < 2100:
        ball_speed_y, ball_speed_x = 0, 0
    else:
        randomball = [1, -1]
        ball_speed_x = 7 * random.choice(randomball)
        ball_speed_y = 7 * random.choice(randomball)
        score_time = None

# ball
randomball = [1, -1]
ball_speed_x = 7 * random.choice(randomball)
ball_speed_y = 7 * random.choice(randomball)
player_1speed = 0
player_2speed = 0
bot_speed = 7
ball_moving = False

# Text variables
player_score_1 = 0
player_score_2 = 0
max_score = 11
game_font = pygame.font.Font('freesansbold.ttf', 32)

# Score timer
score_time = True

# Sound
#pong_sound = pygame.mixer.Sound("paddle.ogg")
score_sound = pygame.mixer.Sound("score.ogg")
pong_sound = pygame.mixer.Sound("pong.ogg")

def gameOver():
    if player_score_1 == max_score or player_score_2 == max_score:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_r:
                        ball_restart()
            if player_score_1 == max_score:
                draw_text("You Wins!", font_s, (0, 0, 255), screen, 920, 420)
            elif player_score_2 == max_score:
                draw_text("You Wins!", font_s, (255, 0, 0), screen, 220, 420)
            
            pygame.display.update()

def one_player():
    """one_player"""
    global player_1speed, player_2speed
    running = True
    while running:
        # input
        for event in pygame.event.get():
            # ถ้ามีการกดที่ปุ่ม QUIT ให้ออกเกม
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause()
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

        # ball
        ballanimation()
        player_2animation()

        # bot
        opponentanimation_1()
        # color
        screen.fill(bg_color)
        pygame.draw.rect(screen, red, player_1)
        pygame.draw.rect(screen, blue, player_2)
        pygame.draw.ellipse(screen, light_grey, ball)
        pygame.draw.aaline(screen, light_grey, (screen_width/2,
                           0), (screen_width/2, screen_height))

        if score_time:
            ball_restart()

        player_text_1 = game_font.render(
            f"{player_score_1}", False, light_grey)
        screen.blit(player_text_1, (660, 470))

        player_text_2 = game_font.render(
            f"{player_score_2}", False, light_grey)
        screen.blit(player_text_2, (600, 470))

        # updating display
        pygame.display.flip()
        clock.tick(60)
        gameOver()

def two_player():
    """two player"""
    global player_1speed, player_2speed
    running = True
    while running:
        # input
        for event in pygame.event.get():
            # ถ้ามีการกดที่ปุ่ม QUIT ให้ออกเกม
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause()
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
        player_1animation()
        player_2animation()

        # color
        screen.fill(bg_color)
        pygame.draw.rect(screen, red, player_1)
        pygame.draw.rect(screen, blue, player_2)
        pygame.draw.ellipse(screen, light_grey, ball)
        pygame.draw.aaline(screen, light_grey, (screen_width/2,
                           0), (screen_width/2, screen_height))

        if score_time:
            ball_restart()

        player_text_1 = game_font.render(
            f"{player_score_1}", False, light_grey)
        screen.blit(player_text_1, (660, 470))

        player_text_2 = game_font.render(
            f"{player_score_2}", False, light_grey)
        screen.blit(player_text_2, (600, 470))

        # updating display
        pygame.display.flip()
        clock.tick(60)
        gameOver()

main_manu()
