import pygame
import os


MUSIC_PATH = "./lab_7/music/songs"
TRACKS = sorted(os.listdir(MUSIC_PATH))

pygame.init()
screen = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Music Player")

font_main = pygame.font.Font('freesansbold.ttf', 20)
font_small = pygame.font.Font('freesansbold.ttf', 15)

play_icon = pygame.transform.scale(pygame.image.load('./lab_7/music/play.png'), (70, 70))
pause_icon = pygame.transform.scale(pygame.image.load('./lab_7/music/pause.png'), (70, 70))

current_track = 0
playing = False
clock = pygame.time.Clock()


def play_track():
    pygame.mixer.music.load(os.path.join(MUSIC_PATH, TRACKS[current_track]))
    pygame.mixer.music.play()
    

def toggle_play_pause():
    global playing
    playing = not playing
    if playing:
        play_track()
    else:
        pygame.mixer.music.pause()


def draw_screen():
    screen.fill((240, 240, 240))
    
    track_text = font_main.render(TRACKS[current_track], True, (50, 50, 50))
    screen.blit(track_text, (250 - track_text.get_width() // 2, 100))
    
    icon = pause_icon if playing else play_icon
    screen.blit(icon, (250 - icon.get_width()//2, 150))
    
    pygame.display.flip()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                toggle_play_pause()
            elif event.key == pygame.K_RIGHT:
                current_track = (current_track + 1) % len(TRACKS)
                play_track()
                playing = True
            elif event.key == pygame.K_LEFT:
                current_track = (current_track - 1) % len(TRACKS)
                play_track()
                playing = True
    
    draw_screen()
    clock.tick(30)

pygame.quit()