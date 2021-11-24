# UNOS SA DESNE STRANE
#
# Петар и Марко се играју игре меморије. Петар диктира Марку цифре једног броја, једну по једну, отпозади,
# кренувши од цифре јединица. Напиши програм који помаже Марку да одреди број чије цифре Петар диктира.
#
# Улаз: Са стандардног улаза уноси се 6 декадних цифара, свака у посебном реду.
#
# Излаз: На стандардни излаз исписати један цео број - број чије цифре су унете са стандардног улаза.
#
# Пример 1
# Улаз
# 1
# 2
# 3
# 4
# 5
# 6
#
# Излаз
# 654321
#
# Пример 2
# Улаз
# 0
# 1
# 2
# 2
# 1
# 0
# Излаз
# 12210

def dodaj_cifru(tezina, broj):
    # ucitavamo novu cifru i dodajemo je na broj sa njegove leve strane
    cifra = int(input("Unesi cifru: "))
    broj = broj + tezina*cifra
    tezina = tezina * 10
    return (tezina, broj)

# tezina - trenutna tezina cifre
# broj - trenutna vrednost broja
# nakon k koraka broj je sastavljen od poslednjih k cifara trazenog broja
# a tezina ima vrednost 10^k
tezina = 1
broj = 0
(tezina, broj) = dodaj_cifru(tezina, broj)
(tezina, broj) = dodaj_cifru(tezina, broj)
(tezina, broj) = dodaj_cifru(tezina, broj)
(tezina, broj) = dodaj_cifru(tezina, broj)
(tezina, broj) = dodaj_cifru(tezina, broj)
(tezina, broj) = dodaj_cifru(tezina, broj)
print("Dobijen je broj : "+str(broj))
