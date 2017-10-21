try:
    import sys, os, time
    import pygame
    from socket import *
    from pygame.locals import *
except ImportError, err:
       print "couldn't load module. %s" %(err)
       sys.exit(2)




#Initialise screen
pygame.init()
screen = pygame.display.set_mode((500,700))
pygame.display.set_caption('DOTS WAR')

#Fill background    
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))

up,down,left,right =0,0,0,0
x, y = 30, 300

grid = []
for i in range(6):
       list1 = []
       for j in range(6):
           x = x + 70
           y = 300 + 70*i
           z = [x,y,up,down,left,right]
           list1.append(z)
           #print list1[j]
           pygame.draw.rect(screen,(255,255,255),[x,y,6,6],0)
   
       x = 30
       y = y + 70
       #grid[i] = list1
       grid.append(list1)
       
count = 0
m = [[0 for x in range(7)] for y in range(7)]
print m

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();sys.exit()

        elif event.type == pygame.MOUSEBUTTONUP:
            pos1 = event.pos
            if count == 0:
                r1 = (pos1[0]-100)%70
                r2 = (pos1[1]-300)%70
                
                q1 = (pos1[0]-100)/70
                q2 = (pos1[1]-300)/70
                
                temp = 1
               
            if count == 1:
                r3 = (pos1[0]-100)%70
                r4 = (pos1[1]-300)%70
                
                q3 = (pos1[0]-100)/70
                q4 = (pos1[1]-300)/70
                
                temp = 2
            count = temp
            if count == 1:
                if r1>10 or r2>10:              
                    count = 0                
                    continue
                #print r1,r2
                #print count
                pt1 = grid[q2][q1] 
                pygame.draw.rect(screen,(0,255,0),[pt1[0],pt1[1],6,6],0) 
            if count == 2:
                if r3>10 or r4>10:              
                    count = 1                
                    continue
                if not((abs(q3-q1) == 1 and abs(q4-q2) == 0) or (abs(q3-q1) == 0 and abs(q4-q2) == 1)):
                    count = 1                
                    continue
                #print r3,r4
                #print count 
                
                count = 0   
                pt2 = grid[q4][q3]
                pygame.draw.rect(screen,(255,255,255),[pt1[0],pt1[1],6,6],0)
                pygame.draw.line(screen,(255,255,255),[pt1[0]+3,pt1[1]+3],[pt2[0]+3,pt2[1]+3],3)
                
                if abs(q3-q1) == 1 and abs(q4-q2) == 0:
                    if (q3-q1) == 1:
                        pt1[5], pt2[4] = 1, (-1)
                        m[q1+1][q2] += 1
                        m[q1+1][q2+1] +=1
                        if m[q1+1][q2] == 4:
                            print "score+1"
                        if m[q1+1][q2+1] == 4:
                            print "score+1"
                    
                    elif (q3-q1) == (-1):
                        pt1[4], pt2[5] = 1, (-1)
                        m[q1][q2] += 1
                        m[q1][q2+1] +=1
                        if m[q1][q2] == 4:
                            print "score+1"
                        if m[q1][q2+1] == 4:
                            print "score+1"

                if abs(q3-q1) == 0 and abs(q4-q2) == 1:
                    if (q4-q2) == (-1):
                        pt1[2], pt2[3] = 1, (-1)
                        m[q1][q2] += 1
                        m[q1+1][q2] += 1
                        if m[q1][q2] == 4:
                            print "score+1"
                        if m[q1+1][q2] == 4:
                            print "score+1"
                    elif (q4-q2) == 1:
                        pt1[3], pt2[2] = 1, (-1)
                        m[q1][q2+1] += 1
                        m[q1+1][q2+1] += 1
                        if m[q1][q2+1] == 4:
                            print "score+1"
                        if m[q1+1][q2+1] == 4:
                            print "score+1"
                print m
    pygame.display.update()
