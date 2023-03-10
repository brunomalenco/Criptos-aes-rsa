import random, os, base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

class Criptografia():

    def __init__(self, key=None, iv=None):
        if key == None:
            self.key = os.urandom(32)
        else:
            self.key = key

        if iv == None:
            self.iv = os.urandom(16)
        else:
            self.iv = iv
        
        self.cipher = Cipher(algorithms.AES(self.key), modes.CBC(self.iv))

    def criptografando(self, message):
        message = base64.b64encode(message.encode()).decode()
        for i in range(16 - len(message) % 16):
            message += " "
        encryptor = self.cipher.encryptor()
        return encryptor.update(message.encode("utf-8") + encryptor.finalize())

aes = Criptografia()
print(aes.criptografando("Mensagem Criptografada"))