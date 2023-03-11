import datetime

# Solicitar al usuario que ingrese el hemisferio (norte o sur) y el día del mes
hemisferio = input("Ingrese el hemisferio (norte o sur): ")
dia = int(input("Ingrese el día del mes (1-31): "))

# Crear un objeto ephem para la fecha y la hora actual
fecha_actual = datetime.date();

# Calcular la fecha del solsticio de verano y de invierno para el año actual, según el hemisferio
if hemisferio == "norte":
    solsticio_verano = datetime.next_summer_solstice(fecha_actual)
    solsticio_invierno = datetime.next_winter_solstice(fecha_actual)
elif hemisferio == "sur":
    solsticio_verano = datetime.next_winter_solstice(fecha_actual)
    solsticio_invierno = datetime.next_summer_solstice(fecha_actual)
else:
    print("Hemisferio no válido.")
    exit()

# Determinar la época del solsticio para el día especificado
if fecha_actual < solsticio_verano and fecha_actual >= solsticio_invierno:
    print("Estamos en invierno.")
else:
    print("Estamos en verano.")
