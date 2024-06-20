import pygame

import modules.path_to_file as m_path



class Zero():


    def __init__(self, x, y,name= "zero"):
        
        self.NAME = name
        
        self.WIDTH = 210
                        
        self.HEIGHT = 215
                  
        self.X = x
                  
        self.Y = y
        
    def load_image(self):
        
        
        
        image_zero = pygame.image.load(
         
            m_path.find_path_to_file(f'images/{self.NAME}.png')
        )
       
        img_transform = pygame.transform.scale(image_zero, (self.WIDTH, self.HEIGHT))
       
        return img_transform 
    
    
    def blit_sprite(self, screen_game):
        
        screen_game.blit(self.load_image(), (self.X, self.Y))
    
zero = Zero(x = 0, y = 0)
