import pygame as pyg

pyg.init()

class Dino(pyg.sprite.Sprite):
    def __init__(self):
        super(Dino , self).__init__()
        self.dino_run= [pyg.image.load("assets\dino1.png").convert_alpha(),
                        pyg.image.load("assets\dino2.png").convert_alpha()]
        self.dino_crouch = [pyg.image.load("assets\dino_crouch1.png").convert_alpha(),
                            pyg.image.load("assets\dino_crouch2.png").convert_alpha()]
        

        self.image= self.dino_run[0]
        self.mask= pyg.mask.from_surface(self.image)
        self.resetdino()
        self.gravity= 10
        self.jump_speed = 250
        
    def update(self, dt):
        keys = pyg.key.get_pressed()
        if keys[pyg.K_DOWN]:
            self.crouch= True 
        else : self.crouch = False

        if self.is_on_ground:
            if self.anim_counter== 7:
                if self.crouch : 
                    self.image = self.dino_crouch[self.image_switch]
                    self.rect = pyg.Rect(200,220, 55, 30)
                    self.mask= pyg.mask.from_surface(self.image)                       #height changed
                else :
                    self.image = self.dino_run[self.image_switch]
                    self.rect = pyg.Rect(200,200, 43, 51)
                    self.mask= pyg.mask.from_surface(self.image)

                if self.image_switch == 0 : self.image_switch =1
                else :self.image_switch = 0
                self.anim_counter = 0
            self.anim_counter += 1

        else :
            self.vel_y += self.gravity*dt
            self.rect.y += self.vel_y

            if self.rect.y >= 200:
                self.is_on_ground = True
                self.rect.y = 200

    def jump_dino(self,dt):
        if self.is_on_ground:
            self.vel_y =- self.jump_speed*dt
            self.is_on_ground = False


    def resetdino(self):
        self.rect = pyg.Rect(200,200, 43, 51)
        self.anim_counter = 0
        self.image_switch= 1
        self.is_on_ground = True
        self.vel_y = 0


