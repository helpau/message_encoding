def encode(s:str)->str:
    "Принимает последовательность 0 и 1,возвращает строку из символов set([-,0,1])"
    next_positive=True
    encoded_str=""
    for bit in s:
        if bit=="1":
            if next_positive:
                encoded_str+="1"
            else: 
                encoded_str+="-"
            next_positive=not(next_positive)
        else:
            encoded_str+="0"
    return encoded_str