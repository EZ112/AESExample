#source code
import roundKey

plaintext = "54776F204F6E65204E696E652054776F"
key = "5468617473206D79204B756E67204675"
'''
key = bin(int(key,16))[2:]
key = key.zfill(128)
'''

rk = roundKey.generateRK(key)

print(rk[10]) #round key selesai