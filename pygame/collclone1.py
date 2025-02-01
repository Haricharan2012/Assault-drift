import pygame   #importing the pygame library/module
import random    #random range 
import sqlite3   #database
import pandas as pd  #dataframe :beacuse we can use dataframe to display data in table format
#import disp
#import musicpl
#import feed

#INITIALIZATION BLOCK
pygame.init()  # initialize all imported pygame modules.

#SETTING SCREEN-------------------------------------------------------------------------------------
SCREEN_WIDTH=800
SCREEN_HEIGHT=500 #SPECIFIES WINDOW WIDTH AND HEIGHT

screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) #CREATING a game window using a function
#----------------------------------------------------------------------------------------------------




gun_s=(200,200)   #new gun size

kew_size=(800,500)

play_size=(800,500)

coin=pygame.image.load("coin.png")   #loading coin image

#flare=pygame.image.load("flare.png")
bomb_s=(50,50)                          #coin size
ncoin=pygame.transform.scale(coin,bomb_s)   #scaling the coin
flare_s=(80,80)                             #size of the flare
#nflare=pygame.transform.scale(flare,flare_s)


#ngun=pygame.transform.scale(gun,gun_s)  #to change size of gun image (gun_s is new var having widht=200,height=200)


#ENEMIES-------------------------------------------------------------------
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
#---------------------------------------------------------------------------





#rectangle for character

#colors------------------
white=(255,255,255) 
BLACK = (0, 0, 0)
orange=(255, 165, 0)
crimson=(220, 20, 60)
Yellow=(255, 255, 0)
#------------------------


#scores----------------
score=0  #game score 
cscore=0 #coins
#----------------------

#speed-----------------
speed=0
sspeed=0
#----------------------

#text = font.render("score: " + str(score), True, BLACK)

#positions --------------------------------------------------
kpos=0      #ypos of enemy1
cypos=0     #coin y position
cxpos=200   #coin x position
lpos=150 #for char2
#-------------------------------------------------------------


lvlwidth=800
lvlheight=500

#screens--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Game screen
back=pygame.image.load("abcs.jpg")  #background image
#gun=pygame.image.load("GUN.png")  #gun 
new_size=(800,500)     #new bg size
nback=pygame.transform.scale(back,new_size) #to change size of background image we use "pygame.transform.scale(back,new_size)" here "back" is the bg image and "new_size" is a variable which has new size width=800 height=500 it is assigned to new var nback 


#mainmenu background
main=pygame.image.load("new_mainmenu.png")
nmain=pygame.transform.scale(main,new_size)
nwidth=nmain.get_width() #main menu width
nheight=nmain.get_height()  #main menu height

#test screen
smain=pygame.image.load("test.jpeg")
snmain=pygame.transform.scale(smain,kew_size)
swidth=snmain.get_width() #retriving width 
sheight=snmain.get_height()  #retrieving height 
back_button=pygame.image.load("button-new_back.png")
nback_button=pygame.transform.scale(back_button,(150,30))
on_toggle=pygame.image.load("on_butt.png")
non_toggle=pygame.transform.scale(on_toggle,(102,47))
on_text=pygame.image.load("on_text.png")
non_text=pygame.transform.scale(on_text,(69,33))
off_toggle=pygame.image.load("off_butt.png")
noff_toggle=pygame.transform.scale(off_toggle,(102,47))
off_text=pygame.image.load("off_text.png")
noff_text=pygame.transform.scale(on_text,(69,33))
##player_enter=pygame.image.load("player_enter.jpg")
##nplayer_enter=pygame.transform.scale(player_enter,play_size)
##tog_button=pygame.image.load("tog_button.png")
##indi=pygame.image.load("on_text.png")


credit=pygame.image.load("credits.png")
ncredit=pygame.transform.scale(credit,(800,500))

#level select screen
level_sel=pygame.image.load("level_menu.png")
nlevel_sel=pygame.transform.scale(level_sel,(lvlwidth,lvlheight))

on_toggle_w=on_toggle.get_width()    #width of toggle
on_toggle_h=on_toggle.get_height()  #height of toggle

bwidth=back_button.get_width()  #width of backbutton
bheight=back_button.get_height() #height of backbutton

off_toggle_w=off_toggle.get_width()
off_toggle_h=off_toggle.get_height()



