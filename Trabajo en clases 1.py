fecha = input("Ingrese la fecha que desea consultar, con el siguiente formato 'jueves, 23/02: ").lower()
dia_semana = fecha[0: fecha.find(",")]
dia = fecha[fecha.find(" ")+1 : fecha.find("/")]
mes = fecha[fecha.find("/")+1 :]
#filtramos los ingresos incorrectos
if int(dia) < 0 or int(dia) > 31:
    print("Ingresó un día incorrecto")
elif int(mes) < 0 or int(mes) > 12:
    print("Ingresó un mes incorrecto")
elif dia_semana not in ["lunes", "martes", "miercoles", "jueves", "viernes"]:
    print("Ingresó un día de la semana incorrecto")
else:
    #Si es lunes nivel inicial
    if dia_semana == "lunes":
        examenes = input("Ingrese si hubo exámenes en el nivel inicial S (sí) o N (no): ").lower()
        if examenes == "s":
            cant_alumnos = int(input("Ingrese la cantidad de alumnos que rindieron: "))
            cant_aprobados = int(input("Ingrese la cantidad de alumnos que aporbaron: "))
            print("El porcentaje de alumnos iniciales aprobados es: ",(cant_aprobados *100)/cant_alumnos,"%")
        else:
            print("Hoy las clases se desarrollaron con normalidad en el nivel inicial")
    #Si es martes nivel intermedio
    if dia_semana == "martes": 
        examenes = input("Ingrese si hubo exámenes en el nivel intermedio S (sí) o N (no): ").lower()
        if examenes == "s":
            cant_alumnos = int(input("Ingrese la cantidad de alumnos que rindieron: "))
            cant_aprobados = int(input("Ingrese la cantidad de alumnos que aporbaron: "))
            print("El porcentaje de alumnos intermedios aprobados es: ",(cant_aprobados *100)/cant_alumnos,"%")
        else:
            print("Hoy las clases se desarrollaron con normalidad en el nivel intermedio")        
    #Si es lunes nivel avanzados
    if dia_semana == "miercoles":  
        examenes = input("Ingrese si hubo exámenes en el nivel avanzado S (sí) o N (no): ").lower()
        if examenes == "s":
            cant_alumnos = int(input("Ingrese la cantidad de alumnos que rindieron: "))
            cant_aprobados = int(input("Ingrese la cantidad de alumnos que aporbaron: "))
            print("El porcentaje de alumnos avanzados aprobados es: ",(cant_aprobados *100)/cant_alumnos,"%")
        else:
            print("Hoy las clases se desarrollaron con normalidad en el nivel avanzado")
    if dia_semana == "jueves":
        cupo = int(input("Ingrese la cantidad total de alumnos"))
        asistencia = int(input("Ingrese la cantidad de almnos que asistieron: "))
        if asistencia > (cupo / 2):
            print("La asistencia fue mayor al 50% ")
        else:
            print("La asistencia fue menor al 50% ")
    if dia_semana == "viernes" or (dia == "01" and mes == "01") or (dia == "01" and mes == "07") :
        if dia == "01" and mes == "01":
            cantidad_ingresantes = int(input("Ingrese la cantidad de ingresantes: "))
            arancel = float(input("Ingrese el arancel en $ que se cobrará: "))
            print("El ingreso en cash total es: $",(cantidad_ingresantes*arancel))
        elif dia == "01" and mes == "07":
            cantidad_ingresantes = int(input("Ingrese la cantidad de ingresantes: "))
            arancel = float(input("Ingrese el arancel en $ que se cobrará: "))
            print("El ingreso en cash total es: $",(cantidad_ingresantes*arancel))
        else:
            print("Hoy cursan los viajeros, disfrute su clase.")