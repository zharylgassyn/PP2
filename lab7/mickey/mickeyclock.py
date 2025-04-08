import pygame
import datetime

pygame.init()


SCREEN_WIDTH, SCREEN_HEIGHT = 1440, 1080
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Clock")
clock = pygame.time.Clock()


bg = pygame.image.load("lab_7/mickey/clock.jpg")
second_hand = pygame.image.load("lab_7/mickey/sec.png")
minute_hand = pygame.image.load("lab_7/mickey/min.png")


def blit_rotate(image, pos, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=pos)
    screen.blit(rotated_image, new_rect.topleft)


running = True
while running:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT or \
            (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    now = datetime.datetime.now()

    second_angle = -now.second * 6 - 225
    minute_angle = -(now.minute + now.second / 60) * 6 - 45 


    center_pos = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    screen.blit(bg, (0, 0))
    blit_rotate(second_hand, center_pos, second_angle)
    blit_rotate(minute_hand, center_pos, minute_angle) 
    pygame.draw.circle(screen, (232, 34, 51), center_pos, 20)

    pygame.display.flip()

pygame.quit()