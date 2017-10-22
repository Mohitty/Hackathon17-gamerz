try:
    import sys, os, time
    import pygame
    import random
    from socket import *
    from pygame.locals import *
except ImportError, err:
       print "couldn't load module. %s" %(err)
       sys.exit(2)




#Initialise screen
pygame.init()
screen = pygame.display.set_mode((500,700))
pygame.display.set_caption('DOTS WAR')
introimage = pygame.image.load("dotmain.jpg").convert()

clock = pygame.time.Clock()

buttonsc = pygame.mixer.Sound("button.wav")
finall = pygame.mixer.Sound("finall.wav")
pygame.mixer.music.load("mainw.wav")

def text_objects(text, font):
    textSurface = font.render(text, True, (255,255,0))
    return textSurface, textSurface.get_rect()
    
def button(msg,x,y,w,h,ic,ac,action=None):    
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    
    
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            pygame.mixer.music.stop()
            pygame.mixer.Sound.play(buttonsc)
            action()         
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("freesansbold.ttf",30)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)
    
    
def quit_game():
    pygame.quit()
    quit()
    
def finalpage(score1,score2):
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(finall)
    final = True
    while final:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill((0,0,0))
        
        pygame.draw.rect(screen,(170,170,170),[0,0,500,200],0)
        font = pygame.font.Font(None, 50)
        text = font.render("FINAL SCORE", 1, (255, 255, 0))
        width = text.get_width()
        screen.blit(text, (250-(width/2),10))
        
        pygame.draw.rect(screen,(255,0,0),[248.5,70,3,100],0)
        
        font = pygame.font.Font(None, 36)
        text = font.render("PLAYER 1", 1, (255, 0, 0))
        width1 = text.get_width()
        screen.blit(text, (20,85))
        
        font = pygame.font.Font(None, 36)
        text = font.render("PLAYER 2", 1, (255, 0, 0))
        width2 = text.get_width()
        screen.blit(text, (500-width2-20,85))
        
        font = pygame.font.Font(None, 45)
        text = font.render(str(score1), 1, (255, 0, 0))
        width3 = text.get_width()
        height1 = text.get_height()
        screen.blit(text, ((20+(width1/2))-(width3/2),150-height1))
        
        font = pygame.font.Font(None, 42)
        text = font.render(str(score2), 1, (255, 0, 0))
        width4 = text.get_width()
        height2 = text.get_height()
        screen.blit(text, (500-(20+(width2/2))-(width4/2),150-height2))
        
        if score1>score2:
            font = pygame.font.Font(None, 86)
            text = font.render("PLAYER 1 WINS!", 1, (255, 0, 0))
            widths1 = text.get_width()
            heights1 = text.get_height()
            screen.blit(text, (250-(widths1/2),450-(heights1/2)))
            
        if score2>score1:
            font = pygame.font.Font(None, 86)
            text = font.render("PLAYER 2 WINS!", 1, (255, 0, 0))
            widths1 = text.get_width()
            heights1 = text.get_height()
            screen.blit(text, (250-(widths1/2),450-(heights1/2)))
            
        if score1==score2:
            font = pygame.font.Font(None, 86)
            text = font.render("MATCH DRAW!", 1, (255, 0, 0))
            widths1 = text.get_width()
            heights1 = text.get_height()
            screen.blit(text, (250-(widths1/2),450-(heights1/2)))
            
        button("PLAY AGAIN",85,500,150,50,(202,45,45),(0,255,0),game_loop)
        button("QUIT",314,500,100,50,(202,45,45),(0,255,0),quit_game)
        
        pygame.display.update()
        clock.tick(15)
 
def update_score(s1,s2,width1,width2):  
    font = pygame.font.SysFont(None, 45)
    pygame.draw.rect(screen,(170,170,170),[(20+(width1/2))-(40/2),150-40,40,40],0)
    text = font.render(str(s1), True, (255, 0, 0))
    width3 = text.get_width()
    height1 = text.get_height()
    screen.blit(text, ((20+(width1/2))-(width3/2),150-height1))
    
    font = pygame.font.SysFont(None, 42)
    pygame.draw.rect(screen,(170,170,170),[500-(20+(width2/2))-(40/2),150-40,40,40],0)
    text = font.render(str(s2), True, (255, 0, 0))
    width4 = text.get_width()
    height2 = text.get_height()
    screen.blit(text, (500-(20+(width2/2))-(width4/2),150-height2))
    
