from random import randint
# Desarrollar una función recursiva que permita contar cuantas veces
# aparece una determinada palabra, en un vector de palabras.

def cont_palabra_r(palabra, vector):
    if not vector:
        return 0
        
    elif vector[0] == palabra:
        return 1 + cont_palabra_r(palabra, vector[1:])
    else:
        return cont_palabra_r(palabra, vector [1:])
    
        
vector = ["hueso","casa", "casa", "pollo", "casa"]
resultado = cont_palabra_r("casa", vector)

print(resultado)