# Aqui es donde obtenemos la cantidad de personas
personas = int(input( '¡Hola! bien venido a la calculadore IMC, cuantas personas son: '))

# Aqui verificamos que la cantidad sea mayor a 0 si no, no tiene sentido pedir nada
while personas > 0:
# Pedimos los datos de la persona 
    nombre = input ('Introduce tu(s) nombre(s): ')
    apellidoP = input ('Introduce tu apellido Paterno: ')
    apellidoM = input ('Introduce tu apellido Materno: ')
    edad = int (input ('Introduce tu edad: '))
    altura = float (input ('Introduce tu altura en metros: '))
    kilos = float (input('Introduce tu peso en kilogramos por favor :'))
    correo = input ('Introduce tu correo electrónico: ')
    telefono = input ('Introduce tu número telefónico: ')

    # Calculo del IMC, masa (En kilogramos) entre la estatura (En metros) elevada al cuadrado
    m = kilos
    est = altura
    IMC = m / est**2

    # Le decimos si es menor o mayor de edad, si es menor a 18 es menor, si no es mayor edad
    if edad < 18 and edad >= 1 :
        print ('¡Hola!: '+ nombre +' '+ apellidoP +' '+ apellidoM)
        print ('¡Eres menor de edad!')
        print ('Tu IMC es el siguiente: '+ str(IMC))
    elif edad >=18 and edad <= 100 :
        print ('¡Hola!: '+ nombre +' '+ apellidoP +' '+ apellidoM)
        print ('¡Eres mayor de edad!')
        print ('Tu IMC es el siguiente: '+ str(IMC))
    else:
          print ('¡Edad no válida!')

    #Hacemos las distintas validaciones
    if IMC >= 0 and IMC <= 15.99 :
        print ("Delgadez severa")
    elif IMC >= 16.00 and IMC <= 16.99 :
        print ("Delgadez moderada")
    elif IMC >= 17.00 and IMC <= 18.49:
        print ("Delgadez leve")
    elif IMC >= 18.50 and IMC <= 24.99 :
        print ("Normal")
    elif IMC >= 25.00 and IMC <= 29.99:
        print ("Sobrepeso")
    elif IMC >= 30.00 and IMC <= 34.99:
        print ("obesidad leve")
    elif IMC >= 35.00 and IMC <= 39.00:
        print ("obesidad media")
    elif IMC >= 40.00:
        print ("obesidad morbida")
    
    # Validamos los 10 digitos telefonicos ingresado
    caracter = len (telefono)
    
    if (caracter) >=1 and (caracter)<=10:
        print ('Mandamos el resultado al número telefónico siguiente: ' +str(telefono))
    else:
        print ('El número telefónico no es válido')

    # Validamos el correo electrónico ingresado
    if '@' in correo:
        print ('Mandamos el resultado al correo electrónico: %s' %(correo))
    else:
        print ('El correo electrónico no es válido')
    
    # cerramos el ciclo si no se vuelve infinito

    personas = personas - 1
