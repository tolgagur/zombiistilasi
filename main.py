import math
import random

import pygame
from pygame import mixer

pygame.init()

ekran = pygame.display.set_mode((800, 600))

arkaplanresmi = pygame.image.load('resimler/arkaplan.png')

oyunbitti = pygame.image.load('resimler/oyunbitti.png')
oyunbittiIcon = pygame.image.load('resimler/zombi2.png')
askerSon = pygame.image.load('resimler/askerson.png')
kalanCan = pygame.image.load('resimler/kalancan.png')
plus = pygame.image.load('resimler/plus.png')
mixer.music.load("muzikler/thewalkingdead.wav")

arkafonses = mixer.music.play(-1)

pygame.display.set_caption("Zombi İstilası")
icon = pygame.image.load('resimler/icon.png')
pygame.display.set_icon(icon)

askerIcon = pygame.image.load('resimler/asker.png')
askerX = 370
askerY = 480
askerX_durum = 0

ZombiImg = []
ZombiX = []
ZombiY = []
ZombiX_durum = []
ZombiY_durum = []

deger = random.randrange(3, 7)
zombi_sayisi = deger

zombiListesi = ['resimler/zombi1.png', 'resimler/zombi2.png', 'resimler/zombi3.png', 'resimler/zombi4.png']

for i in range(zombi_sayisi):
    ZombiImg.append(pygame.image.load(random.choice(zombiListesi)))
    ZombiX.append(random.randint(0, 736))
    ZombiY.append(random.randint(50, 150))
    ZombiX_durum.append(4)
    ZombiY_durum.append(50)


def Zombi(x, y, i):
    ekran.blit(ZombiImg[i], (x, y))


mermiImg = pygame.image.load('resimler/mermi.png')
mermiX = 0
mermiY = 480
mermiX_durum = 0
mermiY_durum = 10
mermi_state = "hazır"

skor_sayisi = 0
tur_sayisi = 0
tur_tut = 0
zombiSayisi = 0
zombiRisk = 0
canTut = 3

font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
testY = 10

oyunSon = pygame.font.Font('freesansbold.ttf', 64)


def goster_skor(x, y):
    skor = font.render("Skorunuz : " + str(skor_sayisi), True, (255, 255, 255))
    ekran.blit(skor, (x, y))


def tur_goster(x, y):
    tur = font.render("Tur : " + str(tur_tut), True, (255, 255, 255))
    ekran.blit(tur, (x, y))


def can_goster(x, y):
    cangoster = font.render("Can : " + str(canTut), True, (255, 255, 255))
    ekran.blit(cangoster, (x, y))



    if canTut >= 6:
        ekran.blit(kalanCan, (10, 100))
        ekran.blit(kalanCan, (30, 100))
        ekran.blit(kalanCan, (50, 100))
        ekran.blit(kalanCan, (70, 100))
        ekran.blit(kalanCan, (90, 100))
        ekran.blit(plus, (110, 100))
    elif canTut == 5:
        ekran.blit(kalanCan, (10, 100))
        ekran.blit(kalanCan, (30, 100))
        ekran.blit(kalanCan, (50, 100))
        ekran.blit(kalanCan, (70, 100))
        ekran.blit(kalanCan, (90, 100))
    elif canTut == 4:
        ekran.blit(kalanCan, (10, 100))
        ekran.blit(kalanCan, (30, 100))
        ekran.blit(kalanCan, (50, 100))
        ekran.blit(kalanCan, (70, 100))
    elif canTut == 3:
        ekran.blit(kalanCan, (10, 100))
        ekran.blit(kalanCan, (30, 100))
        ekran.blit(kalanCan, (50, 100))
    elif canTut == 2:
        ekran.blit(kalanCan, (10, 100))
        ekran.blit(kalanCan, (30, 100))
    elif canTut == 1:
        ekran.blit(kalanCan, (10, 100))
    elif canTut == 0:
        ekran.blit(kalanCan, (3000, 3000))








def zombiSayisi(x, y):
    zombiSayisi = font.render("Zombi Sayısı : " + str(deger), True, (255, 255, 255))
    ekran.blit(zombiSayisi, (x, y))


