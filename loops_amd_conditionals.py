'''#Ejercicio 1
#Write a script that asks the user for a password and a verification code. If both are correct, grant access; otherwise, deny access.
#To get access, the user has to input the password and the verificantion code "securePass123" and "42" . Otherwise, the access should be denied
#tip : verify the logical statement AND

# Inputs for password and verification code
#password =  '@enti.cat'

# correct information conditions
correct_password = "securePass123"
correct_code = "42"

# Implement here if-elif-else logic 

password = str(input("Introduce tu contraseña: "))
while True:
    if password != correct_password:
        print ("Contraseña Incorrecta, vuelve a intentar")
        password = input("Introduce tu contraseña: ")
    else:
        print("Contrasenya Correcta!!")
        verification_code = input("Introduce tu codigo de verificacion: ")

        if verification_code == correct_code:
            print ("Codigo de verificacion correcto, ole ole lo caracole")
            break
        else:
            print("Codigo Incorrecto!!")
            verification_code = input("Introduce tu codigo de verificacion: ")

#Ejercicio 2
#Store information about the user here

user_data = {'ze_pqn': {'File1': 'r', 'File2':'r'}}
permission = {'File1':'r', 'File2':['w', 'x']}

# information given by user
username = "ze_pqn"
file_to_access ='File2'

#Obtenemos los permisos requeridos segun el archivo
permision_list = permission.get(file_to_access)
#Obtenemos los permisos que tiene el usuario y en que archivo tiene los permisos
getUsernamePermisionforFile = user_data.get(username)
#Obtenemos del usuario que queremos los permisos segun el archivo
info = getUsernamePermisionforFile.get(file_to_access)

if permision_list == info :
   print("Puede Acceder")
else: 
    print("No puede acceder")

#Ejercicio 3
ip_log = [
    "192.168.0.1", "10.0.0.5", "192.168.0.2", "10.0.0.6", "203.0.113.5", "192.168.1.1", 
    "172.16.0.1", "10.0.0.7", "192.168.1.2", "172.16.0.2", "192.168.0.3", "10.0.0.8", 
    "172.16.0.3", "192.168.1.3", "10.0.0.9", "203.0.113.6", "192.168.0.4", "10.0.0.10", 
    "172.16.0.4", "192.168.1.4", "10.0.0.11", "192.168.0.5", "10.0.0.12", "172.16.0.5", 
    "192.168.1.5", "10.0.0.13", "192.168.0.6", "10.0.0.14", "172.16.0.6", "192.168.1.6", 
    "10.0.0.15", "192.168.0.7", "10.0.0.16", "172.16.0.7", "192.168.1.7", "10.0.0.17", 
    "192.168.0.8", "10.0.0.18", "172.16.0.8", "192.168.1.8", "10.0.0.19", "192.168.0.9", 
    "10.0.0.20", "172.16.0.9", "192.168.1.9", "10.0.0.21", "192.168.0.10", "10.0.0.22", 
    "172.16.0.10", "192.168.1.10", "10.0.0.23", "192.168.0.11", "10.0.0.24", "172.16.0.11", 
    "192.168.1.11", "10.0.0.25", "192.168.0.12", "10.0.0.26", "172.16.0.12", "192.168.1.12", 
    "10.0.0.27", "192.168.0.13", "10.0.0.28", "172.16.0.13", "192.168.1.13", "10.0.0.29", 
    "192.168.0.14", "10.0.0.30", "172.16.0.14", "192.168.1.14", "10.0.0.31", "192.168.0.15", 
    "10.0.0.32", "172.16.0.15", "192.168.1.15", "10.0.0.33", "192.168.0.16", "10.0.0.34", 
    "172.16.0.16", "192.168.1.16", "10.0.0.35", "192.168.0.17", "10.0.0.36", "172.16.0.17", 
    "192.168.1.17", "10.0.0.37", "192.168.0.18", "10.0.0.38", "172.16.0.18", "192.168.1.18", 
    "10.0.0.39", "192.168.0.19", "10.0.0.40", "172.16.0.19", "192.168.1.19", "10.0.0.41"
]
contador = -1
for i in ip_log:
    contador += 1
    if i == "203.0.113.5":
        print("Dangerous Ip 203.0.113.5 found in the log")
        print("Esta en la poscion", contador)
        break

# Password to checker
uppercase = 0
lowercase = 0
isdigit = 0
specialCharacters = 0
passwordLen = 0

password = 'B49Dh2qyRwXnn8e75Z4SAd#'
if len(password) >= 8:
    passwordLen += 1
special_characters = ["!","@", "#", "$", "%", "^", "&", "*", "()"]

#countCharacters = []

for i in password:
    #countCharacters.append(i)
    if i.isupper() == True:
        uppercase += 1
    elif i.islower() == True:
        lowercase += 1
    elif i.isdigit() == True:
        isdigit += 1
    elif i in special_characters:
        specialCharacters += 1
#if len(countCharacters) < 8:
#   print("No tiene los 8 caracteres como minimo")
#else:
#    print("All good")

if uppercase and lowercase and isdigit and specialCharacters and passwordLen >= 1:
    print("Estan todas las condiciones")
else:
    print("No estan todas las condiciones")

# Correct password (hardcoded for this exercise)
correct_password = "secure123"

# Simulated list of password attempts (in a real scenario, these would be user inputs)
attempts = ["password", "12345", "secure123",]
index = 0
attempts_limit = 3
while index < len(attempts):
    if correct_password in attempts:
        print("ole ole")
        break
    else:
        print("No ole")
        index += 1
    
if index >=attempts_limit:
    print("Account Locked")

# Simulated login attempts: 0 indicates failure, 1 indicates success
login_attempts = [0, 0, 0, 1, 0, 0, 0, 0, 1]

consecutive_failure = 0
index = 0

while index < len(login_attempts) and consecutive_failure < 3:
    attempt = login_attempts[index]
    if attempt == 0:
        consecutive_failure += 1

        print(f"Fallo de incio de sesion. Fallos consecutivos:{consecutive_failure}")
    else:
        consecutive_failure = 0
        print("Inicio de sesion correcto. Contador de fallos reiniciado")
    
    index += 1
if consecutive_failure == 3:
    print("Cuenta bloqueda debido a 3 intentos fallidos consecutivos")
'''

