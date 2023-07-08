import requests, json

class Guia:
    def __init__(self):
        self.info = None
        self.residentes = []

    def obtener_informacion(self):
        self.info = requests.get("https://rickandmortyapi.com/api/location").json()

    def residentes_de(self, lugar):
        self.residentes = [elemento["residents"] for elemento in self.info["results"] if elemento["name"] == lugar]
        return self.residentes

    def obtener_residentes(self):
        return self.residentes
    
    def persistir_datos(self, id_personaje, archivo):            #este es para el d.
        respuesta1 = requests.get(f"https://rickandmortyapi.com/api/character/{id_personaje}")
        informacion= respuesta1.json()
        with open(archivo, 'w') as file:
            json.dump(informacion, file)
        print(f"La informacion del personaje número {id_personaje} se almacenó en {archivo}")

#a. Instancio guia y pruebo si funcionan los métodos
guia = Guia()
guia.obtener_informacion()
guia.residentes_de("Citadel of Ricks")
print(guia.obtener_residentes())

# b. rickandmortyapi.com

# c.
respuesta2 = requests.get('https://rickandmortyapi.com/api/location')
lugares = respuesta2.json()
cantidad_lugares = lugares["info"]["count"]
print("La API tiene", cantidad_lugares, "lugares almacenados")

# d. Si corro esto me lleva la información del personaaje con el id 1 a un archivo local del tipo .json en esta carpeta. Si cambio el número de id sobrescribe la infromación del que buscaba antes.
guia.persistir_datos(1, "personaje.json")

# e. El servidor proporciona recursos y servicios en respuesta a las solicitudes del cliente. El servidor tiene más capacidad y recursos que el cliente, actuando como proveedor de información, mientras que el cliente consume dicha información.
