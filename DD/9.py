pip install cryptography

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives.asymmetric.utils import Prehashed
from cryptography.hazmat.primitives import serialization

# Generate DSA private and public keys
private_key = dsa.generate_private_key(key_size=1024)
public_key = private_key.public_key()

# Message to be signed
message = b"Message for digital signature"

# Signing the message
signature = private_key.sign(message, Prehashed(hashes.SHA256()))

# Verifying the signature
try:
    public_key.verify(signature, message, Prehashed(hashes.SHA256()))
    print("Signature is valid.")
except:
    print("Signature is invalid.")
