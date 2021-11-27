# Напиши програм који одређује број добијен када се из датог троцифреног броја избацују сва појављивања
# његове цифре јединица.
#
# Улаз: Са стандардног улаза се уноси један троцифрени број.
#
# Излаз: На стадардни излаз исписати тражени број.
#
# Пример 1
# Улаз
# 131
# Излаз
# 3
#
# Пример 2
# Улаз
# 133
# Излаз
# 1
#
# Пример 3
# Улаз
# 123
# Излаз
# 12
#
# Пример 4
# Улаз
# 333
# Излаз
# 0

# polazni broj
n = int(input("Unesi trocifren broj: "))

# cifra jedinica polaznog broja
c0 = n % 10

# vrednost rezultata gradimo sdesna na levo
rezultat = 0
tezina = 1

# uklanjamo poslednju cifru tekuceg broja i ako je ona razlicita od
# cifre koja se izbacuje, dodajemo je na levu stranu rezultata
cifra = n % 10
n = n // 10

# naredni uslov sigurno nece biti ispunjen, pa se moze preskociti
# if cifra != c0:
# rezultat = rezultat + cifra*tezina;
# tezina = tezina * 10;
# uklanjamo poslednju cifru tekuceg broja i ako je ona razlicita od
# cifre koja se izbacuje, dodajemo je na levu stranu rezultata

cifra = n % 10
n = n // 10
if cifra != c0:
    rezultat = rezultat + cifra * tezina
    tezina = tezina * 10

# uklanjamo poslednju cifru tekuceg broja i ako je ona razlicita od
# cifre koja se izbacuje, dodajemo je na levu stranu rezultata
cifra = n % 10
n = n // 10
if cifra != c0:
    rezultat = rezultat + cifra * tezina
    tezina = tezina * 10
# ispisujemo konacan rezultat
print(rezultat)
