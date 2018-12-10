import AEStools as at

def decrypt(ctext, rk):
    rnd = []

    s = at.strToList(ctext, 2)
    tRK = rk[10]

    s = at.xorList(s,tRK)
    s = at.shiftColumn(s, 'right')
    s = at.sub(s, at.invSbox)

    s = at.xorList(s,rk[9])
    s = at.mix(s, at.weightInvMC)
    print(s)

    return s