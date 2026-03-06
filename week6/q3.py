# Playfair cipher

class PlayfairCipher:
    def __init__(self, keyword:str):
        self.__keyword = keyword.upper()
        self.__matrix = self.__construct_matrix()
        self.__cache = dict()
    
    # Public Methods
    def clear_cache(self):
        self.__cache.clear()
    
    def encrypt(self, text:str) -> str:
        return self.__transform(text, 1)

    def decrypt(self, text:str) -> str:
        return self.__transform(text, -1)

    # Getters
    @property
    def keyword(self):
        return self.__keyword

    @property
    def matrix(self):
        return self.__matrix
    
    @property
    def cache(self):
        return self.__cache
    
    # Internal Methods
    def __construct_matrix(self) -> list:
        used_characters = set()
        characters = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
        flat_result = []

        for char in self.__keyword:
            if char not in used_characters:
                used_characters.add(char)
                flat_result.append(char)
        
        for char in characters:
            if char not in used_characters:
                used_characters.add(char)
                flat_result.append(char)
        
        return [flat_result[i * 5: i * 5 + 5] for i in range(5)]

    def __coordinate_retriever(self, char: str) -> tuple:
        if char in self.__cache:
            return self.__cache[char]
        
        for r in range(5):
            for c in range(5):
                if self.__matrix[r][c] == char:
                    self.__cache[char] = (r, c)
                    return self.__cache[char]

    def __clean_text(self, plaintext: str) -> str:
        result = plaintext.upper().replace('J', 'I')
        result = ''.join([char for char in result if char.isalpha()])

        pairs = []
        i = 0
        while i < len(result):
            char1 = result[i]

            if i + 1 == len(result):
                if char1 == 'X': pairs.append(char1 + 'Z')
                else: pairs.append(char1 + 'X')
            else:
                char2 = result[i + 1]

                if char1 == char2:
                    if char1 == 'X': pairs.append(char1 + 'Z')
                    else: pairs.append(char1 + 'X')
                else:
                    pairs.append(char1 + char2)
                    i += 1  # Process additional letter if both characters are distinct
            
            i += 1

        return pairs
    
    def __transform(self, text: str, direction: int) -> str:
        if direction == 1:
            pairs = self.__clean_text(text)
        else:
            text = text.upper().replace(" ", "")
            pairs = [text[i:i + 2] for i in range(0, len(text), 2)]
            
        result = []

        for pair in pairs:
            r1, c1 = self.__coordinate_retriever(pair[0])
            r2, c2 = self.__coordinate_retriever(pair[1])

            # Checking same row
            if r1 == r2:
                result.append(self.__matrix[r1][(c1 + direction) % 5])
                result.append(self.__matrix[r2][(c2 + direction) % 5])
            # Checking same column
            elif c1 == c2:
                result.append(self.__matrix[(r1 + direction) % 5][c1])
                result.append(self.__matrix[(r2 + direction) % 5][c2])
            # Rectangle
            else:
                result.append(self.__matrix[r1][c2])
                result.append(self.__matrix[r2][c1])

        return ''.join(result)


cipher = PlayfairCipher('keyword')
encrypted_text = cipher.encrypt('hello world')
print(encrypted_text)