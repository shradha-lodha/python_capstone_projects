import pygame
pygame.init()
c=pygame.time.Clock()

screen=pygame.display.set_mode((400,300))
pygame.display.set_caption("Bouncing Ball")
background=pygame.image.load("bg.jpg").convert()

pink=(255,20,147)
blue=(0,0,255)
black=(0,0,0)

y1=10
y2=290

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
                   
    while y1<290 and y2>10:
      screen.blit(background,[0,0])            
      pygame.draw.circle(screen,pink,(140,y1),15)
      pygame.draw.circle(screen,blue,(240,y2),15)       
      y1=y1+1
      y2=y2-1
      c.tick(200)
      pygame.display.update()
      
    while y1>10 and y2<290:
      screen.blit(background,[0,0])            
      pygame.draw.circle(screen,pink,(140,y1),15)
      pygame.draw.circle(screen,blue,(240,y2),15)           
      y1=y1-1
      y2=y2+1
      c.tick(200)
      pygame.display.update()   
