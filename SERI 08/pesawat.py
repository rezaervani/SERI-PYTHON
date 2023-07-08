import pygame
import math

pygame.mixer.init()

pygame.mixer.set_num_channels(10)




canvas = pygame.display.set_mode((1200, 600))
pesawatkanan = pygame.image.load("assets/pesawatkanan.png")
pesawatkiri = pygame.image.load("assets/pesawatkiri.png")
suarapesawat = pygame.mixer.Sound("assets/suarapesawat.wav")
bom = pygame.image.load("assets/rudal.png")
ledakan = pygame.image.load("assets/ledakan.png")
suarabom = pygame.mixer.Sound("assets/ledakan.wav")



class bomber:
    def __init__(self, tinggi,waktutempuh):
        t = pygame.time.get_ticks()
        self.waktu = t/1000                       # waktu = 1 detik
        self.jarak = 1000
        self.waktutempuh = waktutempuh
        self.y = tinggi
        
        #channel1.play(suarapesawat)
        #channel1.set_volume(2)
        suarapesawat.play()
        self.kecepatan = self.jarak/self.waktutempuh
        self.putaran = math.floor(self.waktu/self.waktutempuh)
        #self.titikbom = titikbom

        self.perubahan = (self.waktu - (self.putaran * self.waktutempuh))    # nilai maksimal selalu 10

        

        if (self.putaran % 2 != 0):                 # terjadi setiap putaran ganjil
            self.x = 1000 - (self.kecepatan * self.perubahan)
            self.kapal = pesawatkanan
            

        if (self.putaran % 2 == 0):                # terjadi setiap putaran genap
            self.x = 0 + (self.kecepatan * self.perubahan)
            self.kapal = pesawatkiri


    
    def rudal(self, titikbom, nomorchannel):
        self.x_bom = titikbom                          # titik dimana pesawat akan menjatuhkan bom
                                                            # x_bom != 0 dan x_bom != 1000
        
        namachannel = "kanal" + str(nomorchannel)
        namachannel  = pygame.mixer.Channel(nomorchannel)
        
        self.kecepatanbom = (self.kecepatan * self.y)/self.x_bom

        self.nilaiakhiry = 0
        self.nilaiakhiry2 = 0
        self.nilaiakhiry3 = 0


        if (self.putaran % 2 == 0) and (self.x >= self.x_bom):
            self.y_bom = 0 + (self.kecepatanbom * self.perubahan)
            canvas.blit(bom, (self.x_bom,self.y_bom))
            self.nilaiakhiry = self.y_bom

        if (self.putaran != 0):
            self.posisi = ((self.waktu - self.perubahan) * self.kecepatanbom)/self.putaran
            self.nilaiy1 = self.posisi

        if (self.nilaiakhiry < 600) and (self.putaran %2 != 0):
            self.y_tam = self.nilaiy1 + (self.kecepatanbom * self.perubahan)
            canvas.blit(bom, (self.x_bom,self.y_tam))
            self.nilaiakhiry2 = self.y_tam

        self.nilaimaksy = (2 * self.waktutempuh) * self.kecepatanbom

        if (self.nilaiakhiry2 < 600) and (self.putaran %2 == 0 and self.putaran != 0):
            self.y_tam2 = self.nilaimaksy + (self.kecepatanbom * self.perubahan)
            canvas.blit(bom, (self.x_bom,self.y_tam2))
            self.nilaiakhiry3 = self.y_tam2

        if (700 > self.nilaiakhiry >= 600) or (700 > self.nilaiakhiry2 >= 600) or (700 > self.nilaiakhiry3 >= 600):
            canvas.blit(ledakan, (self.x_bom - 120, 450))

            namachannel.play(suarabom)
            namachannel.set_volume(2)
            #uarabom.play()

        
        
        return self

    