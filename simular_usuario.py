import random
import uuid
import pandas as pd
from faker import Faker

#1.escoger el pais  y lenguaje para simular datos
fake = Faker('es_co')

#2. sembrar semillas
Faker.seed(42)
random.seed(42)

#3.definir el dato y su tipo a simular
#id (texto (UUID))
#nombre (texto)*
#descripcion (texto)
#area_responsable (texto)

#4.finir el numero de datos a simular (DATASET)
FILAS = 400

#construir funcion generadora de datos
def generar_datos_categoria(numero_registros = FILAS):
   filas=[]
   for _ in range(numero_registros):
        filas.append({
            "id": str(uuid.uuid4()),
            "nombre": fake.word(),
            "descripcion": fake.sentence(),
            "area_responsable": fake.word()
        })
   return filas

# 6. utilizaremos PANDAS para ordenar los datos simulados y crear un dataframe
tabla_ordenada_categoria = pd.DataFrame(generar_datos_categoria())

#7. ensuciar los datos simulados para probar la limpieza de datos
#7.1 generar una funcion que muestre los datos simulados
def generar_muestra():
    return datos.sample(fraccion=porcentaje, random_state=random.randint(0, 9999)).index

#7.2 generar una funcion que ensucie los datos simulados
def ensuciar(datos_df):
    datos_df=datos_df.copy()
    # para el atributo nombre generar el 10% con espacios sobrantes
    subconjunto_datos = generar_muestra(datos_df, 0.1)
    datos_df.loc[subconjunto_datos, 'nombre'] = ""+datos_df.loc[subconjunto_datos, 'nombre']+" "

    #para el atributo nombre generar el 8% con mayusculas
    subconjunto_datos = generar_muestra(datos_df, 0.08)
    datos_df.loc[subconjunto_datos, 'nombre'] = datos_df.loc[subconjunto_datos, 'nombre'].str.upper()

    #para el atributo descripcion generar el 12% de los datos enmayusculas
    subconjunto_datos = generar_muestra(datos_df, 0.12)
    datos_df.loc[subconjunto_datos, 'descripcion'] = datos_df.loc[subconjunto_datos, 'descripcion'].str.upper()


    #para el atributo area_responsable generar el 15% dde los datos con espacios sobrantes
    subconjunto_datos = generar_muestra(datos_df, 0.15)
    datos_df.loc[subconjunto_datos, 'area_responsable'] = ""+datos_df.loc[subconjunto_datos, 'area_responsable']+" "

    #para el atributo area_responsable generar el 5% en none
    subconjunto_datos = generar_muestra(datos_df, 0.05)
    datos_df.loc[subconjunto_datos, 'area_responsable'] = None

    #para el atributo area_responsable generar  variantes de escritura (mayuscula, capital, espaciado)
    def escribir_mal(texto):
        variantes =texto.lower(), texto.upper(), texto.capitalize(), " "+texto+" ", texto.replace("a", "@").replace("e", "3").replace("i", "1").replace("o", "0").replace("u", "v")
