import pygame
import random
pygame.init()
size=(700,600)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Travel in Space")
clock=pygame.time.Clock()
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
yellow=(255,255,0)
font=pygame.font.SysFont("Arial",25)
ship_image=pygame.image.load('Enterprise2.png').convert()
enShip_image=pygame.image.load('enemy_ship_image.png')
enShip_image1=pygame.image.load('enemy_ship_image1.png')
background_image=pygame.image.load('star_trek_background.png')
enShip_image2=pygame.image.load('fighterspr1.png')
enShip_image3=pygame.image.load('spacecraft_2.png')

font2=pygame.font.SysFont("Arial",40)


text_go=font2.render("GAME OVER",True,white)
text_go2=font.render("PRESS SPACE BAR FOR MENU",True,white)

text_inst=font2.render("INSTRUCTIONS",True,red)
text_inst1=font2.render("Use Arrow keys to move UP,DOWN,",True,black)
text_inst2=font2.render("LEFT and RIGHT.",True,black)
text_inst3=font2.render("Shoot using left Ctrl button.",True,black)
text_inst4=font2.render("You are the best!!!",True,black)
text_inst5=font2.render("Have Fun...",True,black)
text_inst6=font.render("PRESS ANY KEY FOR MENU",True,red)
text_inst7=font2.render("Press 'P' during game to PAUSE.",True,black)
new_hs=font2.render("NEW HIGH SCORE !!!",True,white)
winthemall=font2.render("YOU FINISHED THE GAME !!!",True,white)
text=font.render("1. Play",True,green)
text2=font.render("2. Instructions",True,green)
text3=font.render("3. Quit",True,green)
text4=font2.render("Travel in space",True,green)

text_pause=font2.render("PAUSED - Any key to continue !!!",True,white)
music=pygame.mixer.Sound("StarTrek.ogg")
s_sound=pygame.mixer.Sound('shoot.ogg')
d_sound=pygame.mixer.Sound('score.ogg')
nl_sound=pygame.mixer.Sound('newHs.ogg')
crash_sound=pygame.mixer.Sound('hihat3.ogg')

star_list=[]
for i in range(50):
    x=int(random.randint(2,699))
    y=int(random.randint(-200,599))
    star_list.append([x,y])





class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface([40,40])
        self.image.fill(black)
        self.image.blit(ship_image,[0,0])
        self.rect=self.image.get_rect()
        self.rect.x=350
        self.rect.y=550
        self.movex=0
        self.movey=0
        self.lives=3
    def go_left(self):
        self.movex=-3
        
    def go_right(self):
        self.movex=3
        
    def go_up(self):
        
        self.movey=-3
    def go_down(self):
        
        self.movey=3
    
    
    
    def stopx(self):
        self.movex=0
    def stopy(self):
        self.movey=0
    def update(self):
        self.rect.x+=self.movex
        self.rect.y+=self.movey
        if self.rect.x<1:
            self.rect.x=1
        elif self.rect.x>659:
            self.rect.x=659
        if self.rect.y<1:
            self.rect.y=1
        elif self.rect.y>559:
            self.rect.y=559
        
        
        
        
        
class Room(object):
    def __init__(self):
        self.enemies_list=pygame.sprite.Group() 
class Room0(Room):
    def __init__(self):
        super().__init__()
        
        for i in range(20):
            y=random.randrange(-3000,-50)
            x=random.randrange(0,660)
            enemy=Enemy(x,y,40,40,2,3,enShip_image)
            self.enemies_list.add(enemy)    

    


            
            
            
            
class Room1(Room):
    def __init__(self):
        super().__init__()
        
        for i in range(20):
            y=random.randrange(-3000,-50)
            x=random.randrange(0,660)
            enemy=Enemy(x,y,40,40,3,4,enShip_image1)
            self.enemies_list.add(enemy)
        
        
class Room2(Room):
    def __init__(self):
        super().__init__()
        
        for i in range(30):
            y=random.randrange(-3000,-50)
            x=random.randrange(0,660)
            enemy=Enemy(x,y,40,71,3,5,enShip_image2)
            self.enemies_list.add(enemy)
        
            
              
class Room3(Room):
    def __init__(self):
        super().__init__()
        
        for i in range(30):
            y=random.randrange(-3000,-50)
            x=random.randrange(0,660)
            enemy=Enemy(x,y,40,64,4,6,enShip_image3)
            self.enemies_list.add(enemy)
        
                   
        
        