def controls():

    pygame.mixer.music.play(-1)
    controls = True
    while controls:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill((0,0,0))
        
        pygame.draw.rect(screen,(170,170,170),[0,0,500,200],0)
        font = pygame.font.Font(None, 80)
        text = font.render("CONTROLS", 1, (255, 255, 0))
        width = text.get_width()
        height = text.get_height()
        screen.blit(text, (250-(width/2),100+(height/2)))
        
        font = pygame.font.Font(None, 30)
        text = font.render("1.  USE MOUSE TO SELECT DOTS.", 1, (250, 250, 250))
        width1 = text.get_width()
        height1 = text.get_height()
        screen.blit(text, (250-(width1/2),300))
        
        font = pygame.font.Font(None, 30)
        text = font.render("2.  USE KEY q OR KEY esc TO", 1, (250, 250, 250))
        height2 = text.get_height()
        screen.blit(text, (250-(width1/2),300+height1+30))
        
        font = pygame.font.Font(None, 30)
        text = font.render("QUIT GAME WHILE PLAYING.", 1, (250, 250, 250))
        height3 = text.get_height()
        screen.blit(text, (250-(width1/2),300+height1+30+height2+10))
        
        
        button("BACK",200,650,100,50,(202,45,45),(0,255,0),game_intro)
        pygame.display.update()
        clock.tick(15)
def rule():

    pygame.mixer.music.play(-1)
    rule = True
    while rule:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill((0,0,0))
        
        pygame.draw.rect(screen,(170,170,170),[0,0,500,200],0)
        font = pygame.font.Font(None, 80)
        text = font.render("RULES", 1, (255, 255, 0))
        width = text.get_width()
        height = text.get_height()
        screen.blit(text, (250-(width/2),100+(height/2)))
        
        font = pygame.font.Font(None, 30)
        text = font.render("1.  THIS IS A TWO PLAYERS GAME.", 1, (250, 250, 250))
        width1 = text.get_width()
        height1 = text.get_height()
        screen.blit(text, (250-(width1/2),220))
        
        font = pygame.font.Font(None, 30)
        text = font.render("2.  PLAYERS HAVE TO DRAW LINE BY", 1, (250, 250, 250))
        height2 = text.get_height()
        screen.blit(text, (250-(width1/2),220+height1+20))
        
        font = pygame.font.Font(None, 30)
        text = font.render("SELECTING TWO ADJACENT DOTS ONE", 1, (250, 250, 250))
        height3 = text.get_height()
        screen.blit(text, (250-(width1/2),220+height1+20+height2+5))
        
        font = pygame.font.Font(None, 30)
        text = font.render("BY ONE.", 1, (250, 250, 250))
        height4 = text.get_height()
        screen.blit(text, (250-(width1/2),220+height1+20+height2+5+height3+5))
        
        font = pygame.font.Font(None, 30)
        text = font.render("3. PLAYER WILL GET ALTERNATIVE", 1, (250, 250, 250))
        height5 = text.get_height()
        screen.blit(text, (250-(width1/2),220+height1+20+height2+5+height3+20+height4))
        
        font = pygame.font.Font(None, 30)
        text = font.render("CHANCES.", 1, (250, 250, 250))
        height6 = text.get_height()
        screen.blit(text, (250-(width1/2),220+height1+20+height2+5+height3+20+height4+5+height5))
        
        font = pygame.font.Font(None, 30)
        text = font.render("4.  THE PLAYER WHO COMPLETED", 1, (250, 250, 250))
        height7 = text.get_height()
        screen.blit(text, (250-(width1/2),220+height1+20+height2+5+height3+20+height4+5+height5+20+height6))
        
        font = pygame.font.Font(None, 30)
        text = font.render("THE SQUARE WILL GET  1 POINT.", 1, (250, 250, 250))
        height8 = text.get_height()
        screen.blit(text, (250-(width1/2),220+height1+20+height2+5+height3+20+height4+5+height5+20+height6+5+height7))
        
        font = pygame.font.Font(None, 30)
        text = font.render("5.  AFTER COMPLETION OF ALL", 1, (250, 250, 250))
        height9 = text.get_height()
        screen.blit(text, (250-(width1/2),220+height1+20+height2+5+height3+20+height4+5+height5+20+height6+5+height7+20+height8))
        
        font = pygame.font.Font(None, 30)
        text = font.render("THE SQAURES,  THE GAME WILL END", 1, (250, 250, 250))
        height10 = text.get_height()
        screen.blit(text, (250-(width1/2),220+height1+20+height2+5+height3+20+height4+5+height5+20+height6+5+height7+20+height8+5+height9))
        
        font = pygame.font.Font(None, 30)
        text = font.render("AND THE PLAYER WITH MAXIMUM", 1, (250, 250, 250))
        height11 = text.get_height()
        screen.blit(text, (250-(width1/2),220+height1+20+height2+5+height3+20+height4+5+height5+20+height6+5+height7+20+height8+5+height9+5+height10))
        
        font = pygame.font.Font(None, 30)
        text = font.render("POINT WILL WIN THE GAME", 1, (250, 250, 250))
        height12 = text.get_height()
        screen.blit(text, (250-(width1/2),220+height1+20+height2+5+height3+20+height4+5+height5+20+height6+5+height7+20+height8+5+height9+5+height10+5+height11))
        
        
        button("BACK",200,650,100,50,(202,45,45),(0,255,0),game_intro)
        pygame.display.update()
        clock.tick(15)
                   
    
