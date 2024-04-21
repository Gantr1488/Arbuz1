#Создай собственный Шутер!

from pygame import *
from random import randint
win_1 = 700
win_2 = 500


window = display.set_mode((win_1,win_2))
display.set_caption('Сигма против Тайлера Дердана')
background = transform.scale(image.load('sigma.jpg'),(win_1,win_2))
clock = time.Clock()
FPS = 90
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
lost = 0
font.init()
score = 0
font1 = font.Font(None,40)
font2 = font.Font(None,80)



class  GameSprite(sprite.Sprite):
    def __init__(self,player_image , player_x , player_y ,size_x,size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 630:
            self.rect.x += self.speed
        
    def fire(self):
        bullet = Bullet('zz.png',self.rect.centerx,self.rect.top,15,20,-15)
        bullets.add(bullet)
               




class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > 450:
            self.rect.x = randint(80,620)
            self.rect.y = 0
            lost = lost + 1
class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
           self.kill()





sigma_1 = Enemy('sigma11.png',randint(30,620),0,85,50,randint(2,4))
sigma_2 = Enemy('sigma11.png',randint(30,620),0,85,50,randint(2,4))
sigma_3 = Enemy('sigma11.png',randint(30,620),0,85,50,randint(2,4))
sigma_4 = Enemy('sigma11.png',randint(30,620),0,85,50,randint(2,4))
sigma_5 = Enemy('sigma11.png',randint(30,620),0,85,50,randint(2,4))

taler = Player('sigma22.png',300,420,65,50,10)

bullets = sprite.Group()

monsters = sprite.Group()
monsters.add(sigma_1)
monsters.add(sigma_2)
monsters.add(sigma_3)
monsters.add(sigma_4)
monsters.add(sigma_5)

finish = False   
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
               taler.fire()
        
    sprite_list = sprite.groupcollide(monsters,bullets,True,True)
    for el in sprite_list:
        score += 1
        sigma_1 = Enemy('sigma11.png',randint(30,620),0,85,50,randint(2,3))
        monsters.add(sigma_1)
   
    if finish != True:
        


        

        window.blit(background,(0,0))
        
    
    
        taler.update()
        taler.reset()

        monsters.update()
        monsters.draw(window)

        bullets.update()
        bullets.draw(window)
    
        if score >= 15:
            text_win  = font2.render('YOU WON',1,(116, 122, 48))
            window.blit(text_win,(240,210))
            finish  =True


        if lost >= 2:
            text_lose = font2.render('YOU LOSE',1,(237, 28, 101))
            window.blit(text_lose,(240,210))
            finish = True

        text_lose = font1.render('Пропущено:' + str(lost),1,(77, 28, 237))
        text_score = font1.render('Счёт:'+ str(score),1,(77, 28, 237))

        window.blit(text_lose,(20,20))
        window.blit(text_score,(20,47))

        display.update()
        clock.tick(FPS)






