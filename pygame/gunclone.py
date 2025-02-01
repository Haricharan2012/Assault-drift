import pygame   #importing the pygame module
import random    #random range 

#INITIALIZATION BLOCK
pygame.init()  #initializing the module

SCREEN_WIDTH=800
SCREEN_HEIGHT=500 #SPECIFIES WIDOW WIDTH AND HEIGHT

screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) #CREATING a game window using a function

back=pygame.image.load("abcs.jpg")  #background image
#gun=pygame.image.load("GUN.png")  #gun 
new_size=(800,500)     #new bg size
gun_s=(200,200)   #new gun size

coin=pygame.image.load("coin.png")   #loading coin image

#flare=pygame.image.load("flare.png")
bomb_s=(50,50)                          #coin size
ncoin=pygame.transform.scale(coin,bomb_s)   #scaling the coin
flare_s=(80,80)                             #size of the flare
#nflare=pygame.transform.scale(flare,flare_s)

nback=pygame.transform.scale(back,new_size) #to change size of background image we use "pygame.transform.scale(back,new_size)" here "back" is the bg image and "new_size" is a variable which has new size width=800 height=500 it is assigned to new var nback 
#ngun=pygame.transform.scale(gun,gun_s)  #to change size of gun image (gun_s is new var having widht=200,height=200)
char=pygame.image.load('mon1.png').convert_alpha()           #enemy state1
tchar=[pygame.image.load('mon1.png'),pygame.image.load('green.png')]
tpos=-800
font = pygame.font.SysFont(None, 48)   #font 

#rectangle for character

#colors
white=(255,255,255)
BLACK = (0, 0, 0)
orange=(255, 165, 0)
crimson=(220, 20, 60)
Yellow=(255, 255, 0)

#scores
score=0  #game score 
cscore=0 #coins


#text = font.render("score: " + str(score), True, BLACK)
#positions 
kpos=0
cypos=0     #coin y position
cxpos=200   #coin x position



#timer




char_s=(100,100)  #setting size for character state 1
nchar=pygame.transform.scale(char,char_s) #scaling
#cursor
pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)


#music
shot=pygame.mixer.Sound("gun.wav")  #loading gun sound
ching=pygame.mixer.Sound("coins.wav") #loading coin sounds
font = pygame.font.SysFont(None, 48) #font  size48
tshot=pygame.mixer.Sound("gun.wav")  #temp gunshot
#char anim


