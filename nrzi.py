def encode(s:str)->str:
    "Принимает последовательность 0 и 1,возвращает строку из 0 и 1, инверсия по 1"
    encoded_str=""
    symbols=["0","1"]
    for bit in s:
        if bit=="1":
            symbols=symbols[::-1]
            encoded_str+=symbols[0]
        else:
            encoded_str+=symbols[0]
    return encoded_str