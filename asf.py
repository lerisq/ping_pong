from pygame import *
from random import*
font.init()
font1=font.Font(None,35)


window=display.set_mode((700,500))
background=transform.scale(image.load('table.jpg'),(800,550))
player=Player('rocket.png',-50,250,100,200,10)
player1=Player('rocket.png',650,250,100,200,10)
ball=GameSprite('ball.png',300,300,50,50,10)


    clock.tick(FPS)
    display.update()