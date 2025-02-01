
import pygame   # Importing the pygame library/module
import pandas as pd
import sqlite3

pygame.init()  # Initialize all imported pygame modules.

# Setting screen parameters
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080  # Specifies window width and height

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Creating a game window using a function

# Load and scale background image
back = pygame.image.load("min.png")
new_size = (1920, 1080)  # New background size
nback = pygame.transform.scale(back, new_size)

# Define colors
white = (255, 255, 255)
crimson = (220, 20, 60)

# Define button rectangle
pbutton = pygame.Rect(200, 100, 400, 800)  # Example position and size
gbutton = pygame.Rect(1000, 100, 400, 800)
ebutton=pygame.Rect(650,100,300,300)
fbutton=pygame.Rect(650,550,300,300)
kbutton=pygame.Rect(1450,100,800,400)
# Set font and row height
font = pygame.font.SysFont(None, 48)
row_height = 50  # Example row height

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Blit the background onto the screen
    screen.blit(nback, (0, 0))

    # Connect to the database and fetch player data
    conn = sqlite3.connect('player_data.db')
    df = pd.read_sql_query("SELECT * from players WHERE coins>50", conn)
    dfi = pd.read_sql_query("SELECT * from playtime WHERE time > 63", conn)
    dfj=pd.read_sql_query("SELECT * from leveldat WHERE id <4",conn)
    dfk=pd.read_sql_query("SELECT * from selected_songs",conn)
    dfl=pd.read_sql_query("SELECT * from feedback",conn)
    
    
    # Draw a rectangle for the leaderboard
    pygame.draw.rect(screen, white, pbutton)
    pygame.draw.rect(screen, white, gbutton)
    pygame.draw.rect(screen,white,ebutton)
    pygame.draw.rect(screen,white,fbutton)
    pygame.draw.rect(screen,white,kbutton)
    
    
    # Display the header text
    ttext = f"Name      Score   Coins"
    ttext_surface = font.render(ttext, True, crimson)
    screen.blit(ttext_surface, (210, 120))
    
    # Display the player data
    for idx, row in df.iterrows():
        text = f"{row['name']}"                   
        text_surface = font.render(text, True, crimson)
        screen.blit(text_surface, (210, 150 + idx * row_height))

        stext = f"{row['score']}"
        stext_surface = font.render(stext, True, crimson)
        screen.blit(stext_surface, (400, 150 + idx * row_height))

        otext = f"{row['coins']}"
        otext_surface = font.render(otext, True, crimson)
        screen.blit(otext_surface, (510, 150 + idx * row_height))



         # Display the header text
    dtext = f"Id           name     Time"
    dtext_surface = font.render(dtext, True, crimson)
    screen.blit(dtext_surface, (1040, 120))
    
    # Display the player data
    for idx, row in dfi.iterrows():
        text = f"{row['id']}"                   
        text_surface = font.render(text, True, crimson)
        screen.blit(text_surface, (1040, 150 + idx * row_height))

        stext = f"{row['name']}"
        stext_surface = font.render(stext, True, crimson)
        screen.blit(stext_surface, (1150, 150 + idx * row_height))

        otext = f"{row['time']}"
        otext_surface = font.render(otext, True, crimson)
        screen.blit(otext_surface, (1320, 150 + idx * row_height))

    
         # Display the header text
    xtext = f"Id     name     level"
    xtext_surface = font.render(xtext, True, crimson)
    screen.blit(xtext_surface, (660, 120))
    
    # Display the player data
    for idx, row in dfj.iterrows():
        text = f"{row['id']}"                   
        text_surface = font.render(text, True, crimson)
        screen.blit(text_surface, (660, 150 + idx * row_height))

        stext = f"{row['name']}"
        stext_surface = font.render(stext, True, crimson)
        screen.blit(stext_surface, (720, 150 + idx * row_height))

        otext = f"{row['lvlcompleted']}"
        otext_surface = font.render(otext, True, crimson)
        screen.blit(otext_surface, (880, 150 + idx * row_height))


             # Display the header text
    ztext = f"selected_songs"
    ztext_surface = font.render(ztext, True, crimson)
    screen.blit(ztext_surface, (660, 580))
    
    #Display the player data
    for idx, row in dfk.iterrows():
        text = f"{row['song_selected']}"                   
        text_surface = font.render(text, True, crimson)
        screen.blit(text_surface, (660, 620 + idx * row_height))


    #display data
    ztext = f"id     name    comments"
    ztext_surface = font.render(ztext, True, crimson)
    screen.blit(ztext_surface, (1470, 100))
    
    for idx, row in dfl.iterrows():
        text = f"{row['id']}"                   
        text_surface = font.render(text, True, crimson)
        screen.blit(text_surface, (1470, 150 + idx * row_height))

        stext = f"{row['name']}"
        stext_surface = font.render(stext, True, crimson)
        screen.blit(stext_surface, (1580, 150 + idx * row_height))

        otext = f"{row['comments']}"
        otext_surface = font.render(otext, True, crimson)
        screen.blit(otext_surface, (1700, 150 + idx * row_height))


        

    # Update the display to show the background image and text
    pygame.display.flip()

# Close the database connection
conn.close()

pygame.quit()
