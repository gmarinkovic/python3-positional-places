# Напиши програм којим се у датом природном броју размењује цифра јединица и цифра стотина. За број са
# мање од три цифре сматрамо да су недостајуће цифре једнаке 0.
#
# Улаз: У првој линији стандардног улаза налази се природан број мањи од милијарде.
#
# Излаз: На стандардни излаз исписати број добијен после размене цифре јединица и цифре стотина.
#
# Пример
# Улаз
# 2349
# Излаз
# 2943

x=int(input("Unesi prirodan broj manji od milijarde: "))

c0=(x//1)%10
c1=(x//10)%10
c2=(x//100)%10
c3=(x//1000)%10

y=c3*1000+c0*100+c1*10+c2
print("Izmenjeni broj je : "+str(y))