def tehlikeDurumu(x, y):
    if -100 < zombiRisk < 200:
        riskDurum = font.render("Guvendesin : " + str(zombiRisk), True, (255, 255, 255))
    elif 201 < zombiRisk < 300:
        riskDurum = font.render("Cabuk : " + str(zombiRisk), True, (255, 255, 255))
    elif 301 < zombiRisk < 350:
        riskDurum = font.render("Yakindalar : " + str(zombiRisk), True, (255, 255, 255))
    elif 351 < zombiRisk < 450:
        riskDurum = font.render("Tehlikedesin: " + str(zombiRisk), True, (255, 255, 255))
    else:
        riskDurum = font.render("Zombiler Her yerde ", True, (255, 255, 255))

    ekran.blit(riskDurum, (x, y))


def toplamSkor(x, y):
    toplamSkor = zombi_sayisi * skor_sayisi * tur_tut
    toplamSkorYazdır = font.render("Toplam Skorun : " + str(toplamSkor), True, (255, 255, 255))
    ekran.blit(toplamSkorYazdır, (x, y))


def oyun_bitti():
    ekran.blit(oyunbitti, (0, 0))
    sonX = 350
    sonY = 350

    over_text = oyunSon.render("Oyun Sonu", True, (255, 255, 255))
    toplamSkor(sonX, sonY)
    ekran.blit(over_text, (200, 250))
    ekran.blit(askerSon, (400, 400))

    for i in range(3):
        sonX = random.randint(50, 600)
        sonY = random.randint(0, 736)
        ekran.blit(oyunbittiIcon, (sonX, sonY))


def oyuncu(x, y):
    ekran.blit(askerIcon, (x, y))


def ates_et(x, y):
    global mermi_state
    mermi_state = "ates"
    ekran.blit(mermiImg, (x + 16, y + 10))


def vurulmaAni(ZombiX, ZombiY, mermiX, mermiY):
    mesafe = math.sqrt(math.pow(ZombiX - mermiX, 2) + (math.pow(ZombiY - mermiY, 2)))
    if mesafe < 25:
        return True
    else:
        return False


devam = True
while devam:

    ekran.fill((0, 0, 255))
    ekran.blit(arkaplanresmi, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            devam = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                askerX_durum = -5
            if event.key == pygame.K_RIGHT:
                askerX_durum = 5
            if event.key == pygame.K_SPACE:
                if mermi_state is "hazır":
                    mermiSesi = mixer.Sound("muzikler/ates.wav")
                    mermiSesi.play()
                    mermiX = askerX
                    ates_et(mermiX, mermiY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                askerX_durum = 0

    askerX += askerX_durum
    if askerX <= 0:
        askerX = 0
    elif askerX >= 736:
        askerX = 736

    for i in range(zombi_sayisi):

        zombiRisk = 0

        if zombiRisk < ZombiY[i]:
            zombiRisk = ZombiY[i]

        if canTut == 0:
            if ZombiY[i] > 400:
                for j in range(zombi_sayisi):
                    ZombiY[j] = 2000
                    askerY = 2000
                oyun_bitti()
                break

        if ZombiY[i] > 440:
            canTut = canTut - 1
            for j in range(zombi_sayisi):
                ZombiX[i] = random.randint(0, 736)
                ZombiY[i] = random.randint(-50, 0)

            Zombi(ZombiX[i], ZombiY[i], i)

            break

        ZombiX[i] += ZombiX_durum[i]

        if ZombiX[i] <= 0:
            ZombiX_durum[i] = 4
            ZombiY[i] += ZombiY_durum[i]
        elif ZombiX[i] >= 736:
            ZombiX_durum[i] = -4
            ZombiY[i] += ZombiY_durum[i]

        carpisma = vurulmaAni(ZombiX[i], ZombiY[i], mermiX, mermiY)
        if carpisma:
            carpismaMusic = mixer.Sound("muzikler/carpisma.wav")
            carpismaMusic.play()
            mermiY = 480
            mermi_state = "hazır"

            skor_sayisi += 1
            tur_sayisi += 1
            if tur_sayisi % 15 == 0:
                canTut = canTut + 1

            if tur_sayisi % deger == 0:
                tur_tut += 1



            if tur_sayisi % deger == 0:
                skor_sayisi += tur_tut

            ZombiX[i] = random.randint(0, 736)
            ZombiY[i] = random.randint(-50, 0)

        Zombi(ZombiX[i], ZombiY[i], i)

    if mermiY <= 0:
        mermiY = 480
        mermi_state = "hazır"

    if mermi_state is "ates":
        ates_et(mermiX, mermiY)
        mermiY -= mermiY_durum

    oyuncu(askerX, askerY)
    goster_skor(textX, testY)
    tur_goster(textX, testY + 30)
    zombiSayisi(textX, 550)
    tehlikeDurumu(400, 10)
    can_goster(textX, testY + 60)
    pygame.display.update()
