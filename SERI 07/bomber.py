import pygame
import sys
import math


pygame.init()
pygame.mixer.init()

canvas = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("Pesawat Bomber")

warna_latar = (255, 255, 255)

pesawatkanan = pygame.image.load("assets/pesawatkanan.png")
pesawatkiri = pygame.image.load("assets/pesawatkiri.png")
rudal = pygame.image.load("assets/rudal.png")
ledakan = pygame.image.load("assets/ledakan.png")
awan = pygame.image.load("assets/awan.png")
suarabom = pygame.mixer.Sound("assets/ledakan.wav")
suarapesawat = pygame.mixer.Sound("assets/suarapesawat.wav")



jalankan = True
while jalankan:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jalankan = False
            sys.exit()



    t = pygame.time.get_ticks()
    waktu = t/1000                       # waktu = 1 detik

    jarak = 1000
    waktutempuh = 10
    kecepatan = jarak/waktutempuh

    putaran = math.floor(waktu/waktutempuh)
    y = 200

    # putaran 0 --> perubahan x = 0 + (waktu - 0) = 0 + (waktu - (putaran * waktu tempuh))
    # putaran 1 --> perubahan x = 1000 - (waktu - 10) = 1000 - (waktu - (putaran * waktu tempuh))
    # putaran 2 --> perubahan x = 0 + (waktu - 20) = 0 + (waktu - (putaran * waktu tempuh))
    # putaran 3 --> perubahan x = 1000 - (waktu - 30) = 1000 - (waktu - (putaran * waktu tempuh))

    canvas.fill(warna_latar)
    canvas.blit(awan, (0,0))
    suarapesawat.play()

    perubahan = (waktu - (putaran * waktutempuh))    # nilai maksimal selalu 10

    #if (putaran == 0):
    #    x = 30 + (kecepatan * perubahan)      # pergeseran 100 pixel setiap detik
        
    if (putaran % 2 != 0):                 # terjadi setiap putaran ganjil
        x = 1000 - (kecepatan * perubahan)
        pesawat = pesawatkanan

    if (putaran % 2 == 0):                # terjadi setiap putaran genap
        x = 0 + (kecepatan * perubahan)
        pesawat = pesawatkiri

    x_bom = 100                           # titik dimana pesawat akan menjatuhkan bom
                                          # x_bom != 0 dan x_bom != 1000
   
    kecepatanbom = (kecepatan * y)/x_bom
    
    nilaiakhiry = 0
    nilaiakhiry2 = 0
    nilaiakhiry3 = 0
    
    if (putaran % 2 == 0) and (x >= x_bom):
        y_bom = 0 + (kecepatanbom * perubahan)
        canvas.blit(rudal, (x_bom,y_bom))
        nilaiakhiry = y_bom


    if (nilaiakhiry < 600) and (putaran %2 != 0):
        y_tam = y_bom + (kecepatanbom * perubahan)
        canvas.blit(rudal, (x_bom,y_tam))
        nilaiakhiry2 = y_tam
        

    nilaimaksy = (2 * waktutempuh) * kecepatanbom

    if (nilaiakhiry2 < 600) and (putaran %2 == 0 and putaran != 0):
        y_tam2 = nilaimaksy + (kecepatanbom * perubahan)
        canvas.blit(rudal, (x_bom,y_tam2))
        nilaiakhiry3 = y_tam2
        
    if (700 > nilaiakhiry >= 600) or (700 > nilaiakhiry2 >= 600) or (700 > nilaiakhiry3 >= 600):
        canvas.blit(ledakan, (x_bom - 120, 450))
        suarabom.play()

    canvas.blit(pesawat, (x,y))
    pygame.display.flip()


    
pygame.quit()