# Simulated blocklist of malicious IP addresses
blocklist = ["192.168.1.100", "10.0.0.5", "203.0.113.50", "172.16.0.2"]

# Incoming traffic data: each entry contains an IP and a list of packets (as strings)
traffic_log = [
    {"ip": "192.168.0.1", "packets": ["GET /index.html", "Host: example.com", "Data: harmless"]},
    {"ip": "10.0.0.5", "packets": ["attack on port 22", "Host: compromised.com"]},
    {"ip": "172.16.0.2", "packets": ["Data: normal traffic", "Host: normal.com"]},
    {"ip": "203.0.113.5", "packets": ["Data: harmless", "phishing attempt detected", "Host: phishing.com"]},
    {"ip": "192.168.1.10", "packets": ["GET /admin", "malware detected", "Host: danger.com"]},
    {"ip": "192.168.0.15", "packets": ["POST /upload", "Data: user login", "Host: safe.com"]}
]

# Keywords considered suspicious
suspicious_keywords = ["attack", "malware", "phishing"]

index = 0
while index != len(traffic_log):
    attempt = traffic_log[index].get("ip")
    if attempt in blocklist:
        print(f"Ip {attempt} bloqueada")
    else:
        trafficInfo = traffic_log[index].get("packets")
        if any(keyword in packet for packet in trafficInfo for keyword in suspicious_keywords):
            print("Investigación sobre", attempt)

    index+=1
