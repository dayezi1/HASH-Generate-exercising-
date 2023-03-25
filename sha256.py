import hashlib

def sha256(s256data):
    sha256_object = hashlib.sha256()
    sha256_object.update(s256data.encode('utf-8'))
    sha256_value = sha256_object.hexdigest()
    print('SHA256:', sha256_value)

def md5(d5data):
    md5_object = hashlib.md5()
    md5_object.update(d5data.encode('utf-8'))
    md5_value = md5_object.hexdigest()
    print('MD5:', md5_value)

def sha512(s512data):
    sha512_object = hashlib.sha512()
    sha512_object.update(s512data.encode('utf-8'))
    sha512_value = sha512_object.hexdigest()
    print('SHA512:', sha512_value)

print('This is a Hash transverter, it program only supports MD5, SHA256, SHA512 conversion.')
while True:
    message_1 = input('Please select an algorithm:')
    if message_1.lower() != 'md5' and message_1.lower() != 'sha256' and message_1.lower() != 'sha512':
        print('Please enter the correct algorithm name!')
        continue
    else:
        break

message_2 = input('Please enter the data you want to convert:')
message_3 = 'The data you entered is: ' + message_2
print('\nAlgorithm:', message_1.upper())
if message_1.lower() == 'md5':
    print(message_3)
    md5(message_2)
elif message_1.lower() == 'sha256':
    print(message_3)
    sha256(message_2)
elif message_1.lower() == 'sha512':
    print(message_3)
    sha512(message_2)
