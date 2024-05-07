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

Actualizar datos:
db.child("categoria").child("nombreProd").update({"stock": ""})

remove
To delete data for an existing entry use the remove() method.

db.child("users").child("Morty").remove()

"""

#Herramientas:
martillo = {
"descripcion": "Martillo de carpintero de 16oz con mango de fibra de vidrio.",
"id": 1001,
"marca": "Stanley",
"precio": 18.500,  
"stock": 10
}

destornillador = {
"descripcion": "Juego de destornilladores Phillips y planos de 6 piezas.",
"id": 1002,
"marca": "Truper",
"precio": 9.200,  
"stock": 5
}

taladro = {
"descripcion": "Taladro inalámbrico de 12V con 2 baterías y cargador.",
"id": 1003,
"marca": "Dewalt",
"precio": 107.000,  
"stock": 3
}

#Materiales:
madera = {
"descripcion": "Tablón de pino de 2x4x8 pies.",
"id": 2001,
"marca": "N/A",
"precio": 6.400,  
"stock": 20
}

cemento = {
"descripcion": "Bolsa de cemento Portland de 50kg.",
"id": 2002,
"marca": "Cemex",
"precio": 5.700,  
"stock": 15
}

ladrillo = {
"descripcion": "Ladrillo hueco de 12x20x30cm.",
"id": 2003,
"marca": "Ladrillera San Marcos",
"precio": 360,  
"stock": 1000
}

#Seguridad:
candado = {
"descripcion": "Candado de acero con llave de 40mm.",
"id": 3001,
"marca": "Master Lock",
"precio": 7.100,  
"stock": 8
}

extintor = {
"descripcion": "Extintor de polvo químico seco de 5 libras.",
"id": 3002,
"marca": "Kidde",
"precio": 28.500,  
"stock": 2
}

casco = {
"descripcion": "Casco de seguridad blanco con suspensión de 4 puntos.",
"id": 3003,
"marca": "3M",
"precio": 10.700,  
"stock": 10
}

#Anclajes y Fijaciones:
tornillo = {
"descripcion": "Caja de 100 tornillos autorroscantes de 3/4x10.",
"id": 4001,
"marca": "Phillips",
"precio": 3.500,  
"stock": 25
}

tuerca = {
"descripcion": "Bolsa de 100 tuercas hexagonales de 1/4",
"id": 4002,
"marca": "Truper",
"precio": 2.100,  
"stock": 50
}

clavo = {
"descripcion": "Caja de 1kg de clavos de acero de 2",
"id": 4003,
"marca": "Stanley",
"precio": 5.700,  
"stock": 15
}

#Medición:
cinta_metrica = {
"descripcion": "Cinta métrica de 5m con graduación en cm y pulgadas.",
"id": 5001,
"marca": "Stanley",
"precio": 7.100,  
"stock": 12
}

nivel = {
"descripcion": "Nivel de burbuja de 24 con 3 vials.",
"id": 5002,
"marca": "Stabila",
"precio": 14.200,  
"stock": 5
}

escuadra = {
"descripcion": "Escuadra de combinación de acero inoxidable de 12",
"id": 5003,
"marca": "Starrett",
"precio": 17.800,  
"stock": 3
}

productos = {
    'herramientas': {
        'martillo': martillo,
        'destornillador': destornillador,
        'taladro': taladro
    },
    'materiales': {
        'madera': madera,
        'cemento': cemento,
        'ladrillo': ladrillo
    },
    'seguridad': {
        'candado': candado,
        'extintor': extintor,
        'casco': casco
    },
    'anclajes': {
        'tornillo': tornillo,
        'tuerca': tuerca,
        'clavo': clavo
    },
    'medicion': {
        'cinta_metrica': cinta_metrica,
        'nivel': nivel,
        'escuadra': escuadra
    }
}

for categoria, productos_dict in productos.items():
    for nombre_producto, producto_dict in productos_dict.items():
        db.child(categoria).child(nombre_producto).set(producto_dict)


for categoria in productos:
    datos_categoria = db.child(categoria).get()
    print(datos_categoria.key())
    print(datos_categoria.val())

diccionario ={
"descripcion": "Martillo de carpintero de 16oz con mango de fibra de vidrio.",
"id": 1001,
"marca": "Stanley",
"precio": 18.500,  
"stock": 20
}

db.child("herramientas").child("martillo_stanley").set(diccionario)
herramientas = db.child("herramientas").get()
print(herramientas.key())
print(herramientas.val())