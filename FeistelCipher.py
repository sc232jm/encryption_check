# @Josh Mundray

# XOR Function
def xor(a,b):     
    return ''.join("0" if a[i] == b[i] else '1' for i in range(8))

# Circular Shift
def shift(x, n):
    x=int(x, 2)
    return bin((x << n)|(x >> (8 - n)))[-8:].zfill(8)
 
DATA = input("Data: ").zfill(16)
KEY = input("Key: ").zfill(8)

L1 = DATA[0:8]
R1 = DATA[8::]

# Generate keys
KEY=''.join('1' if i == '0' else '0' for i in KEY)
K1=shift(KEY, 0)
K2=shift(KEY, 1)
K3=shift(KEY, 2)
K4=shift(KEY, 3)

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
ENC = bin(int(L5+R5, 2))
print(f"Binary: {ENC[2:].zfill(8)} | Denary: {int(ENC, 2)} ({int(ENC, 2) - 2**16 if ENC[2] == "1" else ENC}) ")