import pygame
import sys

pygame.init()

BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

HEIGHT = 452
WIDTH = 800

BACKGROUND = pygame.display.set_mode((WIDTH, HEIGHT))

ImgBACKGROUND = pygame.image.load("fondo.jpg")

CLOCK = pygame.time.Clock()

Coordx1 = 50
Coordy1 = 256
coordx2 = 755
Coordy2 = 214
coordBallX = 400
coordBallY = 300

speedx = 0
speedy = 0
speedx1 = 0
speedy1 = 0
speedBallY = 2
speedBallx = 2

while True:
    BACKGROUND.blit(ImgBACKGROUND, [0, 0])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speedx = -2
            if event.key == pygame.K_RIGHT:
                speedx = 2
            if event.key == pygame.K_UP:
                speedy = -2
            if event.key == pygame.K_DOWN:
                speedy = 2

            if event.key == pygame.K_d:
                speedx1 = 2
            if event.key == pygame.K_a:
                speedx1 = -2
            if event.key == pygame.K_s:
                speedy1 = 2
            if event.key == pygame.K_w:
                speedy1 = -2

            if event.key == pygame.K_m:
                Coordx1 = coordx2
                Coordy1 = Coordy2
                coordx2 = 400
                Coordy2 = 200

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                speedx = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                speedy = 0
            if event.key == pygame.K_d or event.key == pygame.K_a:
                speedx1 = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                speedy1 = 0

    ball = pygame.draw.rect(BACKGROUND, WHITE, (coordBallX, coordBallY, 10, 10))

    # Игрок 1:
    Coordx1 += speedx
    Coordy1 += speedy
    # Игрок 2:
    coordx2 += speedx1
    Coordy2 += speedy1

    if coordBallY > 440 or coordBallY < 4:
        speedBallY *= -1

    if coordBallX > 784:
        speedBallx *= -1
        points = 'Игрок 1 очко'
        print(points)

    if coordBallX < 4:
        speedBallx *= -1
        points2 = 'Игрок 2 очко'
        print(points2)

    coordBallY += speedBallY
    coordBallX += speedBallx

    p1 = pygame.draw.rect(BACKGROUND, BLUE, (Coordx1, Coordy1, 25, 25))
    p2 = pygame.draw.rect(BACKGROUND, RED, (coordx2, Coordy2, 25, 25))

    if ball.colliderect(p1) or ball.colliderect(p2):
        speedBallx *= -1
        speedBallY *= -1

    # Игрок 1:
    if Coordx1 < 0:
        Coordx1 = 10
    if Coordy1 > 450:
        Coordy1 = 430
    if Coordy1 < 0:
        Coordy1 = 10
    if Coordx1 > 795:
        Coordx1 = 785

    # Игрок 2:
    if coordx2 < 0:
        coordx2 = 10
    if Coordy2 > 450:
        Coordy2 = 430
    if Coordy2 < 0:
        Coordy2 = 10
    if coordx2 > 795:
        coordx2 = 785

    if coordBallX == 795:
        coordBallX = 400
    if coordBallX == 5:
        coordBallX = 400

    pygame.display.update()
    pygame.display.flip()

    CLOCK.tick(60)
