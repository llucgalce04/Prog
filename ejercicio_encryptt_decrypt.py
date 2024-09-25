list = [3,5,7]

squaredNumbers = [x**2 for x in list ]
secretKey = sum(squaredNumbers)
message = "who are you?"

encryptation = [chr(ord(x) + secretKey) for x in message ]
finalResult = "".join(encryptation)
print(finalResult)

messageEncrypted = "\x95ÂÁ·\x7fs\x9d´À¸Æs\x95ÂÁ·"
print(messageEncrypted)

decryptation = [chr(ord(x) - secretKey) for x in messageEncrypted]
decryptedMessage = "".join(decryptation)
print(decryptedMessage)