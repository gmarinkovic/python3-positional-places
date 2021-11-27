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

# odredjujemo cifre polaznog broja
c0 = (n // 1) % 10
c1 = (n // 10) % 10
c2 = (n // 100) % 10

# Hornerovim postupkom gradimo rezultat, zadrzavajuci samo
# cifre razlicite od cifre jedinice
rezultat = 0
if (c2 != c0):
    rezultat = 10 * rezultat + c2
if (c1 != c0):
    rezultat = 10 * rezultat + c1

# naredni uslov sigurno nece biti ispunjen, pa se moze preskociti
# if (c0 != c0)
# rezultat = 10*rezultat + c0;
# ispisujemo konacan rezultat
print(rezultat)
