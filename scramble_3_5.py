def encode(s:str)->str:
    encoded_str=s[0:3]
    for i in range(3,len(s)):
        bit=int(s[i])^int(s[i-3])^int(s[i-5])
        encoded_str+=str(bit)
    return encoded_str