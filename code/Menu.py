import pygame

from pygame import Surface, Rect
from pygame.font import Font
from code.Const import COLOR_WHITE, MENU_OPTION, WIN_WIDTH , MENU_MUSIC, WIN_WIDTH, COLOR_ORANGE, COLOR_PURPLE

class Menu:
    def __init__(self, window): 
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png')
        self.rect = self.surf.get_rect(left=0,top=0)
        
    def run(self, ):
        menu_option = 0;      
        pygame.mixer_music.load(MENU_MUSIC)
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(55, "Mountain",(COLOR_ORANGE),((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Shooter",(COLOR_ORANGE),((WIN_WIDTH / 2), 112))
            
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i],COLOR_PURPLE,((WIN_WIDTH / 2), 180 + 30 * i))     
                else:
                    self.menu_text(20, MENU_OPTION[i],COLOR_WHITE,((WIN_WIDTH / 2), 180 + 30 * i))
            
            pygame.display.flip()
                    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # end pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # DOWN KEY
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:  # UP KEY
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:  # ENTER
                        return MENU_OPTION[menu_option] 
                        
            
                    
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Impact", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)     