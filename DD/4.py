def polyalphabetic_cipher(text, key, mode='encrypt'):
    key = key.upper()
    text = ''.join(filter(str.isalpha, text.upper()))
    return ''.join(
        chr((ord(c) - ord('A') + (1 if mode == 'encrypt' else -1) * (ord(key[i % len(key)]) - ord('A'))) % 26 + ord('A'))
        for i, c in enumerate(text)
    )

text = input("Enter the message: ")
key = input("Enter the keyword: ")
mode = input("Enter the mode (encrypt or decrypt): ")

result = polyalphabetic_cipher(text, key, mode)
print(f"{'Encrypted' if mode == 'encrypt' else 'Decrypted'} Text: {result}")


