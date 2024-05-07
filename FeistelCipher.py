# @Josh Mundray

import re

# XOR Function
def xor(a,b):     
    return ''.join("0" if a[i] == b[i] else '1' for i in range(8))

# Circular Shift
def shift(x, n):
    x=int(x, 2)
    return bin((x << n)|(x >> (8 - n))).split("0b")[1][-8:].zfill(8)

DATA = input("Data: ")
KEY = input("Key: ")

if re.sub("[^01]", "", DATA) == DATA:
    DATA = DATA.zfill(16)
else:
    DATA = bin(int(DATA))[2:].zfill(16)

if re.sub("[^01]", "", KEY) == KEY:
    KEY = KEY.zfill(8)
else:
    KEY = bin(int(KEY))[2:].zfill(8)

if len(DATA) > 16: raise ValueError("Length greater than 16")
if len(KEY) > 8: raise ValueError("Length greater than 8")

L1 = DATA[0:8]
R1 = DATA[8::]

# Generate keys
KEY=''.join('1' if i == '0' else '0' for i in KEY)
K1=shift(KEY, 0)
K2=shift(KEY, 1)
K3=shift(KEY, 2)
K4=shift(KEY, 3)

print(K1, K2, K3, K4)

# First round of encryption
f1 = xor(R1,K1)
R2 = xor(f1,L1)
L2 = R1
  
# Second round of encryption
f2 = xor(R2,K2)
R3 = xor(f2,L2)
L3 = R2
  
# Third round of encryption
f3 = xor(R3,K3)
R4 = xor(f3,L3)
L4 = R3

# Fourth round of encryption
f4 = xor(R4,K4)
R5 = xor(f4,L4)
L5 = R4

# Output
ENC = bin(int(L5+R5, 2))[2:].zfill(16)
print(f"Binary: {ENC[2:]} | Denary: {int(ENC, 2)} ({int(ENC, 2) - 2**16 if ENC[0] == "1" else int(ENC, 2)})")
