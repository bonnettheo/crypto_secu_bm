import re

def phi(nbr):
    prime_numbers=[]
    for i in range(2,nbr):
        if nbr%i==0 :
            real_prime = True
            for prime in prime_numbers:
                if i%prime == 0:
                    real_prime = False
            if real_prime:
                prime_numbers.append(i)
    phi = 1
    for prime in prime_numbers:
        exceed = True
        while exceed:
            nbr = nbr/prime
            phi *= prime-1
            exceed=False
            if nbr%prime == 0:
                exceed = True
    return phi

def pgcd(v1, v2):
    if v1==v2:
        return v1
    elif v1>v2:
        return pgcd(v1-v2, v2)
    elif v1<v2:
        return pgcd(v2-v1, v1)

def mult_encr(message, key):
    if pgcd(key,26)!=1:
        print("la clef doit etre première avec 26")
        exit(1)
    
    encr = ""
    for letter in message:
        if re.match("[a-z]", letter):
            encr += chr(((ord(letter)-97)*key)%26+97)
    return encr


def mult_decr(encr, key):
    if pgcd(key,26)!=1:
        print("la clef doit etre première avec 26")
        exit(1)
    
    decr = ""
    for letter in encr:
        letter_number = ord(letter)-97
        while letter_number%key != 0:
            letter_number+=26
        decr += chr(int(letter_number/key)+97)
    return decr

print("choisir un nombre")
nbr = int(input())
print("pgcd(nbr,26) = ", pgcd(nbr,26))
print("choisir un message")
message = input()
encr = mult_encr(message, nbr)
print(encr)
print(mult_decr(encr, nbr));
