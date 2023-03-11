#represa hidrohituango


nivelAgua = int(input("Ingrese por favor el nivel del agua: "))

#proceso
if nivelAgua >= 0 and nivelAgua <= 250:
    print(f"El sensor marca {nivelAgua}, muy bajo... ")
elif nivelAgua >250 and nivelAgua <=400:
    print(f"El sensor marca {nivelAgua}, operando normal ")
else: 
    print(f"El sensor marca {nivelAgua}, Corra hpta ")
