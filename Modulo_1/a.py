puntuacion = int(input("cual es tu puntuacion"))
if puntuacion >= 90:
    print("bien hecho tu puntuacion es A")
elif puntuacion >= 80 and puntuacion <= 89:
    print("bien hecho tu puntuacion es D")
elif puntuacion >= 70 and puntuacion <= 79:
    print("bien hecho tu puntuacion es C") 
elif puntuacion >= 60 and puntuacion <= 69:
    print("bien hecho tu puntuacion es B")    
elif puntuacion >= 50 and puntuacion <= 59:
    print("bien hecho tu puntuacion es E")     
else:
    print("nesecitas mejorar")





puntuacion = int(input("elije un numero del 1 al 20"))
if puntuacion <= 5:
    print("tu rango es E")   
elif puntuacion <= 10:
    print("tu rango es F")
elif puntuacion <= 15:
    print("tu rango es B")
else:
    print("tu rango es A")



nota = int(input("tu nota es "))
if nota > 5:
    print("aprobado")
elif nota <= 5:
    print("reprobado")