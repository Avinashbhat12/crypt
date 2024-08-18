def autokey_cipher(plaintext, key, mode='encrypt'):
    key = key.upper()
    plaintext = plaintext.upper()
    result = ""

    if mode == 'encrypt':
        for i in range(len(plaintext)):
            if plaintext[i].isalpha():
                key_char = key[i % len(key)]
                shift = ord(key_char) - ord('A')
                encrypted_char = chr(((ord(plaintext[i]) + shift - ord('A')) % 26) + ord('A'))
                result += encrypted_char
            else:
                result += plaintext[i]
    elif mode == 'decrypt':
        for i in range(len(plaintext)):
            if plaintext[i].isalpha():
                key_char = key[i % len(key)]
                shift = ord(key_char) - ord('A')
                decrypted_char = chr(((ord(plaintext[i]) - shift - ord('A')) % 26) + ord('A'))
                result += decrypted_char
            else:
                result += plaintext[i]

    return result

# Example usage:
plaintext = input("Enter the message: ")
key = input("Enter the key: ")
mode = input("Enter the mode (encrypt or decrypt): ")

result = autokey_cipher(plaintext, key, mode)
print(f"{'Encrypted' if mode == 'encrypt' else 'Decrypted'} Text: {result}")

