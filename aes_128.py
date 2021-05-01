from Crypto.Cipher import AES
from secrets import token_bytes
import time

key = token_bytes(16)
#print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()

def encript(msg):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(msg.encode('ascii'))
    return nonce, ciphertext, tag

def decript(nonce, ciphertext, tag):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext.decode('ascii')

msg = "Please Encript Me"

i = 0
while i < 10000:
    nonce, ciphertext, tag = encript(msg)
    plaintext = decript(nonce, ciphertext, tag)
    i += 1

#nonce, ciphertext, tag = encript(msg)
#plaintext = decript(nonce, ciphertext, tag)
#print(f'Key: {key}')
#print(f'Cipher text: {ciphertext}')
#print(f'Plain text: {plaintext}')
print("--- %s seconds ---" % (time.time() - start_time))
print("AES-128")