"""set up"""
import pygame, sys

# setup
pygame.init()

# หน้าต่างเกมหลัก
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

# Game object
# pygame.Rect(ตำแหน่ง_ก, ตำแหน่ง_ย, ขนาด_ก, ขนาด_ย)
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player_1 = pygame.Rect(10, screen_height/2 - 70, 10, 140)
player_2 = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)

while True:
    # input
    for event in pygame.event.get():
        # ถ้ามีการกดที่ปุ่ม QUIT ให้ออกเกม
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
