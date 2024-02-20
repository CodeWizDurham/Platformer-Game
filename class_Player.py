import pygame
import time

class player:
    def __init__ (self, name, picture, speed, weapon, health, type_Enemy,
                  death_Animation, death_Sound, movement_Sound, attack_Sound, attack_Animation,
                  movement_Animation, armour_Type, spawn_X, spawn_Y, screen):
        self.name = name
        self.picture = picture
        self.speed = speed
        self.weapon = weapon
        self.health = health
        self.type_Enemy = type_Enemy
        self.death_animation = death_Animation
        self.death_Sound = death_Sound
        self.attack_Sound = attack_Sound
        self.movement_Sound = movement_Sound
        self.attack_Animation = attack_Animation
        self.movement_Animation = movement_Animation
        self.armour_Type = armour_Type
        self.spawn_X = spawn_X
        self.spawn_Y = spawn_Y
        self.current_X = spawn_X
        self.current_Y = spawn_Y
        self.Rect = pygame.Rect(self.current_X, self.current_Y, 10,10)
        self.movement = 1
        self.screen = screen
        self.obstacle_rect = [
            pygame.Rect(0, 580, 700, 100), 
            pygame.Rect(100, 380, 100, 10),
            pygame.Rect(300, 480, 100, 10),
            pygame.Rect(500, 280, 100, 10)
        ]
        self.fall_speed = 0
        self.gravity = 0.35
        self.screen_height = 700
        self.character_height = 20
        self.jump_Cooldown = 0
        self.frame = 0

    def movement_Update(self):
        
        temp_x = self.current_X
        temp_y = self.current_Y
        
        self.Rect = pygame.Rect(self.current_X, self.current_Y, 10,10)

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            self.current_X -= 5
            
        if keys[pygame.K_RIGHT]:
            self.current_X += 5
        
        if keys[pygame.K_DOWN]:
            if self.detect_collision():
                self.fall_speed = 0
            else:
                if self.fall_speed <= 15:
                    self.fall_speed += 5
                
        if keys[pygame.K_UP]:
            self.fall_speed = -10
        else:
            if self.detect_collision():
                if self.fall_speed != 0:
                    self.fall_speed = 0
            else: 
                self.fall_speed += self.gravity
        
        self.current_Y += self.fall_speed
        
        time.sleep(0.01)
        
        if self.current_X != temp_x or self.current_Y != temp_y:
            self.update_Animation(True)
        else:
            self.update_Animation(False)
        
        #pygame.draw.rect(self.screen, (250, 0, 0), (self.current_X, self.current_Y, 20, 20))
        pygame.display.update()
        
    def health_Update(self, health_Change):
        self.health -= int(health_Change)
        print(self.health)
        self.display_Health()
        if self.health <= 0:
            return False
            #death animation
        else:
            return True
            
    def attack(self):
        self.animate("_Attack.png")
    
    def detect_collision(self):
        
        for bounding_Box in self.obstacle_rect:
            if self.Rect.colliderect(bounding_Box) == True:
                self.current_Y = bounding_Box.top
                return True
        
    def reference_Rect(self):
        return self.Rect
    
    def display_Health(self):
        font = pygame.font.SysFont("calibri", 40)
        text = font.render(str(self.health),True, (0, 255, 0))
        self.screen.blit(text, (10, 10))
        
    def animate(self, image):
        character_image = pygame.image.load(image)
        character_rect = character_image.get_rect()
        character_height = character_rect.height
        frames = character_image.get_width()/120
        
        frames_image = []
        
        for x in range(0,int(frames)):
            frames_image.append(character_image.subsurface(pygame.Rect(x * 120, 0, character_image.get_width() // frames, character_image.get_height())))
            
        return frames_image
            
    def update_Animation(self,step):
        
        frames = self.animate("_Run.png")
        
        if step == True:
            print("step")
            self.frame = self.frame + 1
        
        if len(frames) <= self.frame:
            self.frame = 0
            
        
        
        self.screen.blit(frames[self.frame], (self.current_X - frames[self.frame].get_width()/2,self.current_Y - frames[self.frame].get_height()/2))