# MAIN GAME BLOCK
#GAMELOOP

    
run=True
while run:  #condition to check if game is running
    pos=pygame.mouse.get_pos()   # variable position = position of mouse (x coordinate,y coordinate)
    xpos=pos[0] #xpos is a variable which contains only x cordinate from mouse pos
    ypos=pos[1] #ypos is a var which contains only y coordinate
    tpos=tpos+1
    charrect=pygame.Rect(tpos,kpos,100,100)  #rect encasing character
    coinrect=pygame.Rect(cxpos,cypos,50,50)  #rect encasing coin

    collision=charrect.collidepoint(pos)     #collision btw character rect and mouseclick
    coincoll=coinrect.collidepoint(pos)      #collision btw coin rect and mouseclick
    text = font.render("Score: " + str(score), True, crimson)  #display score on screen
    ctext= font.render("Coins: " +str(cscore), True,orange)    #display no of coins on screen
    
    cypos=cypos+1                   #coinpos y axis  (increasing)

    if(score==10):
        back=pygame.image.load("snow.png")                               #probably level 2 loading 2nd image and updating nback
        nback=pygame.transform.scale(back,new_size)
    
    


  

    time=pygame.time.get_ticks()/5                              #from the time game stated counting in milliseconds 1-3000
    if(not collision):
        if(time%2==0):
            char=pygame.image.load("mon2.png")
            nchar=pygame.transform.scale(char,char_s)
     
        elif(time%5==0):
            char=pygame.image.load("mon3.png")
            nchar=pygame.transform.scale(char,char_s)
        elif(time%7==0):
            char=pygame.image.load("mon4.png")
            nchar=pygame.transform.scale(char,char_s)
        else:
            char=pygame.image.load("mon5.png")
            nchar=pygame.transform.scale(char,char_s)
            
    for event in pygame.event.get():
        if event.type==pygame.MOUSEMOTION:
     
                                           #event handler checks for events
            pygame.MOUSEMOTION=ngun.set_palette
        if event.type==pygame.QUIT:            #if cross is pressed
            run==False                       #we exit the game so run =false
        elif event.type==pygame.MOUSEBUTTONDOWN:   #if mousebutton is pressed
            pygame.mixer.Sound.play(shot)        #playsound
            gun=pygame.image.load("GUN2.png")     #gunn state change
            ngun=pygame.transform.scale(gun,gun_s)   #updating
            flare=pygame.image.load("flare.png")     #gunflare
            nflare=pygame.transform.scale(flare,flare_s)   #scaling

            if(coincoll):                                     #coincollision 
                cxpos=random.randrange(200,500)
                cypos=cypos-1000               #coin y pos (decrease)
                cscore=cscore+50               #increase points by 50
                pygame.mixer.Sound.play(ching)   #coin chime
                #shot=ching
                shot.stop()   # when mousebutton pressed on coin then gunshot sound will be stopped
                gun=pygame.image.load("GUN.png")     #gunn state change
                ngun=pygame.transform.scale(gun,gun_s)  #gun state stable no change
                flare=pygame.image.load("blank.png")     #gunflare
                nflare=pygame.transform.scale(flare,flare_s) 
                
                
                

                
            if(collision):                                    #enemy collision
                char=pygame.image.load("explo.png")
                nchar =pygame.transform.scale(char,char_s)   #
                tpos=tpos-1000
                score=score+1
                kpos=random.randrange(200,270)  #y pos of char
                char=pygame.image.load("green.png")
                nchar=pygame.transform.scale(char,char_s)
                
                pygame.SYSTEM_CURSOR_HAND
                #shot=tshot
        
           
        else:
            gun=pygame.image.load("GUN.png")
            ngun=pygame.transform.scale(gun,gun_s)
            flare=pygame.image.load("blank.png")
            nflare=pygame.transform.scale(flare,flare_s)

    
                                                               #play gunshot sound
    text_rect = text.get_rect()  #rect for string score
    ctext_rect=ctext.get_rect() #rect for string coins
  
    # Center the text
    text_rect.center = (SCREEN_WIDTH-80, SCREEN_HEIGHT-480)
    ctext_rect.center =(SCREEN_WIDTH-80, SCREEN_HEIGHT-440)
    # Draw the text onto the screen
     
#DRAW GAME                                                    
    screen.fill((255,255,255))  #fills the screen with white color
    screen.blit(nback,(0,0))   #bilt means to draw on certain coordinates here we are drawing nback(bg) which has the altered size
    screen.blit(ngun,(xpos,300)) #we are drawing ngun(gun) on x position of mouse and y is set to 300 so as to lock it from moving it wont follow of mouse
    pygame.draw.rect(nchar,white,charrect)  #drawing rect 

    screen.blit(nchar,(tpos,kpos)) #200
    pygame.draw.rect(screen,white,charrect,2) #drawing rect over character 
    pygame.draw.rect(screen,white,coinrect,2) #drawing rect over coin
    screen.blit(nflare,(xpos,280))#t tpos keeps updating
    screen.blit(text, text_rect)  #drawing score text
    screen.blit(ctext, ctext_rect) #drawing coins score text
    screen.blit(ncoin,(cxpos,cypos))    #draw coin 
      #update anim
   
   
         
    pygame.display.flip()  #used to update display no drawing can occur without this method
pygame.quit()
        
