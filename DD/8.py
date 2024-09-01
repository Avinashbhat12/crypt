from Crypto.Cipher import DES
from secrets import token_bytes

key = token_bytes(8)

def encrypt(msg):
  cipher = DES.new(key, DES.MODE_EAX)
  nonce = cipher.nonce
  ciphertext, tag = cipher.encrypt_and_digest(msg.encode('ascii'))
  return nonce, ciphertext, tag

def decrypt(nonce, ciphertext, tag):
  cipher = DES.new(key, DES.MODE_EAX, nonce=nonce)
  plaintext = cipher.decrypt(ciphertext)
  
  try:
      cipher.verify(tag)
      return plaintext.decode('ascii')
  except: 
      return False
        
# Correctly unpack the return values from encrypt()
nonce, ciphertext, tag = encrypt(input('Enter a message:')) 
plaintext = decrypt(nonce, ciphertext, tag)
 
print(f'Cipher text: {ciphertext}') # Now ciphertext is defined

if not plaintext:
    print('message is corrupted!')
else:
    print(f'Plain text: {plaintext}')
