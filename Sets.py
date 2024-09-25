#Ejercicio 1 Crear detected_ips y printar todo el set entero para ver que no se repiten valroes
detected_ips = {"192.168.1.1", "10.0.0.2", "192.168.1.1"}
print("Todas las ips de detected_ips", detected_ips)

#Ejercicio 2 Crear insecure y secure ips
secure_ips = {"192.168.1.1", "10.0.0.2"}
insecure_ips = {"10.0.0.2", "172.16.0.1"}

print("Todas las ips y las que estan repetidas en los dos sets solo se muestran una vez", secure_ips | insecure_ips)
print("Todos los que se encuentran en los dos sets", secure_ips & insecure_ips)

#Ejercicio 3
print("Las ips que son distintas entre secure a insecure" , secure_ips - insecure_ips)

#Ejercicio 4
known_hashes = {"abc123", "def456", "ghi789"}
suspicious_hashes = {"ghi789", "xyz123", "abc123"}

print("Los que estan en los dos sets", known_hashes & suspicious_hashes)
print("Los que estan en suspcious pero no en known", suspicious_hashes - known_hashes)