import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

back = pygame.image.load("abcs.jpg")
new_size = (800, 500)
nback = pygame.transform.scale(back, new_size)

char_s = (71, 126)
char_images = [
    pygame.image.load("walk1.png").convert_alpha(),
    pygame.image.load("walk2.png").convert_alpha(),
    pygame.image.load("walk3.png").convert_alpha(),
    pygame.image.load("walk4.png").convert_alpha(),
    pygame.image.load("walk5.png").convert_alpha()
]

current_char_index = 0
current_char_image = char_images[current_char_index]

shot = pygame.mixer.Sound("gun.wav")

run = True
clock = pygame.time.Clock()
last_frame_time = pygame.time.get_ticks()

ANIMATION_SPEED = 0.2  # Adjust this value to control animation speed

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pygame.mixer.Sound.play(shot)

    pos = pygame.mouse.get_pos()
    xpos = pos[0]
    ypos = pos[1]

    current_time = pygame.time.get_ticks()
    delta_time = (current_time - last_frame_time) / 1000.0  # Convert milliseconds to seconds

    # Update animation frame based on delta time
    current_char_index = (current_char_index + ANIMATION_SPEED * delta_time) % len(char_images)
    current_char_image = char_images[int(current_char_index)]

    last_frame_time = current_time

    nchar = pygame.transform.scale(current_char_image, char_s)

    screen.fill((255, 255, 255))
    screen.blit(nback, (0, 0))
    screen.blit(nchar, (200, 200))
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
