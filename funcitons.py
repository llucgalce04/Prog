'''def block_ip(ip):
    blocked_Ip = ["192.168.1.5", "10.0.0.2", "203.0.113.7"]
    if ip in blocked_Ip:
        print("Ip Malita")
    else:
        print("Ip buenita")
block_ip("192.168.2.5")

def  check_vulnerability(log_entry):
    if "vulnerability" in log_entry:
        print("Mal")
    else:
        print("Bien")

check_vulnerability("Hola vulnerability")

def has_sql_injection(query):
    SQLI = [" ' OR '1'='1"]
    
    if "' OR '1'='1" in query:
        return True
    else:
        return False
    
has_sql_injection("' OR '1'='1")

def detect_dos(ip, traffic):
    if traffic > 1000:
        print(f'Potenial Dos in for this IP: {ip}')
    else:
        print(f'Traffic for this Ip {ip} correct the traffic is {traffic} and is lower then 1000')
    
detect_dos(192, 1000000)
'''
