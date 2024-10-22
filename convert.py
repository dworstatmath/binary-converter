import math
def dectobi(dec):
    dec=int(dec)
    bi = ""
    if dec != 0:
        for i in range(math.ceil(math.log2(dec))):
            if (dec%(2**(i+1)))-(dec%(2**i)) == 2**i:
                bi+="1"
            else:
                bi+="0"
    else: 
        bi = "0"
    bi = bi[::-1]
    return[int(bi)]
def bitodec(bi):
    bi2=bi[::-1]
    dec=0
    for i in range(len(bi2)):
        if int(bi2[i]) == 1:
            dec+=2**i
    return dec
print(bitodec("10101"))