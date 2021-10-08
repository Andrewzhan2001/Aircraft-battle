import pygame
import sys
import random
from pygame import *
import time
import os

game_folder = os.path.dirname(os.path.realpath(sys.argv[0]))
os.chdir(game_folder)


class bullet1(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("images\\bullet1.png").convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.center = position
        self.rect.top=self.rect.top-50
        self.speed=[0,-14]


    def move(self):
        self.rect=self.rect.move(self.speed)



class myplane(pygame.sprite.Sprite):
    def __init__(self,image2):
        position=240,500
        pygame.sprite.Sprite.__init__(self)
        self.image=image2
        self.rect=self.image.get_rect()
        self.rect.center = position
        


    def move_left(self):
        self.speed=[-10,0]
        if self.rect.left<=0:
            self.rect.left=0
        else:
            self.rect=self.rect.move(self.speed)
    def move_right(self):
        self.speed=[10,0]
        if self.rect.left>=480-102:
            self.rect.left=480-102
        else:
            self.rect=self.rect.move(self.speed)
    def move_up(self):
        self.speed=[0,-10]
        if self.rect.top<=0:
            self.rect.top=0
        else:
            self.rect=self.rect.move(self.speed)
    def move_down(self):
        self.speed=[0,10]
        if self.rect.top>=700-126:
            self.rect.top=700-126
        else:
            self.rect=self.rect.move(self.speed)



class theirplane(pygame.sprite.Sprite):
    def __init__(self,speed):
        pygame.sprite.Sprite.__init__(self)
        x=random.randint(50,450)
        
        position=[x,-50]
        self.image=pygame.image.load("images\\enemy1.png").convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.center = position
        self.speed=speed
    def move(self):
        self.rect=self.rect.move(self.speed)


class theirplane2(pygame.sprite.Sprite):
    def __init__(self,speed):
        pygame.sprite.Sprite.__init__(self)
        x=random.randint(50,450)
        position=[x,-50]
        self.image=pygame.image.load("images\\enemy3_n2.png").convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.center = position
        self.speed=speed
    def move(self):
        self.rect=self.rect.move(self.speed)


class bulletsupply(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        x=random.randint(50,450)
        speed=[0,2]
        position=[x,-50]
        self.image=pygame.image.load("images\\bullet_supply.png").convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.center = position
        self.speed=speed
    def move(self):
        self.rect=self.rect.move(self.speed)


def mainscreen():
    planespeed=[0,4]
    bigplanespeed=[0,1]
    bgsize=width,height=480,700
    screen=pygame.display.set_mode(bgsize)
    bground=pygame.image.load("images\\background.png").convert()
    bgpos=bground.get_rect()
    pygame.display.set_caption('Andrew\'s game')
    mixer.music.play(loops=-1)
    image2=pygame.image.load("images\\me2.png").convert_alpha()
    image1=pygame.image.load("images\\me1.png").convert_alpha()
    mp=myplane(image2)
    
    group=pygame.sprite.Group()
    enemysmall=pygame.sprite.Group()
    enemybig=pygame.sprite.Group()
    bulletsupplygroup=pygame.sprite.Group()



    delay=0
    bulletdelay=0
    d=0
    

    state=True

    mpdestroy1=pygame.image.load("images\\me_destroy_1.png").convert_alpha()
    mpdestroy2=pygame.image.load("images\\me_destroy_2.png").convert_alpha()
    mpdestroy3=pygame.image.load("images\\me_destroy_3.png").convert_alpha()
    mpdestroy4=pygame.image.load("images\\me_destroy_4.png").convert_alpha()
    enemydestroy1=pygame.image.load("images\\enemy1_down1.png").convert_alpha()
    enemydestroy2=pygame.image.load("images\\enemy1_down2.png").convert_alpha()
    enemydestroy3=pygame.image.load("images\\enemy1_down3.png").convert_alpha()
    enemydestroy4=pygame.image.load("images\\enemy1_down4.png").convert_alpha()
    enemybigdestroy1=pygame.image.load("images\\enemy3_down1.png").convert_alpha()
    enemybigdestroy2=pygame.image.load("images\\enemy3_down2.png").convert_alpha()
    enemybigdestroy3=pygame.image.load("images\\enemy3_down3.png").convert_alpha()
    enemybigdestroy4=pygame.image.load("images\\enemy3_down4.png").convert_alpha()
    enemybigdestroy5=pygame.image.load("images\\enemy3_down5.png").convert_alpha()
    check=True
    numberplane=15

    score=0
    score2=0
    scorefont=pygame.font.Font("font\\font.ttf", 36)
    scorefont2=pygame.font.Font("font\\font.ttf", 45)
    white=(255,255,255)
    ddd=-10
    powerstate=True
    numberhit=0
    enemyhitstate=False
    while state:
        delay+=1
        if score%2000==0 and score!=score2:
            score2=score
            planespeed[1]=planespeed[1]+1  
            if planespeed[1]>8:
                planespeed[1]=8                        #速度
            numberplane=numberplane-4
            if numberplane<6:
                numberplane=6
            print(numberplane)
            if score%6000==0:
                bigplanespeed[1]=bigplanespeed[1]+1
                if bigplanespeed[1]>3:
                    bigplanespeed[1]=3
            

        bulletdelay+=1
        if delay%10==0:
            mp.image=image1
        if delay%10==5:
            mp.image=image2
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()

        screen.blit(bground,bgpos)
        if delay==ddd+300 and powerstate==False:
            poweroff.play()
            powerstate=True

        if delay%600==0:
            bulletsupply1=bulletsupply()
            bulletsupplygroup.add(bulletsupply1)
        if delay%1000==0:
            thebigplane=theirplane2(bigplanespeed)
            enemybig.add(thebigplane)

        if delay%numberplane==0:
            theplane=theirplane(planespeed)
            enemysmall.add(theplane)

        for bullet in group.sprites():
            bullet.move()
            screen.blit(bullet.image, bullet.rect.center) 



        for therbigplane in enemybig.sprites():
            therbigplane.move()
            if delay%2==0 and enemyhitstate==False:
                therbigplane.image=pygame.image.load("images\\enemy3_n2.png").convert_alpha()
            if delay%2==1 and enemyhitstate==False:
                therbigplane.image=pygame.image.load("images\\enemy3_n1.png").convert_alpha()
            screen.blit(therbigplane.image, therbigplane.rect)
            if check==True:
                h=delay
                print(h)
                check=False
            if therbigplane.rect.top>850:
                enemybig.remove(therbigplane)
            if pygame.sprite.spritecollideany(therbigplane,group):
                numberhit=numberhit+1
                pygame.sprite.spritecollide(therbigplane, group, powerstate)
                if numberhit==10:
                    therbigplane.image=therbigplane.image=pygame.image.load("images\\enemy3_hit.png").convert_alpha()
                    enemyhitstate=True
                if numberhit==20:
                    numberhit=0
                    enemybigdestroy.play()
                    enemyhitstate=False
                    time2=100
                    for xx in range(time2):
                        therbigplane.image=enemybigdestroy1   
                        screen.blit(therbigplane.image, therbigplane.rect)
                    
                    pygame.display.flip()
                    for xx1 in range(time2):
                        therbigplane.image=enemybigdestroy2     
                        screen.blit(therbigplane.image, therbigplane.rect)
                    
                    pygame.display.flip()
                    for xx2 in range(time2):
                        therbigplane.image=enemybigdestroy3   
                        screen.blit(therbigplane.image, therbigplane.rect) 
                    
                    pygame.display.flip()
                    for xx3 in range(time2):
                        therbigplane.image=enemybigdestroy4    
                        screen.blit(therbigplane.image, therbigplane.rect)
                    pygame.display.flip()
                    for xx4 in range(time2):
                        therbigplane.image=enemybigdestroy5    
                        screen.blit(therbigplane.image, therbigplane.rect)
                    pygame.display.flip()
                    for xx5 in range(time2):
                        enemybig.remove(therbigplane)
                    score+=1000
            scoretext=scorefont.render("Score:"+str(score),True,white)
           
            screen.blit(scoretext,(10,5))

            if pygame.sprite.collide_mask(mp,therbigplane):
                mpdestroy.play()
                mp.image=mpdestroy1
                screen.blit(mp.image, mp.rect)
                pygame.display.flip()
                pygame.time.wait(300)
                mp.image=mpdestroy2
                screen.blit(mp.image, mp.rect)
                pygame.display.flip()
                pygame.time.wait(300)
                mp.image=mpdestroy3
                screen.blit(mp.image, mp.rect)
                pygame.display.flip()
                pygame.time.wait(300)
                mp.image=mpdestroy4
                screen.blit(mp.image, mp.rect)
                pygame.display.flip()
                pygame.time.wait(300)
                with open("record.txt",mode='r+') as r:
                    readscore=str(r.read())
                    if readscore=='':
                        readscore=0
                    readscore=int(readscore)
                    r.close()
                with open("record.txt",mode='r+') as r:
                    if readscore<score:
                        r.truncate(0)
                        r.write(str(score))
                    r.close()
                with open("record.txt",mode='r+') as r:
                    readscore2=str(r.read())
                    r.close()
                
                readscoretext=scorefont2.render("Best score:"+str(readscore2),True,white)
                gameover(scoretext,readscoretext)
                
                state=False



        for therplane in enemysmall.sprites():
            
            therplane.move()
            screen.blit(therplane.image, therplane.rect)
            if check==True:
                d=delay
                print(d)
                check=False
            if pygame.sprite.spritecollideany(therplane,group):
                pygame.sprite.spritecollide(therplane, group, powerstate)
                enemydestroy.play()
                
                time=20
                for x in range(time):
                    therplane.image=enemydestroy1   
                    screen.blit(therplane.image, therplane.rect)
                for x1 in range(time):
                    therplane.image=enemydestroy2     
                    screen.blit(therplane.image, therplane.rect)
                for x2 in range(time):
                    therplane.image=enemydestroy3   
                    screen.blit(therplane.image, therplane.rect) 
                for x3 in range(time):
                    therplane.image=enemydestroy4    
                    screen.blit(therplane.image, therplane.rect)
                for x4 in range(time):
                    
                    enemysmall.remove(therplane)
                score+=100
            scoretext=scorefont.render("Score:"+str(score),True,white)
            screen.blit(scoretext,(10,5))

            if pygame.sprite.collide_mask(mp,therplane):
                mpdestroy.play()
                mp.image=mpdestroy1
                screen.blit(mp.image, mp.rect)
                pygame.display.flip()
                pygame.time.wait(300)
                mp.image=mpdestroy2
                screen.blit(mp.image, mp.rect)
                pygame.display.flip()
                pygame.time.wait(300)
                mp.image=mpdestroy3
                screen.blit(mp.image, mp.rect)
                pygame.display.flip()
                pygame.time.wait(300)
                mp.image=mpdestroy4
                screen.blit(mp.image, mp.rect)
                pygame.display.flip()
                pygame.time.wait(300)
                with open("record.txt",mode='r+') as r:
                    readscore=str(r.read())
                    if readscore=='':
                        readscore=0
                    readscore=int(readscore)
                    r.close()
                with open("record.txt",mode='r+') as r:
                    if readscore<score:
                        r.truncate(0)
                        r.write(str(score))
                    r.close()
                with open("record.txt",mode='r+') as r:
                    readscore2=str(r.read())
                    r.close()
                
                readscoretext=scorefont2.render("Best score:"+str(readscore2),True,white)
                gameover(scoretext,readscoretext)
                
                state=False
        if  pygame.sprite.spritecollide(mp,bulletsupplygroup,True):
            getpower.play()
            powerstate=False
            ddd=delay

        for bullet2 in bulletsupplygroup:
            bullet2.move()
            screen.blit(bullet2.image, bullet2.rect.center)   
        

        

        
        

                
                

        key=pygame.key.get_pressed()
        if key[K_j] and bulletdelay>4:
            bulletdelay=0
            b=bullet1(mp.rect.center)
            if powerstate==False:
                b.image=pygame.image.load("images\\bullet2.png").convert_alpha()
            if powerstate==True:
                b.image=pygame.image.load("images\\bullet1.png").convert_alpha()
            bulletsound.play()
            group.add(b)
        
        if key[K_w]:
            mp.move_up()
        if key[K_a]:
            mp.move_left()
        if key[K_s]:
            mp.move_down()
        if key[K_d]:
            mp.move_right()

       







        screen.blit(mp.image, mp.rect)
        
        pygame.display.flip() 
        pygame.time.Clock().tick(30)   

def gameover(scoretext,historyscore):
    pygame.mixer.music.stop()
    buttonsound = pygame.mixer.Sound('sound\\upgrade.wav')
    buttonsound.set_volume(0.05)
    bgover=pygame.image.load("images\\background.png")
    bgoverpos=bgover.get_rect()
    bgoversize=width,height=480,700
    screen=pygame.display.set_mode(bgoversize)
    pygame.display.set_caption('Gameover')
    
    while True:
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()

        immage1=pygame.image.load("images\\gameover.png")
        immage11=pygame.image.load("images\\gameover2.png")
        immage2=pygame.image.load("images\\again.png")
        immage22=pygame.image.load("images\\again2.png")
        button1=immage1
        button2=immage2
        button1pos=button1.get_rect()
        button1pos.center=[240,450]
        button2pos=button2.get_rect()
        button2pos.center=[240,500]
        mousepress=pygame.mouse.get_pressed()
        mousepos=pygame.mouse.get_pos()
        print(mousepos)
        
        if button1pos.left<mousepos[0]<button1pos.right and button1pos.top<mousepos[1]<button1pos.bottom:
            button1=immage11
            if mousepress[0]:
                sys.exit()
        else:
            button1=immage1
        if button2pos.left<mousepos[0]<button2pos.right and button2pos.top<mousepos[1]<button2pos.bottom:
            button2=immage22
            if mousepress[0]:
                buttonsound.play(1)
                mainscreen()
        else:
            button2=immage2
            
    
    
        
        screen.blit(bgover, bgoverpos)
        screen.blit(scoretext,(150,200))
        screen.blit(historyscore,(50,250))
        screen.blit(button1, button1pos)
        screen.blit(button2, button2pos)

        
        pygame.display.flip() 
         
        





pygame.init()
pygame.mixer.pre_init(44100,-16,2,128)
pygame.mixer.init()
pygame.mixer.music.load("sound\\game_music.wav")
pygame.mixer.music.set_volume(0.01)
bulletsound = pygame.mixer.Sound("sound\\bullet.wav")
bulletsound.set_volume(0.05)
enemydestroy = pygame.mixer.Sound("sound\\enemy1_down.wav")
enemydestroy.set_volume(0.05)
mpdestroy = pygame.mixer.Sound("sound\\enemy3_down.wav")
mpdestroy.set_volume(0.2)
enemybigdestroy = pygame.mixer.Sound("sound\\enemy2_down.wav")
enemybigdestroy.set_volume(0.05)
getpower = pygame.mixer.Sound("sound\\get_bullet.wav")
getpower.set_volume(0.2)
poweroff = pygame.mixer.Sound("sound\\get_bomb.wav")
poweroff.set_volume(0.2)
mainscreen()

        