#logoscreen
logo_s=pygame.image.load("logo3.png")
lowidth=logo_s.get_width() #main menu width
loheight=logo_s.get_height()  #main menu height
nlogo_s=pygame.transform.scale(logo_s,(new_size))

#player input screen
plscreen=pygame.image.load("playerinput.png")
nplscreen=pygame.transform.scale(plscreen,(new_size))
plwidth=nplscreen.get_width()
plheight=nplscreen.get_height()


#leaderboard
lbb=pygame.image.load("lbimg.png")



#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#rectangles---------------------------------------------------------------
#rect for main
mrect=pygame.Rect(120,85,120,30)
#rect for submain
torect=pygame.Rect(380,180,on_toggle_w,on_toggle_h)
backrect=pygame.Rect(310,250,bwidth,bheight)
orect=pygame.Rect(380,180,off_toggle_w,off_toggle_h)
##srect=pygame.Rect(380,180,twidth,theight)  #rect created upon toggle button
##backrect=pygame.Rect(310,250,bwidth,bheight) #rect created upon backbutton


new_rect=pygame.Rect(380,180,0,0)


credit_rect=pygame.Rect(325,315,bwidth,bheight)

credit_back=pygame.image.load("button-new_back.png")
ncredit_back=pygame.transform.scale(credit_back,(150,30))
credit_back_rect=pygame.Rect(325,415,150,30)

