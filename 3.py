import re

def validarEmail():
    correo = input("Ingresa tu correo: EJ: david@gmail.com: ")
    # Use regex para validar el correo
    if re.match(r'^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,4}$',correo.lower()):
        
        print("El correo es válido")
    else:
        print("El correo no es válido, usa: david@gmail.com ")

validarEmail()