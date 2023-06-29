# Rumus Kecepatan v = s/t

import pygame
import sys
import math

pygame.init()

canvas = pygame.display.set_mode((800,600))
pygame.display.set_caption("Simulasi Kecepatan")

huruf = pygame.font.Font(None,25)

mobil1 = pygame.image.load("/home/rezaervani/Documents/PYTHON PROGRAMMING/assets/mobilbiru.png")
mobil2 = pygame.image.load("/home/rezaervani/Documents/PYTHON PROGRAMMING/assets/mobilmerah.png")
jalan = pygame.image.load("/home/rezaervani/Documents/PYTHON PROGRAMMING/assets/jalanan.png")

warna_latar = (255,255,255)

jalankan = True
while jalankan:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jalankan = False
            sys.exit()

    canvas.fill(warna_latar)

    waktu_gerak = pygame.time.get_ticks()

    #render = huruf.render(str(waktu_gerak), True, (0,0,0))
    #canvas.blit(render, (100,100))

    # 1 detik = 1000 milidetik

    waktu = waktu_gerak/1000      # = 1 detik
    jarak = round(30 * waktu)            # kecepatannya = 30 meter per detik

    jarak2 = round(60 * waktu)           # kecepatannya = 60 meter per detik

    kecepatan1 = round(jarak/waktu)
    kecepatan2 = round(jarak2/waktu)

    canvas.blit(jalan, (-10,0))

    canvas.blit(mobil1, (jarak,80))
    teks1 = "Jarak : " + str(jarak) + " meter"
    render1 = huruf.render(teks1, True, (255,255,255))
    canvas.blit(render1, (jarak, 140))

    teks2 = "Waktu : " + str(waktu) + " detik"
    render2 = huruf.render(teks2, True, (255,255,255))
    canvas.blit(render2, (jarak, 160))

    teks3 = "Kecepatan : " + str(kecepatan1) + " meter/detik"
    render3 = huruf.render(teks3, True, (255,255,255))
    canvas.blit(render3, (jarak, 180))

    canvas.blit(mobil2, (jarak2, 250))

    teks4 = "Jarak : " + str(jarak2) + " meter"
    render4 = huruf.render(teks4, True, (255,255,255))
    canvas.blit(render4, (jarak2, 300))

    teks5 = "Waktu : " + str(waktu) + " detik"
    render5 = huruf.render(teks5, True, (255,255,255))
    canvas.blit(render5, (jarak2, 320))

    teks6 = "Kecepatan : " + str(kecepatan2) + " meter/detik"
    render6 = huruf.render(teks6, True, (255,255,255))
    canvas.blit(render6, (jarak2, 340))

    pygame.display.flip()

pygame.quit()