mrect=pygame.Rect(800/4+120,500//4+85,150,30)
mscrect=pygame.Rect(800/4+120,500//4+140,150,30)

#rect for game over
lrect=pygame.Rect(798,0,3,SCREEN_HEIGHT)
rrect=pygame.Rect(0,0,1,800)

#rect for coin regen
trect=pygame.Rect(10,1,SCREEN_WIDTH,1)
drect=pygame.Rect(10,350,SCREEN_WIDTH,20)




#rect for level select--
lv2rect=pygame.Rect(-280,155,240,150)  #lv2rect=pygame.Rect(280,155,240,150)
lv3rect=pygame.Rect(-280,155,240,150)




#rect for leaderboard button
lbutton=pygame.Rect(380,400,200,80)
pbutton=pygame.Rect(0,110,800,300)
#---------------------------------------------------------------------------



###cursor
pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)


#music----------------------------------------------------(mixer)is a music/sound module under pygame library-------(sound() is a method within that module)--------------------------------------------------------
variable_mus=("jung.wav")
shot=pygame.mixer.Sound("click.wav")  #loading gun sound
ching=pygame.mixer.Sound("coins.wav") #loading coin sounds
font = pygame.font.SysFont(None, 48) #font  size48
tshot=pygame.mixer.Sound("gun.wav")  #temp gunshot
button=pygame.mixer.Sound("click.wav")  #button sounds
gamemusic=pygame.mixer.Sound(variable_mus) #gamemusic
snow=pygame.mixer.Sound("snow.wav") 
gameover=pygame.mixer.Sound("over.wav") #gameover sound

# Setting the volume 
pygame.mixer.music.set_volume(0.2) 
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#char anim death-----------------------------
dead=pygame.image.load("die.png")
ndead=pygame.transform.scale(dead,(0,0))
copos=0
coypos=0
#--------------------------------------------


#char states------------------------
#charstaes1
charst1=pygame.image.load("mon1.png")
charst2=pygame.image.load("mon2.png")
charst3=pygame.image.load("mon3.png")
charst4=pygame.image.load("mon3.png")


#charstates2
kharst1=pygame.image.load("don1.png")
kharst2=pygame.image.load("don2.png")
kharst3=pygame.image.load("don3.png")
kharst4=pygame.image.load("don3.png")

#char states------------------------


gov_width=0
gov_height=0


gov=pygame.image.load("blank.png")
ngov=pygame.transform.scale(gov,(0,0))




#input box--------------------------------------
base_font = pygame.font.Font(None, 64) 
user_text = ''     #text which player has given
  
# create rectangle 
input_rect = pygame.Rect(270, 180, 280, 62) 
  
# color_active stores color(lightskyblue3) which 
# gets active when input box is clicked by user 
color_active = pygame.Color('lightskyblue3') 
  
# color_passive store color(chartreuse4) which is 
# color of input box. 
color_passive = pygame.Color('chartreuse4') 
color = color_passive 
  
active = False

#input box---------------------------------------


game_start=False
game_fail=False
level_change=False
lboard=False


#function outside the whileloop  could be used for db prototype----------------------------------------------------------------------------------------------

def super2():
    print("hello!")

def allowmovement():
                                 global tpos
                                 global c2pos
                                 tpos=tpos+1 #incrementing enemy1 position [left to right]
                                 c2pos=c2pos-1 #enemy 2 appears from the opposite side hence decrement  [right to left]




#------------------------------------------------------------------------------------------------------------------------------------------------------------
def sql_connect():
    global cscore
    global score
    global user_text
    global lboard
    global time
    mtime = time // 60
    name = user_text

    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('player_data.db')
        cursor = conn.cursor()

        # Create tables if they don't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS players (
                id INTEGER PRIMARY KEY,
                name TEXT,
                score INTEGER,
                coins INTEGER
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS player_times (
                id INTEGER PRIMARY KEY,
                name TEXT,
                time TEXT
            )
        ''')

        # Insert player data into the database
        cursor.execute("INSERT INTO players (name, score, coins) VALUES (?, ?, ?)", (name, score, cscore))
        cursor.execute("INSERT INTO player_times (name, time) VALUES (?, ?)", (name, mtime))

        # Commit the changes
        conn.commit()

        # Retrieve player data from the database
        cursor.execute("SELECT * FROM players ORDER BY score DESC LIMIT 8")
        players = cursor.fetchall()

        # Print the data (for debugging)
        for player in players:
            print(player)

        # Load data into a pandas DataFrame
        df = pd.read_sql_query("SELECT * FROM players ORDER BY score DESC", conn)
        print(df.head(5))

        # Set the leaderboard flag to True
        lboard = True

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        # Close the connection
        if conn:
            conn.close()
    #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# MAIN GAME BLOCK-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#GAMELOOP

run=True
while run:  #condition to check if game is running
#mouse,enmy1,enemy2 position------------------------------------------------------------------------
    pos=pygame.mouse.get_pos()   # variable position = position of mouse (x coordinate,y coordinate)
    xpos=pos[0] #xpos is a variable which contains only x cordinate from mouse pos
    ypos=pos[1] #ypos is a var which contains only y coordinate
##    tpos=tpos+1 #incrementing enemy1 position [left to right]
##    c2pos=c2pos-1 #enemy 2 appears from the opposite side hence decrement  [right to left]
#---------------------------------------------------------------------------------------------------
    if game_start:
        allowmovement()

    if game_fail:
        musicstop()
    
        
#collisions-----------------------------------------------------------------------------------
    charrect=pygame.Rect(tpos,kpos,100,100)  #rect encasing enemy1
    charrect2=pygame.Rect(c2pos,lpos,100,100) #rect encasing 2nd enemy
    coinrect=pygame.Rect(cxpos,cypos,50,50)  #rect encasing coin
    mcollide=mrect.collidepoint(pos)  #start button collision
    
##    bcollide=backrect.collidepoint(pos)
##    toncollide=torect.collidepoint(pos)
##    scollide=srect.collidepoint(pos)  #toggle collision
    bcollide=backrect.collidepoint(pos) #backbutton collision

    msccollide=mscrect.collidepoint(pos)
    #scollide=srect.collidepoint(pos)
    bcollide=backrect.collidepoint(pos)
    toncollide=torect.collidepoint(pos)
    ocollide=orect.collidepoint(pos)
    

    ootcollide=new_rect.collidepoint(pos)

    creditcollide=credit_rect.collidepoint(pos)

    credit_back_coll=credit_back_rect.collidepoint(pos)

    lbcoll=lbutton.collidepoint(pos)


    
    collision=charrect.collidepoint(pos)     #collision btw character rect and mouseclick
    collision2=charrect2.collidepoint(pos)  #collison btw c2 rect and mousepointer
    lvlcoll=lv2rect.collidepoint(pos)
    lvlcoll2=lv3rect.collidepoint(pos)
#----------------------------------------------------------------------------------------------

    

#coin loop------------------------------------------------    
    if(coinrect.y>300):      #if y position of coin is greater than 300
        cypos=cypos-1000    #coin ypos goes back to initial position 
        cxpos=random.randrange(200,500) #the x position is randomised
#---------------------------------------------------------

#enemy and rect collision--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #if(charrect.colliderect(lrect)):  #enemy & rightrect
    if(charrect.x==801):
                    print("works")
                    gov=pygame.image.load("gom.png")    #loads game over screen
                    gov_width=800
                    gov_height=500
                    ngov=pygame.transform.scale(gov,(gov_width,gov_height)) #scale gameover screen
                    game_fail=True
            
       # musicstop()  #stop music
    else:
        game_fail=False
        
    #if(charrect2.colliderect(rrect)): #enemy2 &leftrect
    if(charrect2.x==-1):
             
            print("works")
            gov=pygame.image.load("gom.png")
            gov_width=800
            gov_height=500
            ngov=pygame.transform.scale(gov,(gov_width,gov_height))
            game_fail=True
        #musicstop()
    else:
        game_fail=False
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



        
#level change--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------    
    if(score==10):
        back=pygame.image.load("snow.png")                               # loading 2nd image and updating nback
        nback=pygame.transform.scale(back,new_size)                      #scaling it
        #gamemusic=pygame.mixer.stop()
        variable_mus=("snow.wav")
        replace()                                                        #replacing enemy image with another using function to replace all the character states
        levelsel()
        #ngun=pygame.transform.scale(gun,(50,50))
        #gamemusic=snow
    elif(score==20):
        back=pygame.image.load("desert.png")                            #loading 3rd image 
        nback=pygame.transform.scale(back,new_size)                     #update size
        #gamemusic=pygame.mixer.sound("lvl2.wav")
        lvlwidth=800
        lvlheight=500
        levelsel()
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


    coinre=pygame.Rect.colliderect(drect,coinrect)
    
    coincoll=coinrect.collidepoint(pos)      #collision btw coin rect and mouseclick

#drawtext---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    text = font.render("Score: " + str(score), True, crimson)  #display score on screen
    ctext= font.render("Coins: " +str(cscore), True,orange)    #display no of coins on screen
    pltext= font.render(user_text, True,crimson)
    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    cypos=cypos+1                   #coinpos y axis  (increasing)
    time=pygame.time.get_ticks()/5                              #from the time game stated counting in milliseconds 1-3000
#enemy animation/movement-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if(not collision):
        if(time%2==0):
            char=charst1
            nchar=pygame.transform.scale(char,char_s)
            
        elif(time%5==0):
            charst2
            nchar=pygame.transform.scale(char,char_s)
            
            
           
        elif(time%7==0):
            char=charst3
            nchar=pygame.transform.scale(char,char_s)
                        
        else:
            char=charst4
            nchar=pygame.transform.scale(char,char_s)
            tpos=tpos+speed  

        if(not collision2):
            if(time%2==0):
                char2=kharst1
                nchar2=pygame.transform.scale(char2,char_s)
            elif(time%5==0):
                char2=kharst2
                nchar2=pygame.transform.scale(char2,char_s)
            elif(time%7==0):
                char2=kharst3
                nchar2=pygame.transform.scale(char2,char_s)
            else:
                char2=kharst4
                nchar2=pygame.transform.scale(char2,char_s)
                c2pos=c2pos-sspeed
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#all events handeled here like(keypress,keydown,mouseclick etc)------------------------------------------------------------------------------------------------------------------           
    for event in pygame.event.get():
        
        if event.type==pygame.MOUSEMOTION:
     
                                           #event handler checks for events
            pygame.MOUSEMOTION=ngun.set_palette
        if event.type == pygame.KEYDOWN: 
  
            # Check for backspace 
            if event.key == pygame.K_BACKSPACE: 
  
                # get text input from 0 to -1 i.e. end. 
                user_text = user_text[:-1] 
  
            # Unicode standard is used for string 
            # formation 
            else: 
                user_text += event.unicode


            if event.key == pygame.K_RSHIFT:
                super2()
                plinp()
                mrect=pygame.Rect(800/4+120,500//4+85,150,30)   #setting position of rectangle to button postion from random position!
            if event.key == pygame.K_SPACE:
                logoinp()


            if event.key == pygame.K_m:
                import musicpl
                musicpl.main()
                #pygame.mixer.stop()
                musicstop()

            if event.key == pygame.K_LCTRL:
                import feed
                feed.main()

            if event.key == pygame.K_LALT:
                 import disp
                 disp.main()
                
                

            #if event.key == pygame.K_DELETE:
                #sql_connect()
               
                
        if event.type==pygame.QUIT:            #if cross is pressed
            run==False                      #we exit the game so run =false
            pygame.quit()
          
        elif event.type==pygame.MOUSEBUTTONDOWN:   #if mousebutton is pressed
           # pygame.mixer.Sound.play(button)        #playsound
            gun=pygame.image.load("GUN2.png")     #gunn state change
            ngun=pygame.transform.scale(gun,gun_s)   #updating
            flare=pygame.image.load("flare.png")     #gunflare
            nflare=pygame.transform.scale(flare,flare_s)   #scaling

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
          
                
#start button----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------               
            
            if(nwidth==800 and nheight==500):
                gamemusic=pygame.mixer.Sound(variable_mus)
                if mcollide:
                    toncollide=False
                    ootcollide=False
                    nmain=pygame.transform.scale(main,(0,0))
                    backrect.width=bwidth
                    backrect.height=bheight
                    pygame.mixer.Sound.play(button)
                    shot=pygame.mixer.Sound("gun.wav") #changing the gun shot sound after the start button is pressed
                    #gamemusic=pygame.mixer.Sound("jung.wav")
                    gamemusic.play()
                    game_start=True
                    mrect.x=-300
                    nback_button=pygame.transform.scale(back_button,(0,0))
                    non_toggle=pygame.transform.scale(on_toggle,(0,0))
                    noff_toggle=pygame.transform.scale(off_toggle,(0,0))
                    non_text=pygame.transform.scale(on_text,(0,0))
                    noff_text=pygame.transform.scale(off_text,(0,0))
                    ncredit=pygame.transform.scale(credit,(0,0))
                    ncredit_back=pygame.transform.scale(credit_back,(0,0))
                    nmain=pygame.transform.scale(main,(0,0))
                    snmain=pygame.transform.scale(smain,(0,0))
                    mrect.width=0
                    mrect.height=0
                    mscrect.width=0
                    mscrect.height=0
                    backrect.width=0
                    backrect.height=0
                    torect.width=0
                    torect.height=0
                    orect.width=0
                    orect.height=0
                    credit_rect.width=0
                    credit_rect.height=0
                    credit_back_rect.width=0
                    credit_back_rect.height=0
                    new_rect=pygame.Rect(380,180,0,0)
                    
                if msccollide:
                    nmain=pygame.transform.scale(main,(0,0))
                    mrect.width=0
##                    mrect.height=0
                    backrect.width=bwidth
                    backrect.height=bheight
                    credit_rect.width=0
                    credit_rect.height=0


                if(lbcoll):
                      gov=pygame.image.load("lbimg.png")
                      ngov=pygame.transform.scale(gov,(800,500))
                      screen.fill((255,255,255))
                      sql_connect()
                      print("stupid")
                      shot.stop()
                      pygame.mixer.Sound.play(button)
                    
                        
                if toncollide:
                    torect.width=0
                    torect.height=0
                    non_toggle=pygame.transform.scale(on_toggle,(0,0))
                    noff_toggle=pygame.transform.scale(off_toggle,(102,47))
                    new_rect=pygame.Rect(380,180,on_toggle_w,on_toggle_h)
                    non_text=pygame.transform.scale(on_text,(0,0))
                    noff_text=pygame.transform.scale(off_text,(69,33))
                    credit_rect.width=0
                    credit_rect.height=0
                        
                if ootcollide:
                    non_toggle=pygame.transform.scale(on_toggle,(102,47))
                    new_rect=pygame.Rect(380,180,0,0)
                    torect.width=on_toggle_w
                    torect.height=on_toggle_h
                    non_toggle=pygame.transform.scale(on_toggle,(torect.width,torect.height))
                    noff_text=pygame.transform.scale(off_text,(0,0))
                    non_text=pygame.transform.scale(on_text,(69,33))
                    credit_rect.width=0
                    credit_rect.height=0
                                    
                if bcollide:
                    backrect.width=0
                    backrect.height=0
                    nmain=pygame.transform.scale(main,(800,500))
                    mrect.width=150
                    mrect.height=30
                    credit_rect.width=150
                    credit_rect.height=30

                if creditcollide:
                    toncollide=False
                    ootcollide=False
                    new_rect=pygame.Rect(380,180,0,0)
                    mrect.width=0
                    mrect.height=0
                    mscrect.width=0
                    mscrect.height=0
                    backrect.width=0
                    backrect.height=0
                    torect.width=0
                    torect.height=0
                    orect.width=0
                    orect.height=0
                    credit_back_rect.height=30
                    credit_back_rect.width=150
                    nback_button=pygame.transform.scale(back_button,(0,0))
                    non_toggle=pygame.transform.scale(on_toggle,(0,0))
                    noff_toggle=pygame.transform.scale(off_toggle,(0,0))
                    noff_text=pygame.transform.scale(off_text,(0,0))
                    non_text=pygame.transform.scale(on_text,(0,0))
                    snmain=pygame.transform.scale(smain,(0,0))
                    nmain=pygame.transform.scale(main,(0,0))
                    ncredit=pygame.transform.scale(credit,(800,500))
                        
                if credit_back_coll:
                    nmain=pygame.transform.scale(main,(800,500))
                    mrect.width=150
                    mrect.height=30
                    mscrect.width=150
                    mscrect.height=30
                    torect.width=on_toggle_w
                    torect.height=on_toggle_h
                    ncredit=pygame.transform.scale(credit,(0,0))
                    credit_back_rect.height=0
                    credit_back_rect.width=0
                    snmain=pygame.transform.scale(smain,(800,500))
                    nmain=pygame.transform.scale(main,(800,500))
                    noff_text=pygame.transform.scale(on_text,(69,33))
                    noff_toggle=pygame.transform.scale(off_toggle,(102,47))
                    non_text=pygame.transform.scale(on_text,(69,33))
                    non_toggle=pygame.transform.scale(on_toggle,(102,47))
                    nback_button=pygame.transform.scale(back_button,(150,30))

                

                    
                   

                    
#music settings button---------------------------------------------------------------------------------------------------------------------------------------------------------------------------                    
                    
                else:
##                    if scollide:
##                        tpos=-400      #reset enemy
##                        snmain = pygame.transform.scale(smain, (0, 0))
####                        srect.width=0 
####                        srect.height=0
##                        torect.width=0
##                        torect.height=0
                        
                        
 #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                        
                        
#backbutton----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                       
                        
##                    if bcollide:
##                        backrect.width=0
##                        backrect.height=0
##                        #nmain=pygame.transform.scale(main,(800,500))
##                        mrect.width=150
##                        mrect.height=30

                    pygame.mixer.Sound.play(shot)  #playing the gunshot sound
                    #gamemusic.stop()
                    

#level2 image collision (selecting level2 in level menu)------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                    if lvlcoll:
                        lv2rect.width=0
                        lv2rect.height=0
                        lv2rect.x=-300
                        level_change=False
                        print('dont touch me')
                        lvlwidth=0
                        lvlheight=0
                        shot.stop()
                        pygame.mixer.Sound.play(button)
                        gamemusic.play()

                    if lvlcoll2:
                        lv3rect.width=0
                        lv3rect.height=0
                        lv3rect.x=-300
                        level_change=False
                        print('dont touch me')
                        lvlwidth=0
                        lvlheight=0
                        shot.stop()
                        pygame.mixer.Sound.play(button)
                       
                       
                        
                        
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                     
                   
                    
                
                
            
                 
                
            #else:
                #shot.stop()
                
#coin collision-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------     
                
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
#coin------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

##            if(coinre):
##                
##                cypos=+400

                
      
            #if drect.colliderect(coinrect):
                #cypos=cypos-1000
                

                
                
                
#enemy and gunshot collision---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                
            if(collision):                                   #enemy collision
                char=pygame.image.load("explo.png")
                nchar=pygame.transform.scale(char,char_s)   #scale charater
                tpos=random.randrange(-2000,-500)            #randomize position
                score=score+1                                #increment score after shooting
                kpos=random.randrange(5,290)  #y pos of char
                pygame.SYSTEM_CURSOR_HAND                    #change cursor to hand
                dead=pygame.image.load("explo.png")          #load explosion image
                ndead=pygame.transform.scale(dead,(100,100)) #scale explosion image
                copos=charrect.x                            #xpos of rect encasing character
                coypos=charrect.y                           #ypos of rect encasing character 
                speed=speed+1                        #increment speed value after getting shot to increase difficulty
         
            
                
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
                sspeed=sspeed+1

            
                
          
     
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------      

                
               # pygame.mixer.Sound.play(shot)
                #shot=tshot
             
        

            
            
#not shot ,not dead--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
           
        else:
            gun=pygame.image.load("GUN.png")
            ngun=pygame.transform.scale(gun,gun_s)
            flare=pygame.image.load("blank.png")
            nflare=pygame.transform.scale(flare,flare_s)
            dead = pygame.image.load("blank.png")
            ndead = pygame.transform.scale(dead, (100, 100))

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------     
        
               


            
    
                                                               #play gunshot sound
    text_rect = text.get_rect()  #rect for string score
    ctext_rect=ctext.get_rect() #rect for string coins
    pltext_rect=pltext.get_rect() #playertext
  
    # Center the text
    text_rect.center = (SCREEN_WIDTH-80, SCREEN_HEIGHT-480)
    ctext_rect.center =(SCREEN_WIDTH-80, SCREEN_HEIGHT-440)
    pltext_rect.center=(600,20)
    # Draw the text onto the screen
     
#DRAW GAME--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                                  
    screen.fill((255,255,255))  #fills the screen with white color
    screen.blit(smain,(0,0))  #music screen
    #pygame.draw.rect(screen,crimson,srect,2)#toggle
    #pygame.draw.rect(screen,white,backrect,2)#back 
    screen.blit(nback,(0,0))   #bilt means to draw on certain coordinates here we are drawing nback(bg) which has the altered size
    screen.blit(ngun,(xpos,300)) #we are drawing ngun(gun) on x position of mouse and y is set to 300 so as to lock it from moving it wont follow of mouse
    #pygame.draw.rect(nchar,white,charrect)  #drawing rect

    pygame.draw.rect(screen,crimson,lrect) #rects for left and right side of screen
    
    pygame.draw.rect(screen,crimson,rrect) #rects for left and right side of screen

    pygame.draw.rect(screen,crimson,trect)  #up and down rect

      #up and down rect
   
    screen.blit(ndead,(copos,coypos))  #display death at position of shooting              
    screen.blit(nchar2,(c2pos,lpos))
    #pygame.draw.rect(screen,white,charrect2,2) #rect over char2
    screen.blit(nchar,(tpos,kpos)) #200
    #pygame.draw.rect(screen,white,charrect,2) #drawing rect over character 
    #pygame.draw.rect(screen,white,coinrect,2) #drawing rect over coin
    screen.blit(nflare,(xpos,280))#t tpos keeps updating

    
#scores and details----------------------------------------------------------------
    screen.blit(text, text_rect)  #drawing score text
    screen.blit(ctext, ctext_rect) #drawing coins score text
    screen.blit(pltext, pltext_rect) #player text?

    
#changing levels--------------------------------------------------------------------------------
    if level_change:
        nlevel_sel=pygame.transform.scale(level_sel,(lvlwidth,lvlheight)) #level select screen
        screen.blit(nlevel_sel,(0,0)) 
        game_start=False                 
        #pygame.draw.rect(screen,crimson,lv2rect,2)
        #pygame.draw.rect(screen,crimson,lv3rect,2) #level3 select
        lv2rect.x=280  #return to level2 image position
        lv3rect.x=280+280
        
#------------------------------------------------------------------------------------------------      

    
    
    screen.blit(ncoin,(cxpos,cypos))    #draw coin
    #screen.blit(lvlslc,(0,0))
    
      #update animpygame.mixer.music.pause()
    
    #screen.blit(back_button,(310,250))  #diabled until game ligic is done
    #screen.blit(tog_button,(380,180))
    #screen.blit(indi,(310,190))
    
    screen.blit(ncredit,(0,0))
    screen.blit(ncredit_back,(325,415))

    screen.blit(snmain,(0,0))
    screen.blit(non_text,(310,190))
    screen.blit(noff_text,(310,190))
    screen.blit(nback_button,(310,250))
    screen.blit(noff_toggle,(380,180))
    screen.blit(non_toggle,(380,180))
    screen.blit(nmain,(0,0))  #display mainmenu 
    pygame.draw.rect(screen,white,mrect,2)
    screen.blit(ngov,(0,0))
    if(gov_width==800 and gov_height==500):
               text = font.render("Score: " + str(score), True, crimson)  #display score on screen
               ctext= font.render("Coins: " +str(cscore), True,orange)    #display no of coins on screen
               pltext= font.render(user_text, True,crimson)
	
               text_rect.center = (380,280)
               ctext_rect.center =(380,330)
               pltext_rect.center=(380,220)

               screen.blit(text, text_rect)  #drawing score text
               screen.blit(ctext, ctext_rect) #drawing coins score text
               screen.blit(pltext, pltext_rect) #player text?
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
    if lboard:
        #musicstop()
        pygame.mixer.stop()
        row_height = 40  # Increased from 30 to 40 for more spacing
        try:
            conn = sqlite3.connect('player_data.db')
            df = pd.read_sql_query("SELECT * FROM players ORDER BY score DESC LIMIT 5", conn)

            # Draw the leaderboard background
            pygame.draw.rect(screen, white, pbutton)

            # Display the header
            header_text = "Name      Score   Coins"
            header_surface = font.render(header_text, True, crimson)
            screen.blit(header_surface, (210, 120))

            # Display player data (only 5 rows)
            for idx, row in df.iterrows():
                name_text = f"{row['name']}"
                score_text = f"{row['score']}"
                coins_text = f"{row['coins']}"

                name_surface = font.render(name_text, True, crimson)
                score_surface = font.render(score_text, True, crimson)
                coins_surface = font.render(coins_text, True, crimson)

                # Calculate y position with increased spacing
                y_position = 150 + idx * row_height

                # Display text at the calculated y position
                screen.blit(name_surface, (210, y_position))
                screen.blit(score_surface, (400, y_position))
                screen.blit(coins_surface, (510, y_position))

        except sqlite3.Error as e:
            print(f"SQLite error: {e}")
        finally:
            if conn:
                conn.close()
        
       



#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            
   #gameover screen
    #screen.blit(lboard,(250,40))
    if game_fail:

           
         

           #lbutton.x=320
           pygame.draw.rect(screen,crimson,lbutton)
           gameover.play()
 
        

                                       
                       
                
          #screen.blit(text, ngov)  #drawing score text
          #screen.blit(ctext, ctext_rect) #drawing coins score text
          #screen.blit(pltext, pltext_rect)
        
    
    screen.blit(nplscreen,(0,0))
#drawing input box and text---------------------------------------------------------------   
    if active:
        color = color_active
                    
    else:
        color = color_passive 
              
    # draw rectangle and argument passed which should 
    # be on screen 
    pygame.draw.rect(screen, crimson, input_rect) 
  
    text_surface = base_font.render(user_text, True, white) 
      
    # render at position stated in arguments 
    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5)) 
      
    # set width of textfield so that text cannot get 
    # outside of user's text input 
    #input_rect.w = max(100, text_surface.get_width()+10)
#-----------------------------------------------------------------------------------------
    screen.blit(nlogo_s,(0,0))      #display logoscreen


    
#function to replace charater states after level1--------------------------------------------------------------------------------------------------------------------------------------------------------
    def replace():
        global charst1
        global charst2
        global charst3
        global charst4
        charst1=pygame.image.load("kon1.PNG")
        charst2=pygame.image.load("kon2.PNG")
        charst3=pygame.image.load("kon3.PNG")
        charst4=pygame.image.load("kon4.PNG")

        global kharst1
        global kharst2
        global kharst3
        global kharst4
        kharst1=pygame.image.load("kon1.PNG")
        kharst2=pygame.image.load("kon2.PNG")
        kharst3=pygame.image.load("kon3.PNG")
        kharst4=pygame.image.load("kon4.PNG")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  


#function for stoping music---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def musicstop():
        global gamemusic
        global gameover
        gamemusic=pygame.mixer.stop()
        gameover.play(1)
        
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def levelsel():
                global level_change
                level_change=True
                gamemusic=pygame.mixer.stop()

#function to close logoscreen and proceed to player input screen------------------------------------------------------------------------------------------------------------------------------------------- 
    def logoinp():
        global gamemusic
        global lowidth
        global loheight
        global nlogo_s
        global screen
        global white
        global text_surface
        global input_rect
##        lowidth=0
##        loheight=0
        
        white=(0,0,0,0)
        nlogo_s=pygame.transform.scale(logo_s,(0,0))
        #screen.blit(text_surface, (input_rect.x,200))
        #input_rect.width=0
        
        print("enter working")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#function to close player input screen ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def plinp():
        global input_rect
        global nplscreen
        input_rect.x=-300  #changing position of input rect after enter button is pressed(to make it dissapear
        input_rect.y=20
        input_rect.width=0  
        nplscreen=pygame.transform.scale(plscreen,(0,0)) #scaling player input screen to 0 width and 0 height.
        #mrect=pygame.Rect(800/4+120,500//4+85,150,30) 
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    

#function to allow movement--------------------------------------------------------------
 
       
         
    pygame.display.flip()  #used to update display no drawing can occur without this method
        
        

pygame.quit()
        
