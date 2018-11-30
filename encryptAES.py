import AEStools as at

def encrypt(ptext, rk):
    s = [ptext[i:i+2] for i in range(0, len(ptext), 2)]
    s = at.generateMatrix(s)
    tRK = at.generateMatrix(rk[0])

    s = at.xorList(s, tRK)
    
    print(s)
