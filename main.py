import manchester
import nrz
import bipolar_ami
import nrzi
import ec_4b5b
import scramble_3_5
import numpy as np
import matplotlib.pyplot as plt
hex_str="D7E5EFF3F0D8DD20CC2EC02E"
print("Длина строки(байт): ",len(hex_str)//2)
bin_str=bin(int(hex_str,16))[2:].zfill(8)
print(bin_str)

for code in [manchester,nrz,bipolar_ami,nrzi,ec_4b5b,scramble_3_5]:
    name=code.__name__
    enc_str=code.encode(bin_str)
    if "-" in enc_str:
        enc_data=[]
        for i in enc_str:
            if i=="-":
                enc_data.append(-1)
            else:
                enc_data.append(int(i))
    else:
        enc_data=list(map(int,enc_str))
    xs = np.repeat(range(len(enc_data)), 2)
    ys = np.repeat(enc_data, 2)
    xs = xs[1:]
    ys = ys[:-1]
    xs = np.append(xs,xs[-1] + 1)
    ys = np.append(ys, ys[-1])
    plt.figure(figsize=(20,5))
    plt.plot(xs, ys)
    plt.savefig("pics/"+name+".png")
    print(name)
    print(enc_str)