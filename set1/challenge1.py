# https://cryptopals.com/sets/1/challenges/1

hex_string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
decoded = hex_string.decode('hex')
base_64_string = decoded.encode('base64')
print(base_64_string)
