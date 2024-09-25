#Ejercicio 1 Crear diccionario i printarlo entero
firewall_rules =  {
    "inbound" : ["SSH", "HTTPS"],
    "outbound" :["DNS", "SMTP"]
}
print(firewall_rules)

#Ejercicio 2 Acceder al diccionario anterior y printar el inbound y el outbound
# y luego con el get acceder a la key blocked que no existe
print(firewall_rules.get("inbound"), firewall_rules.get("outbound"), firewall_rules.get("blocked"))

#Ejercicio 3 Crear una nueva key que se llame blocked y despues añadir valores en este
# para luego printarlo
firewall_rules["blocked"] = ["FTP", "Telnet"]
print(firewall_rules)

#Ejercicio 4 Crear un nuevo diccionario e ir añadiendo los valores a las keys
# correspondientes, actualizar la tupla para añadir la key brute force y su valor
attack_signatures = {
    "SQL Injection" : "SQL Query",
    "Cross-Site Scripting (XSS)" : "JavaScript code",
    "Denial of Service" : "Traffic Overload"
}
attack_signatures["Brute Force"] = "Password Craking"
print(attack_signatures)