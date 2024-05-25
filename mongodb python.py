from pymongo import MongoClient

    # Establecer conexión con MongoDB
client = MongoClient('mongodb://localhost:27017/')
    
    # Seleccionar la base de datos
db = client['mi_base_de_datos']
    
    # Seleccionar la colección
coleccion = db['mi_coleccion']
    
    # Insertar un documento en la colección
coleccion.insert_one({'nombre': 'Juan', 'edad': 30})
print("Documento insertado.")
    
    # Leer y mostrar todos los documentos de la colección
print("Documentos en la colección:")
for persona in coleccion.find():
    print(persona)
    
    # Actualizar un documento en la colección
coleccion.update_one({'nombre': 'Juan'}, {'$set': {'edad': 31}})
print("Documento actualizado.")
    
    # Leer y mostrar todos los documentos actualizados de la colección
print("Documentos actualizados en la colección:")
for persona in coleccion.find():
    print(persona)
    
    # Eliminar un documento en la colección
    
    # Cerrar la conexión con MongoDB
client.close()

