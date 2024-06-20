#parking
import pygame
import modules.path_to_file as m_path




class Cross():
    def __init__(self , x , y, name = "cross"):
        self.NAME = name
        self.WIDTH = 210
        self.HIGHT = 215
        self.X = x
        self.Y = y
        
    def load_image(self):
        image_background = pygame.image.load(
            m_path.find_path_to_file(f'images/{self.NAME}.png')
       )
        img_transform = pygame.transform.scale(image_background, (self.WIDTH, self.HIGHT))
        return img_transform
    
    def blit_sprite(self, screen_game):
        screen_game.blit(self.load_image(), (self.X, self.Y))

cross =  Cross(x = 0, y = 0)      