class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height,speed,z,image):
        super().__init__()
        self.image=pygame.Surface([width,height])
        self.width=width
        self.image.fill(black)
        self.image.blit(image,[0,0])
        self.image.set_colorkey(black)
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.speed=speed
        
        self.bulletEn=BulletEn(self.rect.x+(self.width/2)-2,self.rect.y+30)
        self.bulletsEn_list=pygame.sprite.Group()
        self.bulletsEn_list.add(self.bulletEn)
        self.z=z
    def reset(self,l):
        self.rect.y=random.randrange(-l*60,-50)
        self.rect.x=random.randrange(0,700-self.width)
        self.bulletEn.rect.x=self.rect.x+(self.width/2)-2
        self.bulletEn.rect.y=self.rect.y+30
    
    
    
    def update1(self,l):
        self.rect.y+=self.speed
        self.bulletEn.rect.y=self.rect.y+30
        self.bulletEn.rect.x=self.rect.x+(self.width/2)-2
        if self.rect.y>600:
            self.reset(l)
        
            
     
    def Fire(self):
        self.bulletEn.rect.y+=1
        self.bulletEn.image.fill(red)
    def updateBulletEn(self,l):
        self.rect.y+=self.speed
        if self.rect.y>600:
            self.reset(l)
        self.bulletEn.rect.y+=self.speed+self.z
        if self.bulletEn.rect.y>600:
            self.bulletEn.rect.y=self.rect.y+30
            self.bulletEn.image.fill(black)

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface([4,10])
        self.image.fill(white)
        self.rect=self.image.get_rect()
    def update(self):
        self.rect.y-=2
        if self.rect.y<10:
            bullets_list.remove(self)
            all_sprites_list.remove(self)
    def reset(self):
        bullets_list.remove(self)
        all_sprites_list.remove(self)
            
        
        
class BulletEn(pygame.sprite.Sprite):
    def __init__(self,a,b):
        super().__init__()
        self.image=pygame.Surface([4,10])
        self.image.fill(black)
        self.rect=self.image.get_rect()
        self.rect.x=a
        self.rect.y=b
    
def menu():
    
    done=False
    
    
    

    
    while done==False:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done=True
                
                
                
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_1:
                    done=True
                    music.stop()
                    main()
                elif event.key==pygame.K_3:
                    done=True
                    music.stop()
                elif event.key==pygame.K_2:
                    done=True
                    
                    instructions()
                    
        
        screen.fill(black)
        screen.blit(ship_image,[350,550])
        
        for item in star_list:
            pygame.draw.circle(screen,white,item,2)
            item[1]+=1
            if item[1]>600:
                y=int(random.randint(-20,-3))
                x=int(random.randint(1,699))
                item[0]=x
                item[1]=y
                
        
        screen.blit(text,[255,200])
        screen.blit(text2,[255,230])
        screen.blit(text3,[255,260])
        screen.blit(text4,[200,40])
        pygame.display.flip()
        clock.tick(60)        
    
def instructions():
    
    done=False
    
    while done==False:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done=True
            elif event.type==pygame.KEYDOWN:
                done=True
                menu()
        screen.fill(yellow)
        screen.blit(text_inst,[200,50])
        screen.blit(text_inst1,[50,150])
        screen.blit(text_inst2,[50,190])   
        screen.blit(text_inst3,[50,250])
        screen.blit(text_inst4,[50,310])
        screen.blit(text_inst5,[50,370])
        screen.blit(text_inst6,[180,530])
        screen.blit(text_inst7,[50,430])
        
        pygame.display.flip()
        clock.tick(60)
    
def gameover(hsFlag,winall):
    
    done=False
    
    while done==False:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done=True
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    done=True
                    
                    menu()
        
        
        screen.blit(text_go,[220,150])
        
        screen.blit(text_go2,[180,500])
        
        if hsFlag==True:
            screen.blit(new_hs,[150,300])
        elif winall==True:
            screen.blit(background_image,[0,100])
            screen.blit(winthemall,[100,300])
        pygame.display.flip()
        clock.tick(60)
        
    

def paused():
    screen.blit(text_pause,[70,300]) 
    pygame.display.flip()
    done=False
    while done==False:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done=True
            elif event.type==pygame.KEYDOWN:
                done=True
               
        
        
    clock.tick(60)

    
    
    
    
    
