import sys, pygame
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

pspeed = 12

win = pygame.display.set_mode(size)

run = True
while run:
    pygame.time.delay(32)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

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
    
    win.fill((0,0,0))
    for i in range(int(height/mlinheight)):
        pygame.draw.rect(win, (194, 191, 184), (width/2-mlinwidth/2, i*mlinheight*2+mlinheight/2, mlinwidth, mlinheight))

    pygame.draw.rect(win, (255,255,255), (x1, y1, rwidth, rheight))
    pygame.draw.rect(win, (255,255,255), (x2, y2, rwidth, rheight))


    pygame.display.flip()
    

pygame.quit()
sys.exit()

