import codecs
import re

def is_french_word(w):
    dictionnary = codecs.open("../french/liste_fr.txt", "r", encoding="us-ascii")
    words = dictionnary.read().split()

    for word in words:
        if w == word:
            return True

    dictionnary.close()
    return False

def order_letter_by_apparition():
    dictionnary = codecs.open("../french/liste_fr.txt", "r", encoding="us-ascii")
    words = dictionnary.read().split()

    alphabet = {}
    for letter in "abcdefghijklmnopqrstuvwxyz":
        alphabet[letter]=0


    for word in words:
        for letter in word:
            if re.match("[a-z]", letter.lower()):
                alphabet[letter.lower()] += 1

    sorted_list = sorted(alphabet.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)

    return [e[0] for e in sorted_list]

