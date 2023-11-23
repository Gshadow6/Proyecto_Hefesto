""" Programa de menu de conversores, puedes elegir entre conversor de longitud
conversor de tiempo y conversor de velocidad, todas las funciones piden el numero,
la unidad origen y la unidad deseada"""


# Funcion para el conversor de longitud
def conversor_longitud(valor, origen, deseada):
    # Guarda las posibles unidades y sus conversiones (la conversion es a metros) en un diccionario
    """" Para probar: 343 metros = 0.343 kilometros = 34300 centimetros """
    unidades = {'metros': 1, 'kilometros': 1000, 'centimetros': 0.01}
    # Condicion por si no encuentra una unidad en el diccionario
    if origen not in unidades or deseada not in unidades:
        return "Elija una unidad valida: metros, kilometros y centimetros"
    # Formula usado para la conversion y el mensaje para mostrar el resultado
    resultado = valor * unidades[origen] / unidades[deseada]
    return f"{valor} {origen} es igual a {resultado} {deseada}"


# Funcion para elegir el conversor de longitud
def longitud():
    # Pide los valores de la funcion, el numero, la unidad origen y unidad deseada
    valor = float(input("Ingrese el valor a convertir: "))
    origen = input("Ingrese la unidad origen (metros, kilometros, centimetros): ")
    deseada = input("Ingrese la unidad deseada (metros, kilometros, centimetros): ")
    # Se manda a llamar la funcion de conversion y retorna la impresion
    resultado = conversor_longitud(valor, origen, deseada)
    return print(resultado)


# Funcion para el conversor de tiempo
def conversor_tiempo(valor, origen, deseada):
    # Guarda las posibles unidades y sus conversiones (la conversion es a segundos) en un diccionario
    """ Para probar: 90 segundos = 1.5 minutos = 0.025 horas = 0.001 dias = 0.00015 semanas """
    unidades = {'segundos': 1, 'minutos': 60, 'horas': 3600, 'dias': 86400, 'semanas': 604800}
    # Condicion por si no encuentra una unidad en el diccionario
    if origen not in unidades or deseada not in unidades:
        return "Elija una unidad valida: segundos: segundos, minutos, horas, dias y semanas"
    # Formula usado para la conversion y el mensaje para mostrar el resultado
    resultado = valor * unidades[origen] / unidades[deseada]
    return f"{valor} {origen} es igual a {resultado:.5f} {deseada}"


# Funcion para elegir el conversor de tiempo
def tiempo():
    # Pide los valores de la funcion, el numero, la unidad origen y unidad deseada
    valor = float(input("Ingrese la cantidad de tiempo a convertir: "))
    origen = input("Ingrese la unidad de origen (segundos, minutos, horas, dias, semanas): ")
    deseada = input("Ingrese la unidad de destino (segundos, minutos, horas, dias, semanas): ")
    # Se manda a llamar la funcion de conversion y retorna la impresion
    resultado = conversor_tiempo(valor, origen, deseada)
    return print(resultado)


# Funcion para el conversor de velocidad
def conversor_velocidad(valor, origen, deseada):
    # Guarda las posibles unidades y sus conversiones (la conversion es a m/s) en un diccionario
    """ Para probar: 3.601 m/s = 12.96 km/h = 8.055 mph = 7 Nudos """
    unidades = {'m/s': 1, 'km/h': 0.27777, 'mph': 0.44704, 'nudos': 0.514444}
    # Condicion por si no encuentra una unidad en el diccionario
    if origen not in unidades or deseada not in unidades:
        return "Elija una unidad valida: m/s, km/h, mph y nudos"
    # Formula usado para la conversion y el mensaje para mostrar el resultado
    resultado = valor * unidades[origen] / unidades[deseada]
    return f"{valor} {origen} es igual a {resultado:.3f} {deseada}"


# Funcion para elegir el conversor de velocidad
def velocidad():
    # Pide los valores de la funcion, el numero, la unidad origen y unidad deseada
    valor = float(input("Ingrese la velocidad a convertir: "))
    origen = input("Ingrese la unidad de origen (m/s, km/h, mph, nudos): ")
    deseada = input("Ingrese la unidad de destino (m/s, km/h, mph, nudos): ")
    # Se manda a llamar la funcion de conversion y retorna la impresion
    resultado = conversor_velocidad(valor, origen, deseada)
    print(resultado)


# Funcion que simula un switch con un diccionario, se le da la opcion del conversor
def switch(opcion):
    # Se guarda las opciones de conversion en un diccionario
    switch_dict = {
        1: longitud,
        2: tiempo,
        3: velocidad,
    }
    # Retorna del diccionario, el nombre del conversor, y hace un salto a esa funcion
    return switch_dict.get(opcion, default)()


# Funcion por defecto, por si se elige otro numero en el switch
def default():
    return print("Solo hay 3 conversores: 1 conversor de logitud, 2 conversor de tiempo o 3 conversor de velocidad")


# Se pide el numero dependiendo del conversor a usar
opcion = int(input("Ingrese una opción: 1 conversor de logitud, 2 conversor de tiempo o 3 conversor de velocidad: "))
# Se manda a llamar al switch con la opcion ingresada
switch(opcion)
