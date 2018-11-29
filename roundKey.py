sbox = [	
    "63",	"7c",	"77",	"7b",	"f2",	"6b",	"6f",	"c5",	"30",	"01",	"67",	"2b",	"fe",	"d7",	"ab",	"76",
    "ca",	"82",	"c9",	"7d",	"fa",	"59",	"47",	"f0",	"ad",	"d4",	"a2",	"af",	"9c",	"a4",	"72",	"c0",
    "b7",	"fd",	"93",	"26",	"36",	"3f",	"f7",	"cc",	"34",	"a5",	"e5",	"f1",	"71",	"d8",	"31",	"15",
    "04",	"c7",	"23",	"c3",	"18",	"96",	"05",	"9a",	"07",	"12",	"80",	"e2",	"eb",	"27",	"b2",	"75",
    "09",	"83",	"2c",	"1a",	"1b",	"6e",	"5a",	"a0",	"52",	"3b",	"d6",	"b3",	"29",	"e3",	"2f",	"84",
    "53",	"d1",	"00",	"ed",	"20",	"fc",	"b1",	"5b",	"6a",	"cb",	"be",	"39",	"4a",	"4c",	"58",	"cf",
    "d0",	"ef",	"aa",	"fb",	"43",	"4d",	"33",	"85",	"45",	"f9",	"02",	"7f",	"50",	"3c",	"9f",	"a8",
    "51",	"a3",	"40",	"8f",	"92",	"9d",	"38",	"f5",	"bc",	"b6",	"da",	"21",	"10",	"ff",	"f3",	"d2",
    "cd",	"0c",	'13',	"ec",	"5f",	'97',	"44",	"17",	"c4",	"a7",	"7e",	"3d",	"64",	"5d",	"19",	"73",
    "60",	"81",	"4f",	"dc",	"22",	"2a",	"90",	"88",	"46",	"ee",	"b8",	"14",	"de",	"5e",	"0b",	"db",
    "e0",	"32",	"3a",	"0a",	"49",	"06",	"24",	"5c",	"c2",	"d3",	"ac",	"62",	"91",	"95",	"e4",	"79",
    "e7",	"c8",	"37",	"6d",	"8d",	"d5",	"4e",	"a9",	"6c",	"56",	"f4",	"ea",	"65",	"7a",	"ae",	"08",
    "ba",	"78",	"25",	"2e",	"1c",	"a6",	"b4",	"c6",	"e8",	"dd",	"74",	"1f",	"4b",	"bd",	"8b",	"8a",
    "70",	"3e",	"b5",	"66",	"48",	"03",	"f6",	"0e",	"61",	"35",	"57",	"b9",	"86",	"c1",	"1d",	"9e",
    "e1",	"f8",	"98",	"11",	"69",	"d9",	"8e",	"94",	"9b",	"1e",	"87",	"e9",	"ce",	"55",	"28",	"df",
    "8c",	"a1",	"89",	"0d",	"bf",	"e6",	"42",	"68",	"41",	"99",	"2d",	"0f",	"b0",	"54",	"bb",	"16"
]

#karena kunci 128 bit, maka dilakukan hingga 10 kali
#dari wikipedia, https://en.wikipedia.org/wiki/Rijndael_key_schedule
def generateRCon():
    out = []
    temp = []
    rc = "01"
    cek = "80"

    temp.append(rc)

    for i in range(1,10):
        
        if int(temp[i-1],16) < int(cek,16):
            temp.append(2 * int(temp[i-1],16))
        else:
            temp.append((2 * int(temp[i-1],16)) ^ int("11B",16))
        temp[i] = hex(int(temp[i]))
        temp[i] = temp[i][2:]
        temp[i] = temp[i].upper()
        temp[i] = temp[i].zfill(2)
    
    for i in range(10):
        out.append([temp[i], "00", "00", "00"])

    return out  

def xor(left, right):
    temp = int(left,16) ^ int(right,16)
    temp = hex(temp)
    temp = temp[2:]
    temp = temp.upper()
    temp = temp.zfill(2)
    return temp


#geser 1 ke kiri
def leftShift(w):
    a = []

    for i in range(4):
        a.append(w[(i+1)%4])

    return a

#memakai s-box
def sub(bit):
    temp = []

    for i in range(len(bit)):
        idx = int(bit[i],16)
        out = sbox[idx]
        out = out.upper()
        temp.append(out)
    
    return temp

#fungsi g, meng-xor list A dengan list B
def g(A, B):
    aL = []
    for i in range(len(A)):
        temp = xor(A[i],B[i])
        aL.append(temp)
    return aL


def generateRK(key):
    w = [key[i:i+8] for i in range(0,len(key), 8)] #key dibagi menjadi 4 bagian

    #tiap w[i] dibagi menjadi 4 bagian lagi
    for i in range(len(w)):
        temp = w[i]
        w[i] = [temp[j:j+2] for j in range(0,len(w[i]), 2)]
    
    for idx in range(10):
        idxW = idx*4

        x = leftShift(w[idxW+3]) #simpen hasil circular shift

        s = sub(x) #simpen hasil substitution

        rcon = generateRCon() #round constant
        xres = g(s, rcon[idx]) #hasil xor rcon dengan w[3]


        w.append(g(w[idxW],xres))
        w.append(g(w[idxW+4],w[idxW+1]))
        w.append(g(w[idxW+5], w[idxW+2]))
        w.append(g(w[idxW+6], w[idxW+3]))
    
    temp = sum(w, []) #mengubah list 2d menjadi 1d, tujuannya agar bisa dibagi menjadi 11 roundkey

    rk = [temp[i:i+16] for i in range(0, len(temp), 16)] #misahin jadi isinya 16

    return rk