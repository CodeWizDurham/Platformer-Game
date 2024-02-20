from class_Enemy import enemy
from class_Player import player
from class_Platform import platform
import pygame

pygame.init() #initialize's pygame 
screen = pygame.display.set_mode((700, 700)) #(screen size x, screen size y)
clock = pygame.time.Clock()
running = True

#class initialize
walker = enemy("Walker", "pass", 10, 2, 2, "Walker", "pass", "pass", "pass", "pass", "pass", "pass", "none", 150, 391, screen)
player = player("Player", "pass", 10, 10, 20, "Walker", "pass", "pass", "pass", "pass", "pass", "pass", "none", 350, 600, screen)


#Platform rects
obstacle_rect = [
    pygame.Rect(0, 600, 700, 100), 
    pygame.Rect(100, 400, 100, 10),
    pygame.Rect(300, 500, 100, 10),
    pygame.Rect(500, 300, 100, 10)
]

def background():
    screen.fill("black")
    pygame.draw.rect(screen, (250, 250, 250), (0, 600, 700, 100)) #(screen, (RGB color Value), (position x, position y, width, hight))
    pygame.draw.rect(screen, (250, 250, 250), (100, 400, 100, 10)) 
    pygame.draw.rect(screen, (250, 250, 250), (300, 500, 100, 10)) 
    pygame.draw.rect(screen, (250, 250, 250), (500, 300, 100, 10)) 
    
    background_image = pygame.image.load("bw.png")
    background_image = pygame.transform.scale(background_image, (700, 700))
    screen.blit(background_image, (0,0))
    #character_rect = character_image.get_rect()
    
while running:
    for event in pygame.event.get(): # poll for events
        if event.type == pygame.QUIT: # pygame.QUIT event means the user clicked X to close your window
            running = False
            
    # RENDER YOUR GAME HERE
    background()
    player.display_Health()
    walker.movement_Update(obstacle_rect)
    player.movement_Update()
    running = player.health_Update(walker.attack(player.reference_Rect()))
    
    #player.attack()
    
    pygame.display.update()
    
    clock.tick(20)  # limits FPS to 30
pygame.quit()