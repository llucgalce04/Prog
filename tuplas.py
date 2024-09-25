#Tuplas 
#Ejercicio 1
admin_credentials = ("admin", "root","P@ssw0rd")
lenAdminCredentials = len(admin_credentials)
print(admin_credentials)
print(lenAdminCredentials)

#Ejercicio 2
ports = ("22", "443", "80", "21", "8080")
print(ports[0], ports[3])
for x in ports:
    if x == "22":
        print("The port " + x + " is in the list")
        

#Ejercicio 3
#user_roles = ("admin", "user", "guest")
#user_roles[1] = "superuser"
#print(user_roles)

#Ejercicio 4
server_info = ("192.168.1.10", "web_server", "active")
ip, role, status = server_info
print(ip, role, status)