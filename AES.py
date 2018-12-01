#source code
import roundKey, encryptAES, AEStools as at


plaintext = "54776F204F6E65204E696E652054776F"
key = "5468617473206D79204B756E67204675"

rk = roundKey.generateRK(key) #round key selesai

ciphertext = encryptAES.encrypt(plaintext, rk)

print("Plaintext : %s" % plaintext)
print("Ciphertext: %s " % ciphertext)