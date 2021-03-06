import sys, pygame, random, time
pygame.init()

pygame.display.set_caption('¡Pong!')

size = height, width = 500, 500

win = pygame.display.set_mode(size)

def new_round(ballrect, bx, by):
    #center ball and assign it a new speed
    ballrect.left, ballrect.top = bx, by
    speed = [random.randint(1,5), random.randint(1,5)]
    pygame.time.delay(100)
    return speed

def make_text(message, position, color = (0,0,0), font_size = 32):

    font = pygame.font.Font('freesansbold.ttf', font_size)
    text = font.render(str(message), True, color)
    text_rect = text.get_rect()
    text_rect.center = (position)
    return text, text_rect



def button(button_x, button_y, button_width, button_height, color_active, color_inactive, msg, action = None):

    #rectangle for button and the text that goes on it
    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
    small_font = pygame.font.Font('freesansbold.ttf',16)
    button_text = small_font.render(msg, True, (0, 0, 0))
    button_text_rect = button_text.get_rect()
    button_text_rect.center = button_rect.center

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if button_rect.left < mouse[0] < button_rect.right and button_rect.bottom > mouse[1] > button_rect.top:
        pygame.draw.rect(win, color_active, button_rect)
        if click[0] and action:
            eval(action)
    else:
        pygame.draw.rect(win, color_inactive, button_rect)

    win.blit(button_text, button_text_rect)

def menu_loop():

    #where is the button
    button_width, button_height = width//5+10, height//10
    button_x, button_y = width//4-button_width//2, height//2-button_height//2
    button2_x, button2_y = width-width//4-button_width//2, height//2-button_height//2

    #text in menu
    text, text_rect = make_text('PyPong', (width//2, height//4), (255, 255, 255), 86)

    menu = True
    while menu:
        pygame.time.delay(32)
        win.fill((0,0,0))
        #check for user x-ing out of game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        button(button_x, button_y, button_width, button_height, (255,255,255), (192,192,192), 'Two Player', 'game_loop(False)')
        button(button2_x, button2_y, button_width, button_height, (255,255,255), (192,192,192), 'Vs. Computer', 'game_loop(True)')
        win.blit(text, text_rect)
        pygame.display.flip()




def game_loop(computer):

    rwidth = 10
    rheight = int(.15*height)

    mlinwidth = 5
    mlinheight = height/20

    x1 = 5
    y1 = height/2-rheight/2

    x2 = width-rwidth-5
    y2 = height/2-rheight/2

    bx = width/2-5/2
    by = height/2-5/2

    speed = [random.randint(1,5), random.randint(1,5)]
    collisions = 0
    pspeed = 12

    rpoints = 0
    lpoints = 0

    ballrect = pygame.Rect(bx, by, 5, 5)

    run = True
    while run:
        pygame.time.delay(32)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # check for input to move the paddles

        keys = pygame.key.get_pressed()

        # if playing vs computer then dont accept kb input for left paddle
        if not computer:
            if keys[pygame.K_w]:
                if y1>0:
                    y1 -= pspeed

            if keys[pygame.K_s]:
                if y1<height-rheight:
                    y1 += pspeed
        else:
            if ballrect.bottom > y1 + rheight//2:
                if y1<height-rheight:
                    y1 += pspeed//3
            elif ballrect.top < y1 + rheight//2:
                if y1>0:
                    y1 -= pspeed//3

        #input for right paddle
        if keys[pygame.K_UP]:
            if y2>0:
                y2 -= pspeed

        if keys[pygame.K_DOWN]:
            if y2<height-rheight:
                y2 += pspeed

        #move the ball

        ballrect = ballrect.move(speed)

        #speed the ball up after it has hit the paddle 3 times
        if collisions % 3 == 0 and collisions != 0:
            collisions = 0
            speed[0] -= 1

        #check if the ball hit either of the paddles or went off the edge and change its velocity accordingly

        if ballrect.bottom >= height or ballrect.top <= 0:
            speed[1] = -speed[1]

        if ballrect.left <= x1+rwidth:
            if ballrect.top >= y1 and ballrect.bottom <= y1+rheight:
                speed[0] = -speed[0]

        if ballrect.right >= x2:
            if ballrect.top >= y2 and ballrect.bottom <= y2+rheight:
                speed[0] = -speed[0]
                #count the number of times the ball has hit the paddle in order to speed it up after 3 hits
                collisions += 1

        if ballrect.right <= 0:
            speed = new_round(ballrect, bx, by)
            rpoints += 1

        if ballrect.left >= width:
            speed = new_round(ballrect, bx, by)
            lpoints += 1

        if lpoints > 4 or rpoints > 4:
            winner = lambda ls, rs: 1 if ls > rs else 2
            winning_player = winner(lpoints, rpoints)
            end_text, end_text_rect = make_text(f'Player {winning_player} wins!', (width//2, height//2), (255,255,255), 32)
            win.blit(end_text, end_text_rect)
            pygame.display.flip()
            time.sleep(3)
            run = False

        #text for scores
        lscore_text, lscore_text_rect = make_text(str(lpoints), (50,50), (255,255,255))
        rscore_text, rscore_text_rect = make_text(str(rpoints), (width-50,50), (255,255,255))

        #draw everything

        win.fill((0,0,0))
        for i in range(int(height/mlinheight)):
            pygame.draw.rect(win, (194, 191, 184), (width/2-mlinwidth/2, i*mlinheight*2+mlinheight/2, mlinwidth, mlinheight))

        pygame.draw.rect(win, (255,255,255), (x1, y1, rwidth, rheight))
        pygame.draw.rect(win, (255,255,255), (x2, y2, rwidth, rheight))
        pygame.draw.rect(win, (255,255,255), ballrect)
        win.blit(lscore_text, lscore_text_rect)
        win.blit(rscore_text, rscore_text_rect)

        pygame.display.flip()

menu_loop()
pygame.quit()
sys.exit()
