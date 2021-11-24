# Напиши програм који учитава четвороцифрени број и исписује збир свих цифара тог броја.
#
# Улаз: У једној линији стандардног улаза налази се четвороцифрени број.
#
# Излаз: Збир цифара четвороцифреног броја.
#
# Пример
# Улаз
# 1234
# Излаз
# 10

# učitavanje polaznog broja
broj = int(input("Unesi cetvorocifreni broj: "))

# izdvajanje cifara
cifra_jedinica = broj % 10; broj = broj // 10
cifra_desetica = broj % 10; broj = broj // 10
cifra_stotina = broj % 10; broj = broj // 10
cifra_hiljada = broj

# izračunavanje zbira
zbir_cifara = cifra_jedinica + cifra_desetica + \
cifra_stotina + cifra_hiljada

# prikaz rezultata
print("Zbir cifara cetvorocifrenog broja je "+str(zbir_cifara))
