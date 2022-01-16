# Познати су сат, минут и секунд почетка и краја вожње аутобусом (могуће је и да је вожња почела у једном,
# а завршила се у наредном дану, али се зна да је трајала мање од 24 сата). Написати програм који одређује
# колико сати, минута и секунди је трајала та вожња.
#
# Улаз: Са стандардног улаза учитава се 6 бројева (сваки у засебном реду). Прво сат, минут и секунд почетка
# вожње, а затим сат, минут и секунд краја вожње.
#
# Излаз: На стандрадни излаз се исписује један ред у коме су три броја (сат, минут и секунд) раздвојена
# запетом.
#
# Пример 1
# Улаз
# 23 59 59
# 0 0 1
# Излаз
# 0:0:2
#
# Пример 2
# Улаз
# 0 0 1
# 23 59 59
# Излаз
# 23:59:58

def u_milisekunde( sat, min, sek):
    return ( sat * 60 + min) * 60 + sek

# prevodi sekunde u sate, minute, sekunde
def od_milisekundi(v):
    sek = v % 60
    min = (v //  60) % 60
    sat = v // ( 60 * 60)
    return ( sat, min, sek)


poc_sat , poc_min , poc_sek = map(int,(input("Uneti vreme polaska: ").split()))
poc = u_milisekunde(poc_sat,poc_min,poc_sek)

dol_sat , dol_min , dol_sek = map(int,(input("Uneti vreme dolaska: ").split()))
dol = u_milisekunde(dol_sat,dol_min,dol_sek)

vre = u_milisekunde(24,0,0)

if poc > dol :
    vreme = vre - poc + dol
else:
    vreme = dol - poc

sat_tra , min_tra , sek_tra = od_milisekundi(vreme)

print(str(sat_tra) + ":" + str(min_tra) + ":" + str(sek_tra))
