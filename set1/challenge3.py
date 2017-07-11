# https://cryptopals.com/sets/1/challenges/3

import string

def xor(string1, key):
    b1 = bytearray.fromhex(string1)
    key = ord(key)
    b = bytearray(len(b1))

    for i in range(len(b)):
        b[i] = b1[i] ^ key

    return bytes(b).encode('utf8')

hex_encoded = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

for c in range(len(string.ascii_letters)):
    print(xor(hex_encoded, string.ascii_letters[c]))
