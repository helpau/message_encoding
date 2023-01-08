def encode(s:str)->str:
    """Принимает последовательность 0 и 1, возвращает строку в манчестерском кодировании"""
    encodes_s=""
    for bit in s:
        if bit=="0":
            encodes_s+="01"
        else:
            encodes_s+="10"

    return encodes_s