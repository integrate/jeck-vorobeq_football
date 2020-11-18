import pygame, time,portativnaq_computer as port,random

charon=True
print(pygame.font.get_fonts())
SCREENY=700
pygame.init()
qwereschet2=0
qwereschet=0
pygame.key.set_repeat(10)
q = pygame.display.set_mode([1000, SCREENY])
schet=pygame.font.SysFont("comicsansms",100,0,0)
were = pygame.Rect(100,277,50,400)
were2=pygame.Rect(800,277,50,400)
qw=pygame.Rect(500,577,40,40)
speedx=port.ugol()
speedy=7
while 1 == 1:
    time.sleep(1 / 90)
    ask = pygame.key.get_pressed()
    #верх
    if ask[pygame.K_w] == 1:
        were.y -= 3
    #вниз
    if ask[pygame.K_s] == 1:
        were.y += 3
    # верх2
    if ask[pygame.K_UP] == 1:
        were2.y -= 3
    # вниз2
    if ask[pygame.K_DOWN] == 1:
        were2.y += 3
    if ask [pygame.K_SPACE] == 1:
        charon = True

    #обработка событий
    events = pygame.event.get()
   


    #движение квадрата
    if charon:
        qw.x += speedx
        qwere=qw.colliderect(were)
        if qwere == 1:
            speedx=+port.ugol()
        qwere = qw.colliderect(were2)
        if qwere == 1:
            speedx = -port.ugol()

    #движение вниз верх

        qw.y+=speedy
        if qw.bottom>=SCREENY:
            speedy = -7
        if qw.top<=0:
            speedy= 7

    #счёт и голы
    if qw.left <=0 or qw.right >=1000:
        if qw.left <= 0:
            qwereschet += 1
        if qw.right >= 1000:
            qwereschet2+=1
        qw.centerx = 500
        qw.centery = 577
        were.centery = 350
        were2.centery = 350
        charon=False



    # рисуем кадр
    q.fill([0, 0, 0])
        #were+= 1www
    pygame.draw.rect(q, [255, 255, 255], were, 0)
    pygame.draw.rect(q, [255, 255, 255], were2, 0)

    pygame.draw.circle(q,[255,255,255],[qw.centerx,qw.centery],20)
    schetr=schet.render(str(qwereschet)+":"+str(qwereschet2),True,[255,255,255])
    q.blit(schetr, [350, 50])
    pygame.display.flip()
