# Simulasi Gerak Miring

import pygame
import sys
import math

pygame.init()

canvas = pygame.display.set_mode((800,600))
pygame.display.set_caption("Simulasi Gerak Miring")

warna_latar = (255,255,255)

bolakaki = pygame.image.load("/home/rezaervani/Documents/PYTHON PROGRAMMING/assets/bolakaki.png")

jalankan = True
while jalankan:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jalankan = False
            sys.exit()

    

    kemiringan = 10             # dalam derajat, harus dikonversi ke radians
    
    for x in range (1,501):
        y = math.tan(math.radians(kemiringan)) * x
        pygame.time.delay(10)
        canvas.fill(warna_latar)
        canvas.blit(bolakaki, (x,y))
        pygame.display.flip()

    

pygame.quit()
