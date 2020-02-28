import re

def vigenere_encr(message, key):
    while len(key)<len(message):
        key += key

    encr = ""
    for i in range(len(message)):
        if re.match("[a-z]",message[i]):
            encr += chr((ord(message[i]) + ord(key[i]) - 2*97)%26+97)
    return encr


def vigenere_decr(message, key):
    while len(key)<len(message):
        key += key

    encr = ""
    for i in range(len(message)):
        if re.match("[a-z]",message[i]):
            encr += chr((ord(message[i]) - ord(key[i]))%26+97)
    return encr


print("clef :")
key = input()
print("message :")
message = input()
encr = vigenere_encr(message, key)
print(encr)
print(vigenere_decr(encr, key))
