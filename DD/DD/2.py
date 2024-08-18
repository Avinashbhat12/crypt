def affine_encrypt(text, a, b):
    return ''.join([chr(((a * (ord(char) - ord('A')) + b) % 26) + ord('A'))
                    if char.isupper()
                    else chr(((a * (ord(char) - ord('a')) + b) % 26) + ord('a'))
                    if char.islower()
                    else char
                    for char in text])

def affine_decrypt(text, a, b):
    return ''.join([chr(((pow(a, -1, 26) * ((ord(char) - ord('A')) - b)) % 26) + ord('A'))
                    if char.isupper()
                    else chr(((pow(a, -1, 26) * ((ord(char) - ord('a')) - b)) % 26) + ord('a'))
                    if char.islower()
                    else char
                    for char in text])

# Example usage:
if __name__ == "__main__":
    text = input("Enter the message: ")
    a = int(input("Enter the value of a (must be coprime with 26): "))
    b = int(input("Enter the value of b: "))

    encrypted_text = affine_encrypt(text, a, b)
    print("Encrypted Text:", encrypted_text)

    decrypted_text = affine_decrypt(encrypted_text, a, b)
    print("Decrypted Text:", decrypted_text)
