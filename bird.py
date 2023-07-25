import pygame as pyg

class Bird(pyg.sprite.Sprite):
    def __init__(self, enemy_grp , move_speed):
        super(Bird , self).__init__()
        self.img_list= [pyg.image.load("assets/bird1.png").convert_alpha() ,
                         pyg.image.load("assets/bird2.png").convert_alpha()]
        self.image = self.img_list[0]
        self.mask = pyg.mask.from_surface(self.image)
        self.rect= pyg.Rect(600,180, 42,31)
        self.anim_counter = 0
        self.speed = move_speed
        self.enemy_grp = enemy_grp
        self.image_switch= 1

    def update(self,dt):
        if self.anim_counter == 7:
            self.image = self.img_list[self.image_switch]
            if self.image_switch ==0 : self.image_switch = 1
            else : self.image_switch = 0
            self.anim_counter = 0
        self.anim_counter += 1

        self.rect.x -= self.speed*dt

        if self.rect.right< 0:
            self.delete_self()

    def setMove_speed(self, move_speed):
        self.speed = move_speed


    def delete_self(self) :
        self.kill()
        del self