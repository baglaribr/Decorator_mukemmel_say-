# -*- coding: utf-8 -*-
def mukemmel(fonk):
    def wrapper(sayılar):
        mukemmel = [] # mukemmel sayıların listesi
        for i in sayılar:
            toplam = 0 # sayıyı tam bölenlerin toplamını hesaplamak için parametre
            a = 1 # sayıyı bölen sayıları bulmak için
            if i == 1:
                continue
            else:
                while(a<i):
                    if (i%a == 0):
                        toplam += a
                    a += 1
                if toplam == i:
                    mukemmel.append(i)
        print( "Mukemmel Sayılar:",mukemmel)
        fonk(sayılar)
    return wrapper

@mukemmel
def asal_sayılar(sayılar):
    asal = []  # asal sayıları ekleyeceğimiz listeyi oluşturalım
    for i in sayılar:
        sayım = 0 # sayıyı tam bölenleri hesaplamak için parametre
        a = 1 # sayıyı bölen sayıları bulmak için
        if i == 1:
            continue
        else:
            while (a<i):
                if (i % a == 0):
                    sayım +=1
                a +=1
        if sayım == 1:
            asal.append(i)
    print( "Asal sayılar: ",asal)


asal_sayılar(range(1001))