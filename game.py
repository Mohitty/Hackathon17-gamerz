import os,sys  #used for sys.exit and os.environ
import pygame  #import the pygame module
from random import randint

class Control:
    def __init__(self):
        self.color = 0
    def update(self,Surf):
        self.event_loop()  #Run the event loop every frame
        Surf.fill(self.color) #Make updates to screen every frame
    def event_loop(self):
        for event in pygame.event.get(): #Check the events on the event queue
            if event.type == pygame.MOUSEBUTTONDOWN:
                #If the user clicks the screen, change the color.
                self.color = [randint(0,255) for i in range(3)]
                
            elif event.type == pygame.QUIT:
                pygame.quit();sys.exit()

if __name__ == "__main__":
    os.environ['SDL_VIDEO_CENTERED'] = '1'  #Center the screen.
    pygame.init() #Initialize Pygame
    screen = pygame.display.set_mode((500,500)) #Set the mode of the screen
    MyClock = pygame.time.Clock() #Create a clock to restrict framerate
    
    up,down,left,right =0,0,0,0
    x, y = 15, 150

    grid = []
    for i in range(6):
       list1 = []
       for j in range(6):
           x = x + 35
           y = 150 + 35*i
           z = [x,y,up,down,left,right]
           list1.append(z)
           pygame.draw.rect(screen,(255,255,255),[x,y,5,5],0)
   
       x = 15
       y = y + 35
       grid.append(list1)

    RunIt = Control()
    while 1:
        RunIt.update(screen)
        pygame.display.update() #Update the screen
        MyClock.tick(60) #Restrict framerate
