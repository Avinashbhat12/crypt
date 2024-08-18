def caesar_cipher(text, shift, decrypt=False):
    shifted_text = ""
    for char in text:
        if char.isalpha():  # Check if character is a letter
            if decrypt:
                shifted = ord(char) - shift
            else:
                shifted = ord(char) + shift

            if char.islower():
                base = ord('a')
            else:
                base = ord('A')

            shifted = (shifted - base) % 26 + base
            shifted_text += chr(shifted)
        else:
            shifted_text += char  # Non-alphabetical characters remain unchanged
    return shifted_text

# Example usage:
plaintext = input("enter the message:")
shift = int(input("enter key:"))

# Encrypting the plaintext
encrypted_text = caesar_cipher(plaintext, shift)
print("Original:", plaintext)
print("Encrypted:", encrypted_text)

# Decrypting the encrypted text
decrypted_text = caesar_cipher(encrypted_text, shift, decrypt=True)
print("Decrypted:", decrypted_text)
