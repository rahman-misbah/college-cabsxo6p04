class ColumnarTranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, key, plaintext):
        plaintext = self.__process_text(plaintext, len(key))
        key = self.__process_key(key)
        key_sequence = self.__create_key_sequence(key)
        rows = self.__create_matrix(plaintext, len(key))

        result = []

        for idx in key_sequence:
            result.extend([row[idx] for row in rows])
        
        return ''.join(result)

    def decrypt(self, key, encrypted_text):
        key = self.__process_key(key)
        key_sequence = self.__create_key_sequence(key)
        index_rows = self.__create_matrix(list(range(len(encrypted_text))), len(key))

        index_sequence = []
        for idx in key_sequence:
            index_sequence.extend([row[idx] for row in index_rows])
        
        result = [None] * len(encrypted_text)

        for e_idx, result_idx in enumerate(index_sequence):     # e_idx -> encrypted_text_index
            result[result_idx] = encrypted_text[e_idx]
        
        return ''.join(result)

        
    
    def __create_matrix(self, text, key_length):
        rows = []
        for i in range(0, len(text), key_length):
            rows.append(text[i:i + key_length])
        
        return rows

    def __process_text(self, text, key_length):
        # Normalize text and key
        text = text.replace(" ", "").upper()
        
        # Add padding if necessary
        padding_length = (key_length - (len(text) % key_length)) % key_length
        text += 'X' * padding_length

        return text
    
    def __process_key(self, key):
        # Normalize key
        key = key.replace(" ", "").upper()
        return key

    
    def __create_key_sequence(self, key):
        pairs = sorted([(ch, i) for i, ch in enumerate(key)])
        key_sequence = [0] * len(key)
        for new_index, (ch, original_index) in enumerate(pairs):
            key_sequence[original_index] = new_index

        return key_sequence




cipher = ColumnarTranspositionCipher()
e_text = cipher.encrypt("hack", "geeksforgeeks")
de_text = cipher.decrypt("hack", e_text)

print("Encrypted Text:", e_text)
print("Decrypted Text:", de_text)