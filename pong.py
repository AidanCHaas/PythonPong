import pygame
pygame.init()

#Opens Window
screen = pygame.display.set_mode((2000,1500))
pygame.display.set_caption("Pong")

#Variablesws
doExit = False
p1x = 100
p1y = 1000
p2x = 1900
p2y = 1000
bx = 1000
by = 750
bvx = 20
bvy = 20
p1score = 0
p2score = 0
win = 0

#Clock
clock = pygame.time.Clock()

while not doExit: #Game Loop---------------------------------

    #Event Queue---------------------------
    clock.tick(60) #FPS
    for event in pygame.event.get(): #Did the player do something?
        if event.type == pygame.QUIT: #Did the player click close?
            doExit = True #Exit game loop
    #Game Logic----------------------------
    #Keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and p1y > 0:
        p1y-=15
    if keys[pygame.K_s] and p1y + 300 < 1500:
        p1y+=15
    if keys[pygame.K_o] and p2y > 0:
        p2y-=15
    if keys[pygame.K_l] and p2y + 300 < 1500:
        p2y+=15
    #Ball Movement
    bx += bvx
    by += bvy
    #Reflect Ball Off Side Walls of Screen
    if bx < 0 or bx + 20 > 2000:
        bvx *= -1
        if bx < 0:
            p1score += 1
            bx = 1000
        if bx + 20 > 2000:
            p2score += 1
            bx = 1000
    if by < 0 or by + 20 > 1500:
        bvy *= -1
    #Ball Paddle Reflection
    if bx < p1x + 70 and bx + 20 > p1x and by + 20 > p1y and by < p1y + 300:
        bvx *= -1
    if bx + 20 < p2x and bx > p2x - 70 and by + 20 > p2y and by < p2y + 300: 
        bvx *= -1
    #Win Condition
    if p1score is 9:
        doExit = True
    if p2score is 9:
        doExit = True
    #Render Section------------------------
    screen.fill((0,0,0)) #Clear to Color
    pygame.draw.rect(screen, (255, 255, 255), (p1x, p1y, 50, 300), 0)
    pygame.draw.rect(screen, (255, 255, 255), (p2x, p2y, -50, 300), 0)
    #Dsiplay Scores
    font = pygame.font.Font(None, 200)
    text = font.render(str(p1score), 1, (255, 255, 255))
    screen.blit(text, (10, 675))
    text = font.render(str(p2score), 1, (255, 255, 255))
    screen.blit(text, (1910, 675))
    pygame.draw.circle(screen, (255, 255, 255), (bx, by), 20, 0)
    pygame.display.flip() #Update the Screen
#End Game Loop-----------------------------------------------
pygame.quit() #C E A S E