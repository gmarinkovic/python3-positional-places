# Ђаци увежбавају сабирање троцифрених бројева. Учитељица диктира задатак редом цифру по цифру.
# Напиши програм који на основу учитаних цифара израчунава и исписује тражени збир.

# Улаз: У шест линија стандардног улаза задато је шест цифара.

# Излаз: На стандардни излаз исписати један цео број - тражени збир.

# Пример
# Улаз
# 1
# 2
# 3
# 4
# 5
# 6
# Излаз
# 579

# funkcija ucitava trocifreni broj cija je svaka cifra u posebnom redu
def ucitaj_trocifreni_broj():
    broj = 0
    cifra = int(input("Unesi prvu cifru trocifrenog broja: "))
    broj = 10*broj + cifra
    cifra = int(input("Unesi drugu cifru trocifrenog broja: "))
    broj = 10*broj + cifra
    cifra = int(input("Unesi trecu cifru trocifrenog broja: "))
    broj = 10*broj + cifra
    return broj

# ucitavamo i sabiramo dva trocifrena broja
broj1 = ucitaj_trocifreni_broj()
broj2 = ucitaj_trocifreni_broj()
print("Rezultat je "+str(broj1 + broj2))
