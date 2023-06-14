from pickle import TRUE
from lista import Lista
from cola import Cola

# 2. Dada una lista con nombres de personajes de la saga de Avengers
# ordenados por nombre del superhéroes, de los cuales se conoce:
#
# nombre del superhéroe, nombre del personaje(puede ser vacio),
#
# grupo al que(perteneces puede ser vacio), año de aparición,
# por ejemplo(Star Lord – Peter Quill – Guardianes de la galaxia - 1976).
#
# Resolver las siguientes tareas:










# h. Cargue al menos 20 superheroes a la lista.

class Personajes():
    def __init__(self, supername, name, team, year):
        self.supername = supername
        self.name = name
        self.team = team
        self.year = year

    def __str__(self):
        return f"Supername: {self.supername}, Name : {self.name}, Team : {self.team}, Year : {self.year}"


def cargar_personajes_avengers(lista):
    personajes_avengers = [
        Personajes("Star Lord", "Peter Quill",
                   "Guardianes de la galaxia", 1976),
        Personajes("Iron Man", "Tony Stark", "Avengers", 1963),
        Personajes("Thor", "", "Avengers", 1962),
        Personajes("Hulk", "Bruce Banner", "Avengers", 1962),
        Personajes("Black Widow", "Natasha Romanoff", "Avengers", 1964),
        Personajes("Captain America", "Steve Rogers", "Avengers", 1941),
        Personajes("Hawkeye", "Clint Barton", "Avengers", 1964),
        Personajes("Black Panther", "T'Challa", "Avengers", 1966),
        Personajes("Doctor Strange", "Stephen Strange", "Avengers", 1963),
        Personajes("Spider-Man", "Peter Parker", "Avengers", 1962),
        Personajes("Ant-Man", "Scott Lang", "Avengers", 1979),
        Personajes("Wasp", "Hope van Dyne", "Avengers", 1963),
        Personajes("Vision", "", "Avengers", 1968),
        Personajes("Scarlet Witch", "Wanda Maximoff", "Avengers", 1964),
        Personajes("Falcon", "Sam Wilson", "Avengers", 1969),
        Personajes("War Machine", "James Rhodes", "Avengers", 1979),
        Personajes("Winter Soldier", "Bucky Barnes", "Avengers", 2005),
        Personajes("Captain Marvel", "Carol Danvers", "Avengers", 1968),
        Personajes("Black Panther", "Shuri", "Avengers", 2005),
        Personajes("Spider-Man", "Miles Morales", "Avengers", 2011),
        Personajes("Groot", "", "Guardianes de la galaxia", 1960),
        Personajes("Mr. Fantastic", "Reed Richards",
                   "Los cuatro fantásticos", 1961),
        Personajes("Invisible Woman", "Susan Storm",
                   "Los cuatro fantásticos", 1961)
    ]

    for personaje in personajes_avengers:
        lista.insert(personaje, criterio="supername")


# a. Determinar si “Capitana Marvel” está en la lista y mostrar su
# nombre de personaje
def captain_marvel_esta(lista):

    for i in range(0, lista.size()):

        personaje = lista.get_element_by_index(i)

        if personaje.supername == "Captain Marvel":
            print(
                f"Capitana Marvel se ecuentra y su nombre es {personaje.name}")


# b. Almacenar los superhéroes que pertenezcan al grupo
# “Guardianes de la galaxia” en una cola e indicar cuantos son.
def alm_guard_galax_contar(lista):

    cola_guardianes = Cola()
    cont = 0

    for i in range(0, lista.size()):

        personaje = lista.get_element_by_index(i)

        if personaje.team == "Guardianes de la galaxia":
            cola_guardianes.arrive(personaje)
            cont += 1

    return cola_guardianes, cont

# c. Mostrar de manera descendente los superhéroes que
# pertenecen al grupo “Los cuatro fantásticos” y “Guardianes de la galaxia”.
def descend_fantasticos_guardianes(lista):

    lista_fantasticos = Lista()
    lista_guardianes = Lista()

    for i in range(0, lista.size()):

        personaje = lista.get_element_by_index(i)

        if personaje.team == "Los cuatro fantásticos":
            lista_fantasticos.insert(personaje.supername)

        if personaje.team == "Guardianes de la galaxia":
            lista_guardianes.insert(personaje.supername)


    return lista_fantasticos, lista_guardianes

# d. Listar los superhéroes que tengan nombre de personajes cuyo
# año de aparición sea posterior a 1960.
def post_1960(lista):
    
    lista_pos_1960 = Lista()
    
    for i in range(0,lista.size()):
        personaje = lista.get_element_by_index(i)
        
        if int(personaje.year) > 1960:
            lista_pos_1960.insert(personaje.supername)
            
# e. Hemos detectado que la superhéroe “Black Widow” está mal
# cargada por un error de tipeo, figura como “Vlanck Widow”,
# modifique dicho superhéroe para solucionar este problema.            

def corregir_nombre_black_widow(lista):
    for i in range(lista.size()):
        personaje = lista.get_element_by_index(i)
        if personaje.supername == "Vlanck Widow":
            lista.set_value(personaje, Personajes("Black Widow", personaje.name, personaje.team, personaje.year))
            
# f. Dada una lista auxiliar con los siguientes personajes(‘Black Cat’, ‘Hulk’, ‘Rocket Racoonn’, ‘Loki’,
# complete el resto de la información), agregarlos a la lista principal en el caso de no
# estar cargados.

def list_personajes(lista):
    lista_auxiliar = [
        Personajes("Black Cat", "Felicia Hardy", "Los Cuatro Fantásticos", 1979),
        Personajes("Hulk", "Bruce Banner", "Avengers", 1962),
        Personajes("Rocket Racoonn", "Rocket", "Guardianes de la Galaxia", 1976),
        Personajes("Loki", "Loki Laufeyson", "Villanos", 1962)
    ]

    for personaje_auxiliar in lista_auxiliar:
        esta = False
        for i in range(lista.size()):
            personaje_principal = lista.get_element_by_index(i)
            if personaje_principal.supername == personaje_auxiliar.supername:
                esta = True
                break
        if not esta:
            lista.insert(personaje_auxiliar)
   
# g. Mostrar todos los personajes que comienzan con C, P o S.            
def mostrar_superheroe_cps(lista):
    
    for i in range(lista.size()):
        personaje = lista.get_element_by_index(i)
        nombre = personaje.supername.lower()
        
        if nombre.startswith(('c', 'p', 's')):
            print(personaje)

lista_p = Lista()
cargar_personajes_avengers(lista_p)

captain_marvel_esta(lista_p), print()

cola_guardianess, contador_guardianes = alm_guard_galax_contar(lista_p)


print(f"Son {contador_guardianes} guardianes de la galaxia")

lista_fantastico, lista_guardianes = descend_fantasticos_guardianes(lista_p)
