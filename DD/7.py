from math import gcd

def RSA(p: int, q: int, message: int):
    n = p * q
    t = (p - 1) * (q - 1)

    # Find the public exponent e
    for i in range(2, t):
        if gcd(i, t) == 1:
            e = i
            break

    # Find the private exponent d
    j = 0
    while True:
        if (j * e) % t == 1:
            d = j
            break
        j += 1

    # Perform encryption
    ct = (message ** e) % n
    print(f"Encrypted message is {ct}")

    # Perform decryption
    mes = (ct ** d) % n
    print(f"Decrypted message is {mes}")

# User input
p = int(input("Enter the first prime number (p): "))
q = int(input("Enter the second prime number (q): "))
message = int(input("Enter the message to encrypt (as an integer): "))

# Perform RSA encryption and decryption
RSA(p, q, message)
