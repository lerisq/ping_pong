from pygame import *
from random import*
font.init()
font1=font.Font(None,35)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image,player_x,player_y,size_x, size_y,player_speed):
        sprite.Sprite.__init__(self)
        self.image=transform.scale(image.load(player_image),(size_x, size_y))
        self.speed=player_speed
        self.rect =self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys=key.get_pressed()
        if keys[K_UP] and self.rect.y>5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y<450:
            self.rect.y += self.speed
    def update_1(self):
        keys=key.get_pressed()
        if keys[K_w] and self.rect.y>5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y<450:
            self.rect.y += self.speed


window=display.set_mode((700,500))
background=transform.scale(image.load('table.jpg'),(800,550))
player=Player('rocket.png',-50,250,100,200,10)
player1=Player('rocket.png',650,250,100,200,10)
ball=GameSprite('ball.png',300,300,50,50,10)


    clock.tick(FPS)
    display.update()
