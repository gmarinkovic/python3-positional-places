# Познати су сат, минут и секунд почетка филма и дужина трајања филма у секундама. Написати програм који
# одређује сат, минут и секунд завршетка филма.
#
# Улаз: Са стандардног улаза учитавају се 4 природна броја (сваки у засебном реду). Прво сат, минут и секунд
# почетка филма, а затим дужина трајања филма у секундама.
#
# Излаз: На стандрадни излаз се исписује један ред у коме су три броја (сат, минут и секунд) раздвојена
# двотачкама који представљају време завршетка филма.
#
# Пример
# Улаз
# 23
# 15
# 22
# 4115
# Излаз
# 0:23:57

# ucitavamo vreme pocetka i duzinu filma
print("Film je poceo")
hPocetka = int(input("u sati: "));
mPocetka = int(input("u minuta: "));
sPocetka = int(input("u sekundama: "))
duzina = int(input("Film traje: "))

# dodajemo duzinu u sekundama na vreme pocetka
# vrseci prenos istovremeno sa sabiranjem
sZavrsetka = (sPocetka + duzina) % 60
prenos = (sPocetka + duzina) // 60
mZavrsetka = (mPocetka + prenos) % 60
prenos = (mPocetka + prenos) // 60
hZavrsetka = (hPocetka + prenos) % 24
# prenos broja dana se zanemaruje
# prenos = (hPocetka + prenos) // 24
# ispisujemo rezultat
print(hZavrsetka, ":", mZavrsetka, ":", sZavrsetka, sep="")
