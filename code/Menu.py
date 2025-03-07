import pygame

from pygame import Surface, Rect
from pygame.font import Font
from code.Const import COLOR_OPTIONS_MENU, MENU_MUSIC, MENU_OPTION, WIN_WIDTH, COLOR_MAIN_TEXT_MENU

class Menu:
    def __init__(self, window): 
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png')
        self.rect = self.surf.get_rect(left=0,top=0)
        
    def run(self, ):       
        pygame.mixer_music.load(MENU_MUSIC)
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(55, "Mountain",(COLOR_MAIN_TEXT_MENU),((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Shooter",(COLOR_MAIN_TEXT_MENU),((WIN_WIDTH / 2), 112))
            
            for i in range(len(MENU_OPTION)):
                self.menu_text(20, MENU_OPTION[i],COLOR_OPTIONS_MENU,((WIN_WIDTH / 2), 180 + 30 * i))
            
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('Closing game...') 
                    pygame.quit()
                    quit()
                    
                    
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Impact", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)     