import AEStools as at

def decrypt(ctext, rk):
    rnd = []

    s = at.strToList(ctext, 2)
    s = at.xorList(s,rk[10])
    
    for i in range(1, len(rk)):
        s = at.shiftColumn(s, 'right')
        s = at.sub(s, at.invSbox)
        
        if (len(rk)-1-i)!= 0:
            s = at.xorList(s,rk[len(rk)-1-i])
            s = at.trans(s)
            s = at.strToList(s, 2)
            s = at.mix(s, at.weightInvMC)
            s = at.trans(s)
            s = at.strToList(s, 2)

    s = at.xorList(s, rk[0])
    return ''.join(s)