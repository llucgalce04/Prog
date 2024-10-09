'''dangerous_words = ["attack", "malware"]
packet_log = [
    "GET /index.html",
    "malware detected in POST request",
    "Checking for updates",
    "Potential attack detected in payload",
    "Normal traffic"
]

for log in packet_log:
    isBlocked = False
    for word in dangerous_words:
        if word in log:
            isBlocked = True
    
    if isBlocked == True:
        print("Blocked")
    else:
        print("All good")

# Hardcoded log of access attempts

maxAttempts = 3
count = 0
for ip in set(access_attempts):
    if access_attempts.count(ip) > maxAttempts:
        count += 1

print("Number of flagged IP's: ",count)
'''
access_attempts = ["192.168.0.1", "192.168.0.1", "192.168.0.2", "192.168.0.1",
                   "192.168.0.2", "192.168.0.2", "192.168.0.3", "192.168.0.3", "192.168.0.2"]
info_ip = {}
count = 0
for ip in access_attempts:
    if ip in info_ip:
        info_ip[ip] += 1
    else:
        info_ip[ip] = 1

for key in info_ip.keys():
    if info_ip[key] > 3:
        count += 1
print(f'Number of flagged IPs: {count}')
print (info_ip)