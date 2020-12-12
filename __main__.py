import pygame, time, portativnaq_computer as port

charon = True
print(pygame.font.get_fonts())
SCREENY = 700
pygame.init()
qwereschet2 = 0
qwereschet = 0
pygame.key.set_repeat(10)
pygame.mixer.music.load("cat soung/did.mp3")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.5)
knock=pygame.mixer.Sound("cat soung/knock.wav")
gol=pygame.mixer.Sound("cat soung/gol.wav")
screen = pygame.display.set_mode([1000, SCREENY])
schet = pygame.font.SysFont("consolas", 100, 0, 0)
were = pygame.Rect(100, 277, 50, 400)
were2 = pygame.Rect(800, 277, 50, 400)
qw = pygame.Rect(500, 577, 40, 40)
speedx = 7
speedy = 7
while 1 == 1:
    time.sleep(1 / 90)
    ask = pygame.key.get_pressed()
    # верх
    if ask[pygame.K_w] == 1:
        were.y -= 4
    # вниз
    if ask[pygame.K_s] == 1:
        were.y += 4
    if ask[pygame.K_a] == 1:
        were.x -= 3
    if ask[pygame.K_d] == 1:
        were.x += 3
    # верх2
    if ask[pygame.K_UP] == 1:
        were2.y -= 4
    # вниз2
    if ask[pygame.K_DOWN] == 1:
        were2.y += 4
    if ask[pygame.K_LEFT] == 1:
        were2.x -= 3
    if ask[pygame.K_RIGHT] == 1:
        were2.x += 3
    if ask[pygame.K_SPACE] == 1:
        charon = True

    # обработка событий
    events = pygame.event.get()

    # движение квадрата
    if charon:
        qw.x += speedx
        qwere = qw.colliderect(were)
        if qwere == 1:
            speedx,speedy=port.ugol(qw,were)
            qw.left = were.right
            knock.play()
        qwere = qw.colliderect(were2)
        if qwere == 1:
            speedx,speedy=port.ugol(qw, were2)
            speedx=-speedx
            knock.play()
            qw.right=were2.left


        # движение вниз верх
        qw.y += speedy
        if qw.bottom >= SCREENY:
            speedy = -7
            knock.play()
        if qw.top <= 0:
            speedy = 7
            knock.play()



    #непробиваемая линия
    if were.right>=500:
        were.right=498
    if were2.left<=500:
        were2.left=502



    # счёт и голы
    if qw.left <= 0 or qw.right >= 1000:
        if qw.left <= 0:
            qwereschet += 1
            gol.play()
        if qw.right >= 1000:
            qwereschet2 += 1
            gol.play()
        qw.centerx = 500
        qw.centery = 577
        were.centery = 350
        were2.centery = 350
        were.centerx = 100
        were2.centerx = 800
        charon = False

    # рисуем кадр
    screen.fill([0, 0, 0])
    # were+= 1www
    pygame.draw.rect(screen, [5, 45, 255], were, 0)
    pygame.draw.rect(screen, [255, 58, 0], were2, 0)
    pygame.draw.line(screen,[255,255,255],[500, 0],[500,700],4)

    pygame.draw.circle(screen, [255, 0, 255], [qw.centerx, qw.centery], 20)
    schetr = schet.render(str(qwereschet) + ":" + str(qwereschet2), True, [0, 255, 0])
    schetwid=schetr.get_width()
    screen.blit(schetr, [500-schetwid/2, 50])
    pygame.display.flip()