all_sprites_list=pygame.sprite.Group()
bullets_list=pygame.sprite.Group()



        
        
def main():        
    
    hsFlag=False
    myFile=open("highscore.txt","r")
    hs=myFile.read()
    myFile.close()
    score=0
    
    
    
    
    done=False
    for i in all_sprites_list:
        i.kill()
    
    player=Player()
    all_sprites_list.add(player)
        
    
    all_rooms=[]
    room=Room0()       
    all_rooms.append(room)
    room=Room1()
    all_rooms.append(room)
    room=Room2()
    all_rooms.append(room)
    room=Room3()
    all_rooms.append(room)
    current_room_no=0
    current_room=all_rooms[current_room_no]
    for item in current_room.enemies_list:
        item.reset(len(current_room.enemies_list))
        
    while done==False:
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done=True
                menu()
            elif event.type==pygame.KEYDOWN:
                
                
                
                
                if event.key==pygame.K_LCTRL:
                    s_sound.play()
                    bullet=Bullet()
                    bullet.rect.x=player.rect.x+18
                    bullet.rect.y=player.rect.y
                    
                    bullets_list.add(bullet)
                    all_sprites_list.add(bullet)
                 
                elif event.key==pygame.K_p:
                    paused()   
                    
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    player.stopx()
                elif event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                    player.stopy()     
              
        
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                    player.go_left()
            elif keys[pygame.K_RIGHT]:
                    player.go_right()
            if keys[pygame.K_UP]:
                    player.go_up()
            elif keys[pygame.K_DOWN]:
                    player.go_down()
        
        
        
        
        
        for x in current_room.enemies_list:
            if (x.rect.x>=player.rect.x-4 and x.rect.x<player.rect.x+4) and x.rect.y>40:
                x.Fire()
        
            if x.bulletEn.rect.y>x.rect.y+30:
                x.updateBulletEn(len(current_room.enemies_list))
            else:
                x.update1(len(current_room.enemies_list))
            hit2_list=pygame.sprite.spritecollide(player,x.bulletsEn_list,True)
            for hit2 in hit2_list:
                crash_sound.play()
                player.lives-=1
                x.bulletEn=BulletEn(x.rect.x+(x.width/2)-2,x.rect.y+30)
                x.bulletsEn_list.add(x.bulletEn)    
        
        
        
        for item in bullets_list:
            hit_list=pygame.sprite.spritecollide(item,current_room.enemies_list,True)
            for hit in hit_list:
                score+=1
                d_sound.play()
                item.reset()
                hit.bulletsEn_list.remove(hit.bulletEn)
                #current_room.resetBulletEn()
                  
        hit3_list=pygame.sprite.spritecollide(player,current_room.enemies_list,False)
        for h3 in hit3_list:
            crash_sound.play()
            player.lives-=1
            h3.reset(len(current_room.enemies_list))
                
        screen.fill(black)       
        
        all_sprites_list.draw(screen)
        
            
        all_sprites_list.update()
        current_room.enemies_list.draw(screen)
        for i in current_room.enemies_list:
            i.bulletsEn_list.draw(screen)
        
        
        
        textL=font.render("Lives: "+str(player.lives),True,green)
        screen.blit(textL,[600,5])
        text_score=font.render("Score: "+str(score),True,green)
        screen.blit(text_score,[5,5])
        text_hs=font.render("High Score: "+hs,True,green)
        screen.blit(text_hs,[5,22])
        
        
        
        if len(current_room.enemies_list)<1:
            
            current_room_no+=1
            
            if current_room_no==4:
                done=True
                myFile=open('highscore.txt','w')
                myFile.write(str(score))
                myFile.close()
                music.play()
                gameover(False,True)
        
        
            else:
                current_room=all_rooms[current_room_no]
                for item in current_room.enemies_list:
                    item.reset(len(current_room.enemies_list))
                
                
                
                
        for item in star_list:
            pygame.draw.circle(screen,white,item,2)
            item[1]+=1
            if item[1]>600:
                y=int(random.randint(-20,-3))
                x=int(random.randint(1,699))
                item[0]=x
                item[1]=y        
        if player.lives<1:
            if score>int(hs):
                hsFlag=True
                myFile=open('highscore.txt','w')
                myFile.write(str(score))
                myFile.close()
            
            
            
            done=True
            music.play()
            gameover(hsFlag,False)
        pygame.display.flip()
        clock.tick(60)

music.play()    
menu()            
pygame.quit()            
            
