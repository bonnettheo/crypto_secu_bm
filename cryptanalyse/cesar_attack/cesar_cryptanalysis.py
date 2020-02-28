import sys
import os
import re

sys.path.append(os.path.abspath("../french"))
import check_french as fr

sys.path.append(os.path.abspath("../../cryptography/cesar_algorithm"))
import cesar as c

def idiot_cesar_cryptanalysis(cypher):
    for i in range(26):
        tried_brute_force = c.cesar_decr(cypher, i)
        print(i, " : ", tried_brute_force)

def cesar_cryptanalysis(cypher):
    for i in range(26):
        tried_brute_force = c.cesar_decr(cypher, i)
        for word in tried_brute_force.split():
            if fr.is_french_word(word):
                print(i, " : ", tried_brute_force)
                break

def smart_cesar_cryptanalysis(cypher):
    letter_sorted = fr.order_letter_by_apparition()
    nbrIt = 0

    alphabet = {}
    for letter in "abcdefghijklmnopqrstuvwxyz":
        alphabet[letter]=0

    for letter in cypher:
        if re.match("[a-z]", letter.lower()):
            alphabet[letter.lower()] += 1

    most_used = "a"
    max_apparition = 0
    for letter in alphabet:
        if alphabet[letter] > max_apparition:
            max_apparition = alphabet[letter]
            most_used = letter

    print("most used letter :", most_used, "\nin cypher : ",cypher)
    for letter in letter_sorted:
        nbrIt += 1
        key = ord(most_used)-ord(letter)
        tried_brute_force = c.cesar_decr(cypher, key)
        for word in tried_brute_force.split():
            if fr.is_french_word(word):
                print("achieved in ", nbrIt, "iteration, common letter", letter)
                print(key, " : ", tried_brute_force)
                break


smart_cesar_cryptanalysis(c.cesar_encr("attaque du bounou", 4))
