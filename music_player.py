import pygame

pygame.init()
song = pygame.mixer.music.load('illuminati.mp3')
pygame.mixer.music.play()

# Keep the program running while music plays
while pygame.mixer.music.get_busy():
  pygame.time.Clock().tick(10)
