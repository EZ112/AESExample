import AEStools as at

def decrypt(ctext, rk):
    rnd = []

    s = at.strToList(ctext, 2)
    tRK = rk[10]

    s = at.xorList(s,tRK)
    s = at.generateMatrix(s)
    s = at.shiftRow(s, "right")
    s = at.generateMatrix(s)
    s = at.sub(s, at.invSbox)
    print(s)
    

    return s