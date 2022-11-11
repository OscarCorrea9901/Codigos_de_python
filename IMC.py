# Captura la estatura y el peso para calcular el IMC y determina su condición de peso
Altura = float(input("Ingrese su estatura en metros: "))
Peso = float(input("Ingrese su peso en kilogramos: "))

IMC = Peso /(Altura**2)

if IMC < 18.5:
    print("Usted está bajo de peso")
elif IMC >= 18.5 and IMC < 24.9:
    print("Su peso se encuentra normal")
elif IMC >= 24.9 and IMC < 29.9:
    print("Usted tiene un peso superior al normal")
else:
    print("Usted se encuentra en obesidad")

print(f'Su indice de masa corporal es {IMC} kg/m2')