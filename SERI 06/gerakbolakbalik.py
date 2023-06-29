import pygame
import sys
import math


pygame.init()

canvas = pygame.display.set_mode((1200, 400))
pygame.display.set_caption("Simulasi Gerak Bola Bolak Balik")

warna_latar = (255, 255, 255)

bolakaki = pygame.image.load("/home/rezaervani/Documents/PYTHON PROGRAMMING/assets/bolakaki.png")
siaptendang = pygame.image.load("/home/rezaervani/Documents/PYTHON PROGRAMMING/assets/siaptendang.png")
tendangkanan = pygame.image.load("/home/rezaervani/Documents/PYTHON PROGRAMMING/assets/tendangkanan.png")

jalankan = True
while jalankan:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jalankan = False
            sys.exit()

    t = pygame.time.get_ticks()
    waktu = t/1000                       # waktu = 1 detik

    jarak = 1000
    waktutempuh = 0.5
    kecepatan = jarak/waktutempuh

    putaran = math.floor(waktu/waktutempuh)
    y = 200

    # putaran 0 --> perubahan x = 0 + (waktu - 0) = 0 + (waktu - (putaran * waktu tempuh))
    # putaran 1 --> perubahan x = 1000 - (waktu - 10) = 1000 - (waktu - (putaran * waktu tempuh))
    # putaran 2 --> perubahan x = 0 + (waktu - 20) = 0 + (waktu - (putaran * waktu tempuh))
    # putaran 3 --> perubahan x = 1000 - (waktu - 30) = 1000 - (waktu - (putaran * waktu tempuh))

    canvas.fill(warna_latar)

    perubahan = (waktu - (putaran * waktutempuh))    # nilai maksimal selalu 10

    if (putaran == 0):
        x = 0 + (kecepatan * perubahan)      # pergeseran 100 pixel setiap detik
        
    if (putaran % 2 != 0):                 # terjadi setiap putaran ganjil
        x = 1000 - (kecepatan * perubahan)

    if (putaran % 2 == 0):                # terjadi setiap putaran genap
        x = 0 + (kecepatan * perubahan)

    # pemain menendang bola adalah pada saat putaran ke : 0, 2, 4, 6 ...
    # pemain menendang bola pada saat perubahan mendekati 10

    saatmenendang = waktutempuh - 0.1

    if (putaran % 2 == 0) and (saatmenendang <= perubahan <= waktutempuh):
        pemain = tendangkanan
    else:
        pemain = siaptendang

    canvas.blit(pemain, (1020,80))
    canvas.blit(bolakaki, (x,y))
    
    pygame.display.flip()

    
pygame.quit()