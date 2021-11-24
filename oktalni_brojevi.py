# У рачунарству се често користе тзв. октални бројеви - бројеви записани у основи 8, коришћењем само цифара
# од 0 до 7. Напиши програм који врши конверзију четвороцифрених окталних бројева у декадне вредности и
# обратно.

# Улаз: Са стандардног улаза се учитавају 4 окталне цифре (свака у посебном реду, почевши од цифре највеће
# тежине) и након тога декадно записан природан број n (0 ≤ n < 8^4).

# Излаз: На стандардном излазу у првој линији исписати декадну вредност броја формираног од учитаних
# окталних цифара, а у другој линији четвороцифрену окталну репрезентацију броја n.
#
# Пример
# Улаз
# 1
# 2
# 3
# 4
# 1234
# Излаз
# 668
# 2322

# odredjivanje vrednosti oktalnog zapisa (c3c2c1c0)8
def iz_oktalnog(c3, c2, c1, c0):
    return c3*8*8*8 + c2*8*8 + c1*8 + c0

# prevodjenje broja n u oktalni zapis (c3c2c1c0)8
def u_oktalni(n):
    c0 = (n // (1)) % 8;
    c1 = (n // (8)) % 8;
    c2 = (n // (8*8)) % 8;
    c3 = (n // (8*8*8)) % 8;
    return (c3, c2, c1, c0)

# izracunavanje vrednosti oktalno zapisanog broja
c3 = int(input("Uneti prvu oktalnu cifru: "))
c2 = int(input("Uneti drugu oktalnu cifru: "))
c1 = int(input("Uneti trecu oktalnu cifru: "))
c0 = int(input("Uneti cetvrtu oktalnu cifru: "))

# izracunavanje cifara broja koji treba zapisati oktalno
n = int(input("Uneti dekadni cetvorocifreni broj: "))
(c8, c7, c6, c5) = u_oktalni(n)

print("Iz oktalnog broja u dekadni dobijamo "+str(iz_oktalnog(c3, c2, c1, c0)))
print("Iz dekadnog u oktalni "+str(c8), str(c7), str(c6), str(c5), sep="")
