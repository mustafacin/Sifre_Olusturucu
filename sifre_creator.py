import random

def girdiler():

    rakam = input("Kac harfli bir sifre olusturmak istiyorsunuz? : ")
    sayi = input("sifrenizde rakamlar bulunsun mu? (E/H) : ")
    ozel = input("Sifrenizde ozel karakterler bulunsun mu? (E/H) : ")


    if (sayi == "E" or ozel == "E") or (sayi == "e" or ozel == "e"):
        if (sayi == "E" and ozel =="H") or (sayi == "e" and ozel == "h"):
            kwargs = "ok1"
            main(rakam, kwargs)
        elif (sayi == "H" and ozel == "E") or (sayi == "h" and ozel == "e"):
            kwargs = "ok2"
            main(rakam, kwargs)

        elif (sayi == "E" and ozel == "E") or (sayi == "e" and ozel == "e"):
            kwargs = "ok12"
            main(rakam, kwargs)

        else:
            print("Yanlis bir deger tusladiniz!!!\n")
            print("Kucuk veya buyuk harf kullanarak 'E/H' veya 'e/h' seklinde tuslama yapiniz. ")

    elif (sayi == "H" and ozel == "H") or (sayi == "h" and ozel == "h"):
        kwargs = "no"
        main(rakam, kwargs)

    else:
        print("Yanlis bir deger tusladiniz !!!! ")

    print("\n")



def main(rakam, kwargs):
    sayac = 0
    if kwargs == "ok1":
        a = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        for i in a:
            if sayac < int(rakam):
                b = random.choice(a)
                print(b, end="")
                sayac = sayac + 1

    elif kwargs == "ok2":
        a = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'"
        for i in a:
            if sayac < int(rakam):
                b = random.choice(a)
                print(b, end="")
                sayac = sayac + 1

    elif kwargs == "ok12":
        a = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'"
        for i in a:
            if sayac < int(rakam):
                b = random.choice(a)
                print(b, end="")
                sayac = sayac + 1


    elif kwargs == "no":
        a = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i in a:
            if sayac < int(rakam):
                b = random.choice(a)
                print(b, end="")
                sayac = sayac + 1




if __name__ == "__main__":
    girdiler()

