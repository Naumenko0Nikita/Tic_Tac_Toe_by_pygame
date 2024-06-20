# Класс для фону писав Науменко та Пилепенко 
import pygame 

import modules.path_to_file as m_path

class Background():
    
    def __init__(self , x , y):
        self.WIDTH = 680
        self.HIGHT = 680
        self.X = x
        self.Y = y
    
    def load_image(self):
       
        image_background = pygame.image.load(
           
            m_path.find_path_to_file('images/background.jpg')
       )
      
        img_transform = pygame.transform.scale(image_background, (self.WIDTH, self.HIGHT))
       
        return img_transform
    
   
    def blit_sprite(self, screen_game):
        
        screen_game.blit(self.load_image(), (self.X, self.Y))

background = Background(x = 0, y = 0)      