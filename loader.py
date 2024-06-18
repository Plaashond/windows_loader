import pygame,sys
pygame.init()
S=pygame.display.set_mode((800,600))
F=pygame.font.Font("segoen_slboot.ttf",100)
M=[f"{i:X}"for i in range(0xE052,0xE0CB)]
i=0
while 1:
  for e in pygame.event.get():
   if e.type==pygame.QUIT:sys.exit()
  S.fill(0)
  S.blit(F.render(chr(int(M[i],16)),1,(255,255,255)),(300,250))
  pygame.display.flip()
  pygame.time.wait(45)
  i=(i+1)%len(M)