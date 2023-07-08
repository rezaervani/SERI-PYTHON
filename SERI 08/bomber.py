import pygame
import sys
import math
import pesawat


pygame.init()
pygame.mixer.init()


pygame.display.set_caption("Pesawat Bomber")

warna_latar = (255, 255, 255)
canvas = pygame.display.set_mode((1200, 600))


awan = pygame.image.load("assets/awan.png")





jalankan = True
while jalankan:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jalankan = False
            sys.exit()

    canvas.fill(warna_latar)
    canvas.blit(awan, (0,0))

    pesawat1 = pesawat.bomber(200,10)
    rudal1 = pesawat1.rudal(500, 1)
    rudal4 = pesawat1.rudal(100, 4)

    pesawat2 = pesawat.bomber(100,5)
    rudal2 = pesawat2.rudal(200, 2)

    pesawat3 = pesawat.bomber(300,7)
    rudal3 = pesawat3.rudal(800, 3)

    canvas.blit(pesawat1.kapal, (pesawat1.x,pesawat1.y))
    canvas.blit(pesawat2.kapal, (pesawat2.x,pesawat2.y))
    canvas.blit(pesawat3.kapal, (pesawat3.x,pesawat3.y))
   
    #print(rudal1.putaran, rudal1.waktu, rudal1.nilaiy1)

    pygame.display.flip()


    
pygame.quit()