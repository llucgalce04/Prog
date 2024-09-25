list = [3,5,7]

squaredNumbers = [x**2 for x in list ]
secretKey = sum(squaredNumbers)
message = "who are you ?"
encriptedList = []
for i in message:
    y = ord(i)
    encript = (y)+ secretKey
    encriptedList.append(encript)

decryptedList = []

for i in encriptedList:
    y = chr(i)
    decryptedList.append(y)
finalResult = "".join(decryptedList)
print(finalResult)
