def playfair_cipher(text, key, mode='encrypt'):
    key_matrix = [''.join(dict.fromkeys(key.upper().replace('J', 'I') + 'ABCDEFGHIKLMNOPQRSTUVWXYZ'))[i:i+5] for i in range(0, 25, 5)]
    text = ''.join(filter(str.isalpha, text.upper().replace('J', 'I')))
    if len(text) % 2 != 0: text += 'X'

    def find_coordinates(char):
        for row in key_matrix:
            if char in row: return key_matrix.index(row), row.index(char)

    def process_pair(c1, c2, mode):
        if c1[0] == c2[0]:
            return (c1[0], (c1[1] + mode) % 5), (c2[0], (c2[1] + mode) % 5)
        elif c1[1] == c2[1]:
            return ((c1[0] + mode) % 5, c1[1]), ((c2[0] + mode) % 5, c2[1])
        else:
            return (c1[0], c2[1]), (c2[0], c1[1])

    result = ''
    for i in range(0, len(text), 2):
        c1, c2 = find_coordinates(text[i]), find_coordinates(text[i + 1])
        c1, c2 = process_pair(c1, c2, 1 if mode == 'encrypt' else -1)
        result += key_matrix[c1[0]][c1[1]] + key_matrix[c2[0]][c2[1]]

    return result

text = input("Enter the message: ")
key = input("Enter the keyword: ")
mode = input("Enter the mode (encrypt or decrypt): ")

result = playfair_cipher(text, key, mode)
print(f"{'Encrypted' if mode == 'encrypt' else 'Decrypted'} Text: {result}")
