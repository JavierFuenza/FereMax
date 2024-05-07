import pyrebase

#Diccionario para configuracion pyrebase
config = {
    "apiKey": "AIzaSyB6dPfDJP4HFblXOf4hHKvyDtQ7rmqLUMg",
    "authDomain": "ferremax-2023.firebaseapp.com",
    "databaseURL": "https://ferremax-2023-default-rtdb.firebaseio.com",
    "projectId": "ferremax-2023",
    "storageBucket": "ferremax-2023.appspot.com",
    "messagingSenderId": "237976751648",
    "appId": "1:237976751648:web:38c0421a295f58b6e2b645",
    "measurementId": "G-616XYS7Y25"
}
#Codigo para inicializar la coneccion a firebase
firebase = pyrebase.initialize_app(config)
db = firebase.database()
"""
(categoria se refiere a la categoria del articulo, ej: herramienta)
(las categorias posibles son:
-herramientas
-materiales
-seguridad
-anclajes
-fijaciones
-medicion )

Formato diccionario
diccionario = { "descripcion":'', "id": '', "marca": '', precio:'', "stock: ''}

Para subir diccionario
db.child("categoria").child("nombreProd").set(diccionario)

Recuperar datos:
categoria = db.child("categoria").get()

"""
herramientas = db.child("herramientas").get()
print(herramientas.key())
print(herramientas.val())