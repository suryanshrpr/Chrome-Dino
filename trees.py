import pygame as pyg
import random

class Tree(pyg.sprite.Sprite):
    def __init__(self,enemy_grp , move_speed):
        super(Tree , self).__init__()
        self.img_list = []
        for i in range(1,6):
            self.img_list.append(pyg.image.load(f"assets/trees/tree{i}.png").convert_alpha())
        self.image= self.img_list[random.randint(0,4)]
        self.mask = pyg.mask.from_surface(self.image)
        self.rect = pyg.Rect(600,207 , 50 , 50)
        self.speed = move_speed
        self.enemy_grp = enemy_grp

    def update(self, dt):
        self.rect.x -= self.speed*dt

        if self.rect.right <0 :
            self.delete_self()

    def setMove_speed(self, move_speed):
        self.speed = move_speed

    def delete_self(self) :
        self.kill()
        del self
