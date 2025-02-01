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

kew_size=(800,500) 

coin=pygame.image.load("coin.png")   #loading coin image

#flare=pygame.image.load("flare.png")
bomb_s=(50,50)                          #coin size
ncoin=pygame.transform.scale(coin,bomb_s)   #scaling the coin
flare_s=(80,80)                             #size of the flare
#nflare=pygame.transform.scale(flare,flare_s)

nback=pygame.transform.scale(back,new_size) #to change size of background image we use "pygame.transform.scale(back,new_size)" here "back" is the bg image and "new_size" is a variable which has new size width=800 height=500 it is assigned to new var nback 
#ngun=pygame.transform.scale(gun,gun_s)  #to change size of gun image (gun_s is new var having widht=200,height=200)

#enemy1
char=pygame.image.load('mon1.png').convert_alpha()           #enemy state1
tpos=-800
font = pygame.font.SysFont(None, 48)   #font
char_s=(100,100)  #setting size for character state 1
nchar=pygame.transform.scale(char,char_s) #scaling


#enemy2
char2=pygame.image.load('don1.png')
c2pos=800 #xpos of enemy2
nchar2=pygame.transform.scale(char2,char_s)


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

speed=0
sspeed=0


#text = font.render("score: " + str(score), True, BLACK)
#positions 
kpos=0
cypos=0     #coin y position
cxpos=200   #coin x position
lpos=150 #for char2


#mainmenu background
main=pygame.image.load("bg.png")
nmain=pygame.transform.scale(main,new_size)
nwidth=nmain.get_width() #main menu width
nheight=nmain.get_height()  #main menu height

#test screen
smain=pygame.image.load("test.jpeg")
snmain=pygame.transform.scale(smain,kew_size)
swidth=snmain.get_width() #retriving width 
sheight=snmain.get_height()  #retrieving height 
back_button=pygame.image.load("back_button.png")
tog_button=pygame.image.load("tog_button.png")
indi=pygame.image.load("on_text.png")


twidth=tog_button.get_width()    #width of toggle
theight=tog_button.get_height()  #height of toggle

bwidth=back_button.get_width()  #width of backbutton
bheight=back_button.get_height() #height of backbutton

#rect for main
mrect=pygame.Rect(800/4+120,500//4+85,150,30)
#rect for submain
srect=pygame.Rect(380,180,twidth,theight)  #rect created upon toggle button
backrect=pygame.Rect(310,250,bwidth,bheight) #rect created upon backbutton


#rect for game over
lrect=pygame.Rect(798,0,3,SCREEN_HEIGHT)
rrect=pygame.Rect(0,0,1,800)

#rect for coin regen
trect=pygame.Rect(10,1,SCREEN_WIDTH,1)
drect=pygame.Rect(10,350,SCREEN_WIDTH,20)
#timer

#cursor
pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)


#music
shot=pygame.mixer.Sound("error.wav")  #loading gun sound
ching=pygame.mixer.Sound("coins.wav") #loading coin sounds
font = pygame.font.SysFont(None, 48) #font  size48
tshot=pygame.mixer.Sound("gun.wav")  #temp gunshot
button=pygame.mixer.Sound("click.wav")

snow=pygame.mixer.Sound("snow.wav")

#char anim
dead=pygame.image.load("die.png")
ndead=pygame.transform.scale(dead,(0,0))
copos=0
coypos=0

# MAIN GAME BLOCK
#GAMELOOP
gov=pygame.image.load("blank.png")
ngov=pygame.transform.scale(gov,(0,0))

logo_s=pygame.image.load("test.jpeg")

base_font = pygame.font.Font(None, 32) 
user_text = '' 

#inputbox
input_rect = pygame.Rect(200, 200, 140, 32) 

# color_active stores color(lightskyblue3) which 
# gets active when input box is clicked by user 
color_active = pygame.Color('lightskyblue3') 

# color_passive store color(chartreuse4) which is 
# color of input box. 
color_passive = pygame.Color('chartreuse4') 
color = color_passive 

active = False






