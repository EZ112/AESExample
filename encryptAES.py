import AEStools as at

def encrypt(ptext, rk):
    s = [ptext[i:i+2] for i in range(0, len(ptext), 2)]
    s = at.generateMatrix(s)
    tRK = at.generateMatrix(rk[0])

    s = at.xorList(s, tRK) #xor kedua matrix
    s = at.sub(s) #menggunakan s-box pada state matrix awal
    s = at.shiftRow(s)
    s = at.mix(s)
    print(s)
