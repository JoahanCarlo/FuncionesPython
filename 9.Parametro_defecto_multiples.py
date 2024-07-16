#Parámetros por defecto y múltiples returns

def volumen(lenght=1,height=1,width=1):
    return lenght*height*width,width,"hola"

result,width,text = volumen(height=32)
print(f"El volumen del paralelepipedo es : {result} m3")
print(width)
print(text)
    