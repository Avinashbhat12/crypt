import numpy as np

def mod_inverse(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = pow(det, -1, modulus)
    return (det_inv * np.round(det * np.linalg.inv(matrix)).astype(int)) % modulus

def hill_cipher(text, key, mode='encrypt'):
    text = ''.join(filter(str.isalpha, text.upper()))
    key_size = len(key)
    if len(text) % key_size != 0:
        text += 'X' * (key_size - len(text) % key_size)

    key_matrix = np.array(key)
    text_matrix = np.array([[ord(char) - ord('A') for char in text[i:i+key_size]]
                            for i in range(0, len(text), key_size)])

    if mode == 'encrypt':
        result = np.dot(text_matrix, key_matrix) % 26
    elif mode == 'decrypt':
        key_matrix = mod_inverse(key_matrix, 26)
        result = np.dot(text_matrix, key_matrix) % 26
    else:
        raise ValueError("Invalid mode. Choose 'encrypt' or 'decrypt'.")

    return ''.join(chr(num + ord('A')) for row in result for num in row)

text = input("Enter the message: ").replace(" ", "").upper()
key = [list(map(int, input(f"Enter row {i+1} of the key matrix: ").split())) for i in range(2)]
mode = input("Enter the mode (encrypt or decrypt): ")

print("Result:", hill_cipher(text, key, mode))


