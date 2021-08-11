from cryptography.fernet import Fernet
import sys
cipher_suite = Fernet(b'dUwSYoeocAvCSVvefxBlmZlDnda-dS1b0ffQkFCWRL4=')

class Algo:
    def encode(self):
        encoded_text = cipher_suite.encrypt(bytes(sys.argv[2], encoding='utf-8'))
        return encoded_text
    def decode(self):
        decoded_text = cipher_suite.decrypt(bytes(sys.argv[2], encoding='utf-8'))
        return decoded_text

obj=Algo()
if sys.argv[1] == 'encode':
    print(obj.encode())
elif sys.argv[1] == 'decode':
    print(obj.decode())
else:
    print("Wrong command...")