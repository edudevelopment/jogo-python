import pygame

print('Starting game...')
pygame.init()
screen = pygame.display.set_mode(size = (600, 480))

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      print('Closing game...') 
     
     
      