def caesar_cipher(text: str, shift: int) -> str:
    if shift >= 26:
        shift %= 26
    
    alphabets = 'abcdefghijklmnopqrstuvwxys'
    shifted_alphabets = alphabets[shift:] + alphabets[:shift]
    table = str.maketrans(alphabets + alphabets.upper(), shifted_alphabets + shifted_alphabets.upper())
    return text.translate(table)

text = input("Enter text: ")
key = int(input("Key: "))

encrypted = caesar_cipher(text, key)
decrypted = caesar_cipher(encrypted, -key)

print("Encrypted Text:", encrypted)
print("Encrypted Text:", decrypted)