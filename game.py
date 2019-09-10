import  pygame
from random import *

cyan = (0,206,206) #valeur max =255.
white = (255,255,255)

pygame.init()

surfaceW = 1800
surfaceH = 1000
ballonW = 150
ballonH = 166
nuageW = 400
nuageH = 300

surface = pygame.display.set_mode((surfaceW,surfaceH))
pygame.display.set_caption("Mr balloon est la!!!")


img = pygame.image.load('balloon.png')
img_nuage01 = pygame.image.load('nuageGris.png')
img_nuage02 = pygame.image.load('NuageBlanc.png')

def nuages(x_nuage, y_nuage, espace):
    surface.blit(img_nuage01, (x_nuage, y_nuage))
    surface.blit(img_nuage02,(x_nuage,y_nuage+ nuageH +espace))


def ballon(x,y, image):
    surface.blit(image, (x,y))

def main():
    x=150
    y=200
    y_move=0

    x_nuage = surfaceW
    y_nuage = randint(10,10)
    espace = ballonH*3
    nuage_vitesse = 6

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over= True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_move = -5
            if event.type ==pygame.KEYUP :
                y_move = 5

        y += y_move

        surface.fill(cyan)
        ballon(x,y,img)

        nuages(x_nuage,y_nuage, espace)

        x_nuage -=nuage_vitesse


        if y>surfaceH -40 or y <-10:
            game_over = True

        if x_nuage < (-1*nuageW):
            #print('passing here?')
            x_nuage = surfaceW
            y_nuage = randint(-200,100)


        if x +ballonW > x_nuage + 40 :
            if y < y_nuage + nuageH  -50:
                if x - ballonW < x_nuage +nuageW -20 :
                    game_over = True

        if x +ballonW >x_nuage + 40 :
            if y +ballonH > y_nuage + nuageH + espace +50 :
                if x -ballonW < x_nuage+ nuageW - 20:
                    game_over = True


        pygame.display.update()


main()
pygame.quit()
quit() 