run=True
while run:  #condition to check if game is running
    pos=pygame.mouse.get_pos()   # variable position = position of mouse (x coordinate,y coordinate)
    xpos=pos[0] #xpos is a variable which contains only x cordinate from mouse pos
    ypos=pos[1] #ypos is a var which contains only y coordinate
    tpos=tpos+1
    c2pos=c2pos-1
    charrect=pygame.Rect(tpos,kpos,100,100)  #rect encasing character
    charrect2=pygame.Rect(c2pos,lpos,100,100)
    coinrect=pygame.Rect(cxpos,cypos,50,50)  #rect encasing coin
    mcollide=mrect.collidepoint(pos)
    scollide=srect.collidepoint(pos)  #toggle collision
    bcollide=backrect.collidepoint(pos) #backbutton collision
    
    collision=charrect.collidepoint(pos)     #collision btw character rect and mouseclick
    collision2=charrect2.collidepoint(pos)  #collison btw c2 rect and mousepointer
    if(coinrect.y>300):
        cypos=cypos-1000
        cxpos=random.randrange(200,500)
    if(charrect.colliderect(lrect)):  #enemy & rightrect
        print("works")
        gov=pygame.image.load("go.png")
        ngov=pygame.transform.scale(gov,new_size)
        gamemusic.stop()
    if(charrect2.colliderect(rrect)): #enemy2 &leftrect
        print("works")
        gov=pygame.image.load("go.png")
        ngov=pygame.transform.scale(gov,new_size)
        gamemusic.stop()

    
    if(score==3):
        back=pygame.image.load("snow.png")                               #probably level 2 loading 2nd image and updating nback
        nback=pygame.transform.scale(back,new_size)
        #gamemusic=snow
        gamemusic=pygame.mixer.music.unload()
    elif(score==4):
        back=pygame.image.load("desert.png")
        nback=pygame.transform.scale(back,new_size)
        #gamemusic=pygame.mixer.sound("lvl2.wav")        


    coinre=pygame.Rect.colliderect(drect,coinrect)
    
    coincoll=coinrect.collidepoint(pos)      #collision btw coin rect and mouseclick
    text = font.render("Score: " + str(score), True, crimson)  #display score on screen
    ctext= font.render("Coins: " +str(cscore), True,orange)    #display no of coins on screen
    
    cypos=cypos+1                   #coinpos y axis  (increasing)
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
            tpos=tpos+speed

        if(not collision2):
            if(time%2==0):
                char2=pygame.image.load("don2.png")
                nchar2=pygame.transform.scale(char2,char_s)
            elif(time%5==0):
                char2=pygame.image.load("don3.png")
                nchar2=pygame.transform.scale(char2,char_s)
            elif(time%7==0):
                char2=pygame.image.load("don4.png")
                nchar2=pygame.transform.scale(char2,char_s)
            else:
                char2=pygame.image.load("don5.png")
                nchar2=pygame.transform.scale(char2,char_s)
                c2pos=c2pos-sspeed
            
    for event in pygame.event.get():
        if event.type==pygame.MOUSEMOTION:
     
                                           #event handler checks for events
            pygame.MOUSEMOTION=ngun.set_palette
        if event.type==pygame.QUIT:            #if cross is pressed
            run==False                       #we exit the game so run =false
        elif event.type==pygame.MOUSEBUTTONDOWN:   #if mousebutton is pressed
           # pygame.mixer.Sound.play(button)        #playsound
            gun=pygame.image.load("GUN2.png")     #gunn state change
            ngun=pygame.transform.scale(gun,gun_s)   #updating
            flare=pygame.image.load("flare.png")     #gunflare
            nflare=pygame.transform.scale(flare,flare_s)   #scaling

            
            if(nwidth==800 and nheight==500):
                gamemusic=pygame.mixer.Sound("jung.wav")
                if mcollide:
                    tpos=-100
                    nmain=pygame.transform.scale(main,(0,0))
                    mrect.width=0
                    mrect.height=0
                    backrect.width=bwidth
                    backrect.height=bheight
                    pygame.mixer.Sound.play(button)
                    shot=pygame.mixer.Sound("gun.wav") #changing the gun shot sound after the start button is pressed
                    gamemusic=pygame.mixer.Sound("jung.wav")
                    gamemusic.play()
                    
                    
                else:
                    if scollide:
                        tpos=-400      #reset enemy
                        snmain = pygame.transform.scale(smain, (0, 0))
                        srect.width=0 
                        srect.height=0
                        
                        
                        
                        
                        
                        
                    if bcollide:
                        backrect.width=0
                        backrect.height=0
                        nmain=pygame.transform.scale(main,(800,500))
                        mrect.width=150
                        mrect.height=30

                    pygame.mixer.Sound.play(shot)  #playing the gunshot sound
                    gamemusic.stop()
                    


                  
                   
                    
                
                
            
                 
                
            #else:
                #shot.stop()
                
      
                
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


            if(coinre):
                
                cypos=+400

                
      
            #if drect.colliderect(coinrect):
                #cypos=cypos-1000
                

                
                
                

                
            if(collision):                                   #enemy collision
                
   
                char=pygame.image.load("explo.png")
                nchar =pygame.transform.scale(char,char_s)   #
                tpos=random.randrange(-2000,-500)
                score=score+1
                kpos=random.randrange(5,290)  #y pos of char
                pygame.SYSTEM_CURSOR_HAND
                dead=pygame.image.load("explo.png")
                ndead=pygame.transform.scale(dead,(100,100))
                copos=charrect.x
                coypos=charrect.y
                speed=speed+2
            
                
            if(collision2):                                        #enemy2 collision
                
                char2=pygame.image.load("explo.png")
                nchar2 =pygame.transform.scale(char2,char_s)
                c2pos=random.randrange(899,2000)
                score=score+1
                lpos=random.randrange(100,290) #y pos of char2
                pygame.SYSTEM_CURSOR_HAND
                dead=pygame.image.load("explo.png")
                ndead=pygame.transform.scale(dead,(100,100))
                copos=charrect2.x
                coypos=charrect2.y
                sspeed=sspeed+2


            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False
 
