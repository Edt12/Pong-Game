import sys
import time

import pygame
pygame.init()
clock = pygame.time.Clock()
#list of functions
def draw_rect():
    pygame.draw.rect(screen, red, player)
    pygame.draw.rect(screen, red, opponent)
    pygame.draw.ellipse(screen, red, ball)



#setting colour values
red = (255,0,0)
lightGrey = (255,255,255)


# screen setup
screen_width = (1200)
screen_height = (700)
screen = pygame.display.set_mode((screen_width, screen_height),pygame.RESIZABLE)


#setting colour valuesssss
red = (255,0,0)
lightGrey = (255,255,255)


#setting a score value and displaying it
player_score = 0
opponent_score = 0
game_font = pygame.font.Font("freesansbold.ttf",32)#font then size



background = pygame.image.load("spacebackground.png").convert_alpha()
pygame.mouse.set_visible(False)
pygame.display.set_caption('pong')


# set up player and opponentand  ball rect
opponent = pygame.Rect(screen_width-20,screen_height/2 - 70,10,140)
player = pygame.Rect(0+20,screen_height/2 ,10,140 )
ball = pygame.Rect(screen_width/2, screen_height/2,30, 30)
#last 2 values are width and height
surface = pygame.image.load('spacebackground.png').convert()
#defining player speed
player_speed = 0 #dont need x because only moving up and down


#defining speed of ball and opponents
ball_speed_x = 9
ball_speed_y = 9
opponent_speed =8
# defining clock
clock = pygame.time.Clock()

while True:
    #checks for screen size
    x,y = screen.get_size()
    screen_width = x
    screen_height = y
    # same for player
    player.y += player_speed
    pygame.display.flip()
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            # arrow key controls for player when key is pressed changes speed value to move it and when the key comes up it reverses it so the speed goes back to 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN or event.key == ord("s"):
                player_speed += 8
            if event.key == pygame.K_UP or event.key == ord("w"):
                player_speed -= 8
            #have to do for key up as well
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == ord("s") :
                player_speed -= 8
            if event.key == pygame.K_UP or event.key == ord("w"):
                player_speed += 8
    #speed of the ball is added to the balls x or y coordinates each time the loop runs
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Drawing the rects
    draw_rect()
#setting up collisons with edge of screen and other rects if ballor player collides with edge their speed is reversed
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1 #reverses velocity of the ball
    if ball.left <= 0:
        opponent_score+= 1
        ball.x = screen_width / 2
        ball.y = screen_height / 2
        ball_speed_x *= -1
        ball_speed_y *= -1
        if ball_speed_x < 11 and ball_speed_y < 11:
            ball_speed_x *= 1.1
            ball_speed_y *= 1.1

    if ball.right >= screen_width:
        ball.x = screen_width / 2;ball.y = screen_height / 2
        player_score += 1
        if ball_speed_x <11 and ball_speed_y <11:
            ball_speed_x *= 1.1
            ball_speed_y *= 1.1

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *=-1


    #keeping player from moving outside of window
    if player.top <= 0: #only need down and up due to player only moving along y axis
        player.top = 0#teleports player back but doesnt look like it due to it being by a small amount

    if player.bottom >= screen_height:
        player.bottom =screen_height
    #same for the opponent
    if opponent.top <= 0: #only need down and up due to player only moving along y axis
        opponent.top = 0#teleports player back but doesnt look like it due to it being by a small amount
#ai for opponent
    if opponent.centery < ball.y:
        opponent.top += opponent_speed
    if opponent.centery > ball.y:
        opponent.bottom -= opponent_speed
    #putting text over the top of background
    player_text = game_font.render(f'{player_score}', False, lightGrey)#have to put text above background otherwise goes behind
    opponent_text = game_font.render(f'{opponent_score}', False, lightGrey)
    # makes surface above background blit puts one surface on top of another
    screen.blit(player_text, (screen_width/2-30,screen_height/2))
    screen.blit(opponent_text, (screen_width/2+30, screen_height/2))
    if x or y != 1:
        opponent.x = screen_width-20

    clock.tick(60)
