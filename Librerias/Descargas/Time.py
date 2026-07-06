import sys
import datetime

# Obtenemos el comando (ej: "segundos" o "now")
comando = sys.argv[1].lower()
now = datetime.datetime.now()

try:
    if comando == "segundos":
        print(now.second)
    elif comando == "minutos":
        print(now.minute)
    elif comando == "hora":
        print(now.hour)
    elif comando == "dia":
        print(now.day)
    elif comando == "mes":
        print(now.month)
    elif comando == "año":
        print(now.year)
    elif comando == "now":
        print(now.strftime("%Y-%m-%d %H:%M:%S"))
    else:
        print("ComandoDesconocido")
except Exception:
    print("ErrorLib")
