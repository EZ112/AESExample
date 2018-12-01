import AEStools as at

def encrypt(ptext, rk):
    rnd = []

    s = [ptext[i:i+2] for i in range(0, len(ptext), 2)]
    s = at.generateMatrix(s)
        
    tRK = at.generateMatrix(rk[0])

    s = at.xorList(s, tRK) #xor kedua matrix
    s = at.trans(s) #hasil round key adalah transpose dari matrix yang ada
    s = [s[i:i+2] for i in range(0, len(s), 2)]
    rnd.append(s) #hasil round key 0, makanya yang dimasukkin itu hasil transpose nya

    for j in range(1,len(rk)):
        #pas memproses, harus di-transpose lagi biar yang diproses itu matrix aslinya
        s = at.trans(rnd[j-1])
        s = [s[i:i+2] for i in range(0, len(s), 2)] #dipecah jadi komponen yang berisi 2
        
        s = at.sub(s, at.sbox)
        s = at.shiftRow(s)
        if j != 10: #di terakhir ga lakuin mix column
            s = at.mix(s)
        s = at.xorList(s, at.generateMatrix(rk[j]))
        
        #hasil round key adalah transpose dari matrix yang ada
        s = at.trans(s)
        s = [s[i:i+2] for i in range(0, len(s), 2)]

        rnd.append(s) #hasil round key ke n di mana n >= 1

    
    return "".join(rnd[10])