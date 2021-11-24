# Oд оперативног система UNIX време у рачунарима се изражава као број секунди протеклих од почетка епохе тј.
# од 1. јануара 1970. године. По узору на то, осмислили смо систем мерења времена у коме се време
# изражава бројем милисекунди протеклих од укључивања рачунара. У неком тренутку, на рачунару је пуштена песма.
# Ако је познато време када је песма пуштена и дужина трајања песме у милисекундама, напиши
# програм који одређује када је песма завршена.
#
# Улаз: Са стандардног улаза учитавају се следећи цели бројеви (сваки у посебном реду):
# • dan (0 ≤ dan ≤ 10), sat (0 ≤ sat < 24), min (0 ≤ min < 60), sek (0 ≤ sek < 60), mili (0 ≤ mili <
# 1000) - број дана, сати, минута, секунди и милисекунди протеклих од тренутка укључивања рачунара
# до пуштања песме.
# • trajanje (0 ≤ trajanje ≤ 1000000) - број милисекунди колико траје песма.
#
# Излаз: На стандардни излаз исписати следеће целе бројеве, раздвојене двотачкама:
# • dan (0 ≤ dan ≤ 100), sat (0 ≤ sat < 24), min (0 ≤ min < 60), sek (0 ≤ sek < 60), mili (0 ≤ mili < 1000)
# - број дана, сати, минута, секунди и милисекунди протеклих од тренутка укључивања рачунара
# до завршетка песме.
#
# Пример 1
# Улаз
# 3
# 10
# 15
# 23
# 843
# 100000
# Излаз
# 3:10:17:3:843
#
# Пример 2
# Улаз
# 4
# 23
# 59
# 59
# 517
# 12345
# Излаз
# 5:0:0:11:862
#
# Пример 3
# Улаз
# 10
# 23
# 59
# 59
# 999
# 1000000
# Излаз
# 11:0:16:39:999

# prevodi broj dana, sati, minuta, sekundi i milisekundi u broj milisekundi
def u_milisekunde(dan, sat, min, sek, mili):
    # Hornerova sema
    rez = dan
    rez = rez * 24 + sat
    rez = rez * 60 + min
    rez = rez * 60 + sek
    rez = rez * 1000 + mili
    return rez

# prevodi milisekunde u dane, sate, minute, sekunde i milisekunde
def od_milisekundi(v):
    mili = v % 1000
    v = v // 1000
    sek = v % 60
    v = v // 60
    min = v % 60
    v = v // 60
    sat = v % 24
    v = v // 24
    dan = v
    return (dan, sat, min, sek, mili)


# početak pesme izrazen u broju dana, sati, minuta, sekundi i milisekundi od uključivanja računara
pocetak_dan = int(input("Uneti dan: "))
pocetak_sat = int(input("Uneti sate: "))
pocetak_min = int(input("Uneti minute: "))
pocetak_sek = int(input("Uneti sekunde: "))
pocetak_mili = int(input("Uneti milisekunde: "))

# trajanje pesme u milisekundama
trajanje = int(input("Uneti vreme trajanja pesme u milisekundama: "))

# početak pesme izražen u broju milisekundi od uključivanja racunara
pocetak = u_milisekunde(pocetak_dan, pocetak_sat, pocetak_min, pocetak_sek, pocetak_mili)

# kraj pesme izražen u broju milisekundi od uključivanja računara
kraj = pocetak + trajanje

# kraj pesme izrazen u broju dana, sati, minuta, sekundi i milisekundi
(kraj_dan, kraj_sat, kraj_min, kraj_sek, kraj_mili) = od_milisekundi(kraj)

# ispis rezultata
print(kraj_dan, ":", kraj_sat, ":", kraj_min, ":", kraj_sek, ":", kraj_mili, sep="")