def game_intro():

    pygame.mixer.music.play(-1)

    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.blit(introimage,(0,0))
        screen.blit(introimage,(0,490))
        largeText = pygame.font.Font("freesansbold.ttf",75)
        TextSurf, TextRect = text_objects("DOT WARS", largeText)
        TextRect.center = ((500/2),(700/2))
        screen.blit(TextSurf, TextRect)
        
        button("PLAY",85,450,100,50,(202,45,45),(0,255,0),game_loop)
        button("QUIT",314,450,100,50,(202,45,45),(255,0,0),quit_game)
        button("RULES",85,520,120,50,(202,45,45),(0,0,250),rule)
        button("CONTROLS",314,520,160,50,(202,45,45),(0,0,250),controls)

        pygame.display.update()
        clock.tick(15)
        
def game_loop():
   
    
    screen.fill((0,0,0))
    
    pygame.draw.rect(screen,(170,170,170),[0,0,500,200],0)
    
    font = pygame.font.Font(None, 50)
    text = font.render("SCORE", 1, (255, 255, 0))
    width = text.get_width()
    screen.blit(text, (250-(width/2),10))
    
    pygame.draw.rect(screen,(255,0,0),[248.5,70,3,100],0)
    
    font = pygame.font.Font(None, 36)
    text = font.render("PLAYER 1", 1, (255, 0, 0))
    width1 = text.get_width()
    height1 = text.get_height()
    screen.blit(text, (20,85))
    
    font = pygame.font.Font(None, 36)
    text = font.render("PLAYER 2", 1, (255, 0, 0))
    width2 = text.get_width()
    screen.blit(text, (500-width2-20,85))

    up,down,left,right =0,0,0,0
    x, y = 20, 300

    grid = []
    for i in range(6):
           list1 = []
           for j in range(6):
               x = x + 70
               y = 300 + 70*i        
               z = [x,y,up,down,left,right]
               list1.append(z)
               pygame.draw.rect(screen,(255,255,255),[x,y,8,8],0)
       
           x = 20
           y = y + 70
           grid.append(list1)
           
    player1 = True
    player2 = False
    s1 = 0 
    s2 = 0
    count = 0
    m = [[0 for x in range(7)] for y in range(7)]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit();sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    quit_game()

            elif event.type == pygame.MOUSEBUTTONUP:
                pygame.mixer.music.stop()
                pygame.mixer.Sound.play(buttonsc)
                
                pos1 = event.pos
                if count == 0:
                    r1 = (pos1[0]-90)%70
                    r2 = (pos1[1]-300)%70
                    
                    q1 = (pos1[0]-90)/70
                    q2 = (pos1[1]-300)/70
                    
                    temp = 1
                   
                if count == 1:
                    r3 = (pos1[0]-90)%70
                    r4 = (pos1[1]-300)%70
                    
                    q3 = (pos1[0]-90)/70
                    q4 = (pos1[1]-300)/70
                    
                    temp = 2

                count = temp
                if count == 1:
                    if r1>8 or r2>8:              
                        count = 0                
                        continue
                    pt1 = grid[q2][q1] 

                    if not(pt1[2]*pt1[3]*pt1[4]*pt1[5] == 0) and pt1[2]+pt1[3]+pt1[4]+pt1[5] == 0:
                        count = 0
                        continue
                    pygame.draw.rect(screen,(0,255,0),[pt1[0],pt1[1],8,8],0) 

                if count == 2:
                    if r3>8 or r4>8:              
                        count = 1                
                        continue

                    if q3-q1 == 0 and q4-q2 == 0:
                        count = 0
                        pygame.draw.rect(screen,(255,255,255),[pt1[0],pt1[1],8,8],0)
                        continue

                    if not((abs(q3-q1) == 1 and abs(q4-q2) == 0) or (abs(q3-q1) == 0 and abs(q4-q2) == 1)):
                        count = 1                
                        continue

                    if abs(q3 - q1)>0:
                        if q3<q1:
                            if pt1[4] == -1:
                                count = 1
                                continue
                        else:
                            if pt1[5] == 1:
                                count = 1
                                continue

                    if abs(q4 - q2)>0:
                        if q4<q2:
                            if pt1[2] == 1:
                                count = 1
                                continue
                        else:
                            if pt1[3] == -1:
                                count = 1
                                continue
                    count = 0   
                    pt2 = grid[q4][q3]
                    pygame.draw.rect(screen,(255,255,255),[pt1[0],pt1[1],8,8],0)

                    if player1 == True:
                        pygame.draw.line(screen,(0,0,255),[pt1[0]+4,pt1[1]+4],[pt2[0]+4,pt2[1]+4],4)
                    elif player2 == True:
                        pygame.draw.line(screen,(255,0,0),[pt1[0]+4,pt1[1]+4],[pt2[0]+4,pt2[1]+4],4)
                    
                    if abs(q3-q1) == 1 and abs(q4-q2) == 0:
                        if (q3-q1) == 1:
                            pt1[5], pt2[4] = 1, (-1)
                            m[q1+1][q2] += 1
                            m[q1+1][q2+1] +=1
                            if m[q1+1][q2] == 4:
                                if player1 == True:
                                    s1 += 1
                                else:
                                    s2 += 1            
                            if m[q1+1][q2+1] == 4:
                                if player1 == True:
                                    s1 += 1
                                else:
                                    s2 += 1
                            elif not(m[q1+1][q2] == 4) and not(m[q1+1][q2+1] == 4):
                                if player1 == True:
                                    player1 = False
                                    player2 = True
                                else:
                                    player2 = False
                                    player1 = True
                        
                        elif (q3-q1) == (-1):
                            pt1[4], pt2[5] = -1, 1
                            m[q1][q2] += 1
                            m[q1][q2+1] +=1
                            if m[q1][q2] == 4:
                                if player1 == True:
                                    s1 += 1
                                else:
                                    s2 += 1
                            if m[q1][q2+1] == 4:
                                if player1 == True:
                                    s1 += 1
                                else:
                                    s2 += 1
                            elif not(m[q1][q2+1] == 4) and not(m[q1][q2] == 4):
                                if player1 == True:
                                    player1 = False
                                    player2 = True
                                else:
                                    player2 = False
                                    player1 = True

                    if abs(q3-q1) == 0 and abs(q4-q2) == 1:
                        if (q4-q2) == (-1):
                            pt1[2], pt2[3] = 1, -1
                            m[q1][q2] += 1
                            m[q1+1][q2] += 1
                            if m[q1][q2] == 4:
                                if player1 == True:
                                    s1 += 1
                                else:
                                    s2 += 1
                            if m[q1+1][q2] == 4:
                                if player1 == True:
                                    s1 += 1
                                else:
                                    s2 += 1
                            elif not(m[q1][q2] == 4) and not(m[q1+1][q2] == 4):
                                if player1 == True:
                                    player1 = False
                                    player2 = True
                                else:
                                    player2 = False
                                    player1 = True
                        elif (q4-q2) == 1:
                            pt1[3], pt2[2] = -1, 1
                            m[q1][q2+1] += 1
                            m[q1+1][q2+1] += 1
                            if m[q1][q2+1] == 4:
                                if player1 == True:
                                    s1 += 1
                                else:
                                    s2 += 1
                            if m[q1+1][q2+1] == 4:
                                if player1 == True:
                                    s1 += 1
                                else:
                                    s2 += 1
                            elif not(m[q1][q2+1] == 4) and not(m[q1+1][q2+1] == 4):
                                if player1 == True:
                                    player1 = False
                                    player2 = True
                                else:
                                    player2 = False
                                    player1 = True
                    print "score of player 1: ", s1
                    print "score of player 2: ", s2
                    pygame.display.update()
                    
                    update_score(s1,s2,width1,width2)
                    if s1+s2 == 25:
                        finalpage(s1,s2)
                    
        pygame.display.update()
        clock.tick(60)
    
game_intro()
game_loop()
pygame.quit()
quit()
