import sys, pygame, random
pygame.init()

pygame.display.set_caption('¡Pong!')

size = height, width = 500, 500
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
pspeed = 12

rpoints = 0
lpoints = 0

ballrect = pygame.Rect(bx, by, 5, 5)

win = pygame.display.set_mode(size)

def newRound():
    ballrect.left, ballrect.top = bx, by
    speed = [random.randint(1,5), random.randint(1,5)]
    pygame.time.delay(100)

run = True
while run:
    pygame.time.delay(32)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # check for input to move the paddles

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        if y1>0:
            y1 -= pspeed

    if keys[pygame.K_s]:
        if y1<height-rheight:
            y1 += pspeed

    if keys[pygame.K_UP]:
        if y2>0:
            y2 -= pspeed

    if keys[pygame.K_DOWN]:
        if y2<height-rheight:
            y2 += pspeed

    #move the ball

    ballrect = ballrect.move(speed)
    

    #check if the ball hit either of the paddles or went off the edge and change its velocity accordingly

    if ballrect.bottom >= height or ballrect.top <= 0:
        speed[1] = -speed[1]

    if ballrect.left <= x1+rwidth:
        if ballrect.top >= y1 and ballrect.bottom <= y1+rheight:
            speed[0] = -speed[0]
            
    if ballrect.right >= x2:
        if ballrect.top >= y2 and ballrect.bottom <= y2+rheight:
            speed[0] = -speed[0]
            
    if ballrect.right <= 0:
        newRound()
        rpoints += 1
        
    if ballrect.left >= width:
        newRound()
        lpoints += 1

    
    #draw everything    
    
    win.fill((0,0,0))
    for i in range(int(height/mlinheight)):
        pygame.draw.rect(win, (194, 191, 184), (width/2-mlinwidth/2, i*mlinheight*2+mlinheight/2, mlinwidth, mlinheight))

    pygame.draw.rect(win, (255,255,255), (x1, y1, rwidth, rheight))
    pygame.draw.rect(win, (255,255,255), (x2, y2, rwidth, rheight))
    pygame.draw.rect(win, (255,255,255), ballrect)


    pygame.display.flip()
    

pygame.quit()
sys.exit()

