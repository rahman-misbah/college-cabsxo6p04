def crypt(data: str, key: int) -> str:
    data = data.encode()
    crypted_text = bytes([i ^ key for i in data])
    return crypted_text.decode()

data = input("Enter a string: ")
key = int(input("Enter a key: "))
encrypted = crypt(data, key)
decrypted = crypt(encrypted, key)

print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")