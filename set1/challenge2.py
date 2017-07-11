# https://cryptopals.com/sets/1/challenges/2

def xor(string1, string2):
    b1 = bytearray.fromhex(string1)
    b2 = bytearray.fromhex(string2)
    b = bytearray(len(b1))

    for i in range(len(b)):
        b[i] = b1[i] ^ b2[i]

    return bytes(b).encode('hex')

str1 = '1c0111001f010100061a024b53535009181c'
str2 = '686974207468652062756c6c277320657965'

print(xor(str1, str2))
