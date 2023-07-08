import random

nombres_mujer = ["Katniss", "Primrose", "Effie", "Rue", "Glimmer", "Johanna", "Annie", "Clove", "Sae", "Venia", "Mags", "Wiress", "Enobaria" ]  #creo una lista con nombre de mujeres que supongamos que son todos los nombres que existen en Panem
nombres_hombre = ["Peeta", "Gale", "Haymitch", "Cato", "Finnick", "Thresh", "Marvel", "Cinna", "Seneca", "Caesar", "Thresh", "Snow", "Claudius"]   #también creo una lista pero de hombres
generos = ["Mujer", "Hombre"]



class Participante:
    def __init__(self, nombre, edad, sexo, distrito):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.distrito = distrito

    def __str__(self):
        return f"{self.nombre}, {self.edad} años, {self.sexo}, Distrito {self.distrito}"


class Distrito:

  def __init__(self, numero, cantidad_hombres, cantidad_mujeres):
    self.numero = numero
    self.participantes_hombres = []  # acá hago una lista vacía para los participantes hombres
    self.participantes_mujeres = []  # y otra para mujeres

    for x in range(cantidad_hombres):       # y voy creando hombres con los nombres masculinos que creé con edades random entre 12 y 18 y que pertenecen a diferentes distritos
      nombre = random.choice(nombres_hombre)
      edad = random.randint(12, 18)
      participante = Participante(nombre, edad, "Hombre", self.numero)
      self.participantes_hombres.append(participante)

    for y in range(cantidad_mujeres):       #lo mismo con las mujeres
      nombre = random.choice(nombres_mujer)
      edad = random.randint(12, 18)
      participante = Participante(nombre, edad, "Mujer", self.numero)
      self.participantes_mujeres.append(participante)

  def elegir_participantes(self):            # toma como una "muestra" de cada distrito que son los participantes, un hombre y una mujer de cada lista que creé más arriba
    hombre_elegido = random.choice(self.participantes_hombres)     
    mujer_elegida = random.choice(self.participantes_mujeres)       
    return [hombre_elegido, mujer_elegida]  

  def mostrar_poblacion(self):        #esto me muestra las personas que hay en cada distrito entre 12 y 18 años de las listas
    for participante in self.participantes_hombres:   
      print(participante)
    for participante in self.participantes_mujeres:   
      print(participante)


class Panem:

  def __init__(self):
    self.distritos = []

  def agregar_distrito(self, numero):
    cantidad_hombres = random.randint(1, 10)         # acá genero una cantidad variable de hombres en la poblacion del distrito 
    cantidad_mujeres = random.randint(1, 10)         # y de mujeres
    distrito = Distrito(numero, cantidad_hombres, cantidad_mujeres)
    self.distritos.append(distrito)

  def mostrar_poblacion(self):      #si corro este método podría ver a toda la población entre 12 y 18 años por cada distrito
    for distrito in self.distritos:       
      print(f"Distrito {distrito.numero}:")
      distrito.mostrar_poblacion()

  def iniciar_juegos(self):
    print("Se anuncian a los participantes en el desfile. Estos son:")
    participantes = []
    for distrito in self.distritos:
      participantes.extend(distrito.elegir_participantes())       #extend es como un append que nos agrega los elementos al final de la lista de participantes
    for participante in participantes:
      print(participante)
    
    print("--------------------------------------------------------------------------") 
    print("¡Que comiencen los Juegos del Hambre!")

    print("--------------------------------------------------------------------------")

    while len(participantes) > 1:               
      participante_eliminado = random.choice(participantes)         # muera uno al azar de los participantes 
      participantes.remove(participante_eliminado)          
      print("Se avista una bengala en el cielo y el sinsajo anuncia la muerte de", participante_eliminado)      # acá voy haciendo que se eliminen uno por uno los participantes en la lista hasta que quede uno solo
      
    ganador = participantes[0]                #tomo el único elemento que quedó en la lista que es el único que no murió de los participantes y ganó
    print("--------------------------------------------------------------------------")
    print("¡",ganador, "ha ganado los Juegos del Hambre !")



# instancio Panem
panem = Panem()

# instancio los distritos del 1 al 12 y no agrego el distrito 13 porque los participantes son 24, osea 2 por cada uno de los 12 distritos. En el distrito 13 no vivía nadie según la película, por eso mismo no lo sumo.
for numero_distrito in range(1, 12):     
    panem.agregar_distrito(numero_distrito)

#si quiero ver a la población cómo está conformada antes de elegir a los participantes puedo correr esto de abajo:
#panem.mostrar_poblacion()      

# inicio los Juegos del Hambre
panem.iniciar_juegos()


