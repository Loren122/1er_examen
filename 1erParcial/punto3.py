from pila import Pila

# Se recuperó la bitácora de la nave del cazarrecompensas Boba Fett, la
# cual se almacenaban en una pila en cada misión de caza que
# emprendió(con la siguiente información planeta visitado, a quien
# capturado, costo de la recompensa), resolver las siguientes actividades:


class Registros():
    def __init__(self, planeta, captura, costo):
        self.planeta = planeta
        self.captura = captura
        self.costo = costo

    def __str__(self):
        return f"{self.planeta} - {self.captura} - {self.costo}"
    
def cargar_pila(pila):
    pila.push(Registros("Tatooine", "Bounty 1", 100)) # cuarta mision que realiza
    pila.push(Registros("Coruscant", "Bounty 2", 200)) # tercera mision que realiza
    pila.push(Registros("Endor", "Han Solo", 500)) # segunda mision que realiza
    pila.push(Registros("Hoth", "Bounty 3", 150)) # primera mision que realiza
    
# a. Mostrar los planetas visitados en el orden que hizo las misiones.
def mostrar_planetas_visitados(pila):
    
    while pila.size() > 0:
       registro = pila.pop()
       print(registro.planeta)
        
    cargar_pila(pila)

# b. Determinar cuántos créditos galácticos recaudo en total.
def credito_reacudado(pila):
    
    suma_credito = 0
    
    while pila.size() > 0:
        registro = pila.pop()
        suma_credito += registro.costo
        
    cargar_pila(pila)
        
    return suma_credito
        
 # c. Determinar el número de la misión en que capturo a Han Solo
 # # y en que planeta fue, suponga que dicha misión está cargada.
def captura_han_solo(pila):
     
    for i in range(1, pila.size()):
         
        registro = pila.pop()
        
        if registro.captura == "Han Solo":
            planeta_han_solo = registro.planeta
            num_mision = i 
    
    cargar_pila(pila)
    
    return num_mision, planeta_han_solo
           
    
pila = Pila()
cargar_pila(pila)

mostrar_planetas_visitados(pila), print()

print(credito_reacudado(pila)), print()
num_mision, planeta_han_solo = captura_han_solo(pila)
print(f"Encuentra a Han Solo en la {num_mision}° mision en el planeta {planeta_han_solo}")