#input box block
            if event.type == pygame.KEYDOWN:
                # Check for backspace
                if event.key == pygame.K_BACKSPACE:
                    # get text input from 0 to -1 i.e. end.
                    user_text = user_text[:-1]
                 # Unicode standard is used for string
                 # formation
                else:
                    user_text += event.unicode
          
     
        

                
               # pygame.mixer.Sound.play(shot)
                #shot=tshot
             
        

            
            
        
           
        else:
            gun=pygame.image.load("GUN.png")
            ngun=pygame.transform.scale(gun,gun_s)
            flare=pygame.image.load("blank.png")
            nflare=pygame.transform.scale(flare,flare_s)
            dead = pygame.image.load("blank.png")
            ndead = pygame.transform.scale(dead, (100, 100))
        
               


            
    
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
    #pygame.draw.rect(nchar,white,charrect)  #drawing rect

    pygame.draw.rect(screen,crimson,lrect)
    
    pygame.draw.rect(screen,crimson,rrect)

    pygame.draw.rect(screen,crimson,trect)  #up and down rect

      #up and down rect
   
 





    screen.blit(ndead,(copos,coypos))
                
    screen.blit(nchar2,(c2pos,lpos))
    pygame.draw.rect(screen,white,charrect2,2) #rect over char2
    screen.blit(nchar,(tpos,kpos)) #200
    pygame.draw.rect(screen,white,charrect,2) #drawing rect over character 
    pygame.draw.rect(screen,white,coinrect,2) #drawing rect over coin
    #pygame.draw.rect(screen,crimson,drect)
    screen.blit(nflare,(xpos,280))#t tpos keeps updating
    screen.blit(text, text_rect)  #drawing score text
    screen.blit(ctext, ctext_rect) #drawing coins score text
    screen.blit(ncoin,(cxpos,cypos))    #draw coin 
      #update anim
    #screen.blit(smain,(0,0))
    #screen.blit(back_button,(310,250))  #diabled until game ligic is done
    #screen.blit(tog_button,(380,180))
    #screen.blit(indi,(310,190))
    #pygame.draw.rect(screen,crimson,srect,2)
    #pygame.draw.rect(screen,crimson,backrect,2)
    screen.blit(nmain,(0,0))
    pygame.draw.rect(screen,white,mrect,2)
    screen.blit(ngov,(0,0))
    screen.blit(logo_s,(0,0))


    text_surface = base_font.render(user_text, True, (255, 255, 255)) 
	
	# render at position stated in arguments 
    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5)) 
	
	# set width of textfield so that text cannot get 
	# outside of user's text input 
    input_rect.w = max(100, text_surface.get_width()+10)
    pygame.draw.rect(screen, color, input_rect) 
    

   
         
    pygame.display.flip()  #used to update display no drawing can occur without this method
pygame.quit()
        
