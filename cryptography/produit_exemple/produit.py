import sys
import os
import random

sys.path.append(os.path.abspath("../transposition_exemple"))
import transposition as t

sys.path.append(os.path.abspath("../cesar_algorithm"))
import cesar as c

numbers = [1, 2, 3, 4, 5]

def prod_encr(message, nbrTurn):
    cesar_keys = []
    rules = []
    encr = message

    for i in range(nbrTurn):
        cesar_key = random.randint(1,25)
        random.shuffle(numbers)
        cesar_keys.append(cesar_key)
        rules.append(numbers.copy())

        str_rule = ""
        for rule in numbers:
            str_rule += str(rule)
        
        encr = c.cesar_encr(encr, cesar_key)
        encr = t.transpo_encr(encr, str_rule)

    return encr, cesar_keys, rules

def produit_decr(encr, cesar_list, transpo_list):
    decr = encr
    for i in range(len(cesar_list)-1, -1, -1):
 
        str_rule = ""
        for rule in transpo_list[i]:
            str_rule += str(rule)

        decr = t.transpo_decr(decr, str_rule)
        decr = c.cesar_decr(decr, cesar_list[i])
    return decr

encr, cesar, transp = prod_encr("joliclazr", 3)

print(cesar)
print(transp)
print(encr)

print(produit_decr(encr, cesar, transp))
