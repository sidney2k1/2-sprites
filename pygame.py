import pygame
import random
screenwidth,screenheight=500,400
movementspeed=5
fontsize=12
pygame.init()
backgroundimage=pygame.transform.scale(pygame.image.load("download.jpeg"),(screenwidth,screenheight))
font=pygame.font.Sysfont("Times New Roman",fontsize)
class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,width,height):
        super().__init__()
        self.image=pygame.Surface([width,height])
        self.image.fill(pygame.Color("dodgerblue"))
        pygame.draw.rect(self.image,color,pygame.Rect(0,0,width,height))
        self.rect=self.image.get_rect()
    def move(self,changex,changey):
        self.rect.x=max(min(self.rect.x+changex,screenwidth-self.rect.width),0)
        self.rect.y=max(min(self.rect.y+changey,screenheight-self.rect.height),0)
screen=pygame.display.set_mode((screenwidth,screenheight))
pygame.display.set_caption("Two sprites")
allsprites=pygame.sprite.Group()
sprite1=Sprite(pygame.Color("black"),20,30)
sprite1.rect.x,sprite1.rect.y=random.randint(0,screenwidth-sprite1.rect.width),random.randint(0,screenheight-sprite1.rect.height)
allsprites.add(sprite1)
sprite2=Sprite(pygame.Color("red"),20,30)
sprite2.rect.x,sprite2.rect.y=random.randint(0,screenwidth-sprite2.rect.width),random.randint(0,screenheight-sprite2.rect.height)
allsprites.add(sprite2)
running,won=True,False
clock=pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.type==pygame.K_x):
            running=False
    if not won:
        keys=pygame.key.get_pressed()
        changex=(keys[pygame.K_RIGHT]-keys[pygame.K_LEFT])*movementspeed
        changey=(keys[pygame.K_DOWN]-keys[pygame.K_UP])*movementspeed
        sprite1.move(changex,changey)
        if sprite1.rect.colliderect(sprite2.rect):
            allsprites.remove(sprite2)
            won=True
    screen.blit(backgroundimage,(0,0))
    allsprites.draw(screen)
    if won:
        screen.blit(win_text, ((SCREEN_WIDTH - win_text.get_width()) // 2,(SCREEN_HEIGHT - win_text.get_height()) // 2))

pygame.display.flip()

clock.tick(90)

pygame.quit(
