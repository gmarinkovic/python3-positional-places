# Ако је познато трајање путовања и време када аутобус треба да стигне на одредиште, напиши програм који
# израчунава када аутобус треба да пође са полазишта (полазак може бити у претходном дану у односу на
# долазак).
#
# Улаз: Са стандардног улаза учитава се четири цела броја:
# • trajanjeh (0 ≤ trajanjeh < 12) и trajanjem (0 ≤ trajanjem < 60) - сати и минути трајања вожње
# • dolazakh (0 ≤ dolazakh < 24) и dolazakm (0 ≤ dolazakm < 60) - сат и минут доласка
#
# Излаз: На стандардни излаз исписати два цела броја раздвојена двотачком:
# • polazakh (0 ≤ polazakh < 24) и polazakm (0 ≤ polazakm < 60) - сат и минут поласка
#
# Пример 1
# Улаз
# 2 30
# 13 0
# Излаз
# 10:30
#
# Пример 2
# Улаз
# 12
# 0
# 8
# 0
# Излаз
# 20:0

def u_minute( sat, min):
    return sat * 60 + min

# prevodi sekunde u sate, minute
def od_minuta(v):
    min = v % 60
    sat = v // 60
    return ( sat, min )

tra_sat , tra_min = map(int,(input("Uneti vreme dolaska: ").split()))
tra = u_minute(tra_sat,tra_min)

dol_sat , dol_min = map(int,(input("Uneti vreme trajanja voznje: ").split()))
dol = u_minute(dol_sat,dol_min)

vre = u_minute(24,0)

if dol >= tra :
    pol = dol-tra
else:
    pol = vre - (tra - dol)

pol_sat , pol_min = od_minuta(pol)
print( str(pol_sat)+":"+str(pol_min))
