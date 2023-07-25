import pygame as pyg
import sys
import time 
from dino import Dino
from bird import Bird
from trees import Tree
import random
pyg.init()

class Game:
    def __init__(self): 
        self.width = 600
        self.height = 300
        self.win= pyg.display.set_mode((self.width ,self.height))
        self.clock = pyg.time.Clock()

        self.ground1= pyg.image.load("assets/ground.png").convert_alpha()
        self.ground1_rect = self.ground1.get_rect(center=(300,250))

        self.ground2= pyg.image.load("assets/ground.png").convert_alpha()
        self.ground2_rect = self.ground2.get_rect(center=(900, 250))
        
        self.font1 = pyg.font.Font("assets/font.ttf",17)
        self.label_score = self.font1.render("Score : 0" , True , (0,23,20))
        self.label_rect = self.label_score.get_rect(center= (480,25))   

        self.font2 = pyg.font.Font("assets/font.ttf",20)
        self.restart = self.font2.render("Restart Game" , True , (0,23,20))
        self.restart_rect = self.label_score.get_rect(center = (270,130))

        self.font3 = pyg.font.Font("assets/font.ttf",10)
        self.space = self.font3.render("Press Space" , True , (0,23,20))
        self.space_rect = self.label_score.get_rect(center = (315,160)) 

        self.dino = Dino()
        self.move_speed = 220
        self.game_lost = False
        self.enemy_spawn_counter = 0
        self.enemy_spawn_time = 100
        self.score = 0
        self.enemy_grp = pyg.sprite.Group()
        
        self.dead_sound = pyg.mixer.Sound("assets\sfx\dead.mp3")
        self.jump_sound = pyg.mixer.Sound("assets\sfx\jump.mp3")
        self.points_sound = pyg.mixer.Sound("assets\sfx\points.mp3")
        
        self.gameLoop()
        
    def check_collions(self):
        if pyg.sprite.spritecollide(self.dino , self.enemy_grp , False , pyg.sprite.collide_mask) :
            self.stop_game()

    def stop_game(self):
        self.game_lost= True
        self.dead_sound.play()

    def Restart(self):
        self.game_lost = False
        self.move_speed = 200
        self.enemy_spawn_counter = 0
        self.label_score = self.font1.render("Score : 0" , True , (0,23,20))
        self.score = 0

        self.dino.resetdino()

        for enemy in self.enemy_grp:
            enemy.delete_self()

    def gameLoop(self):
        last_time= time.time()
        while True :
            new_time = time.time()
            dt = new_time- last_time
            last_time = new_time
            for event in pyg.event.get():
                if event.type== pyg.QUIT:
                    pyg.quit()
                    sys.exit()

                if event.type == pyg.KEYDOWN and event.key ==pyg.K_SPACE:
                    if not self.game_lost:
                        self.dino.jump_dino(dt)
                        self.jump_sound.play()
                    else :
                        self.Restart()

            self.win.fill((220,255,255))   
            
            if not self.game_lost:
                
                self.check_collions()
                self.ground1_rect.x -= int(self.move_speed*dt)
                self.ground2_rect.x -= int(self.move_speed*dt)

                if self.ground1_rect.right <0:
                    self.ground1_rect.x = 600
                if self.ground2_rect.right<0 :
                    self.ground2_rect.x = 600
            
                self.score += 0.1
                self.label_score = self.font1.render(f"Score : {int(self.score)}", True , (0,23,20))
                self.dino.update(dt)
                self.enemy_grp.update(dt)

                if self.enemy_spawn_counter == self.enemy_spawn_time:
                    if random.randint(0,1) == 0:
                        self.enemy_grp.add(Bird(self.enemy_grp, self.move_speed))
                    else : self.enemy_grp.add(Tree(self.enemy_grp , self.move_speed))
                    # enemy = Bird(self.enemy_grp, self.move_speed)
                    # self.enemy_grp.add(enemy)
                    self.enemy_spawn_counter= 0
                self.enemy_spawn_counter +=1 

                if int(self.score)%30 ==0 :
                    self.move_speed += 5
                    for enemy in self.enemy_grp:
                        enemy.setMove_speed(self.move_speed)


                if int(self.score + 1)%100 == 0:
                    self.points_sound.play()

                self.win.blit(self.dino.image ,self.dino.rect)
                for enemy in self.enemy_grp :
                        self.win.blit(enemy.image , enemy.rect)

            else : 
                self.win.blit(self.restart , self.restart_rect)
                self.win.blit(self.space , self.space_rect)
                

            
            self.win.blit(self.ground1, self.ground1_rect)
            self.win.blit(self.ground2 , self.ground2_rect)
            
            self.win.blit(self.label_score ,self.label_rect)
            
            

            pyg.display.update()
            self.clock.tick(60)

game= Game()