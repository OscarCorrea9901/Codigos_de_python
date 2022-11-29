Calificacion = float(input("Ingrese la calificación del examen: "))

if Calificacion < 3:
    print("Insuficiente")
elif Calificacion >= 3 and Calificacion <  4:
    print("Aceptable")
elif Calificacion >= 4 and Calificacion <  4.6:
    print("Sobresaliente")
elif Calificacion >= 4.6 and Calificacion <=  5:
    print("Excelente")
