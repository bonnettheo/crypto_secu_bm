
def exclusiv_or(a,b):
    toReturn = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            toReturn += '0'
        else :
            toReturn += '1'
    return toReturn

def s_box(a):
    if a == "0000":
        return "0001"
    elif a == "0001":
        return "1001"
    elif a == "0010":
        return "1101"
    elif a == "0011":
        return "1011"
    elif a == "0100":
        return "0100"
    elif a == "0101":
        return "1111"
    elif a == "0110":
        return "0010"
    elif a == "0111":
        return "0000"
    elif a == "1000":
        return "0101"
    elif a == "1001":
        return "1110"
    elif a == "1010":
        return "0110"
    elif a == "1011":
        return "1000"
    elif a == "1100":
        return "0111"
    elif a == "1101":
        return "1010"
    elif a == "1110":
        return "0011"
    elif a == "1111":
        return "1100"

def s_box_back(a):
    if a == "0000":
        return "0111"
    elif a == "0001":
        return "0000"
    elif a == "0010":
        return "0110"
    elif a == "0011":
        return "1110"
    elif a == "0100":
        return "0100"
    elif a == "0101":
        return "1000"
    elif a == "0110":
        return "1010"
    elif a == "0111":
        return "1100"
    elif a == "1000":
        return "1011"
    elif a == "1001":
        return "0001"
    elif a == "1010":
        return "1101"
    elif a == "1011":
        return "0011"
    elif a == "1100":
        return "1111"
    elif a == "1101":
        return "0010"
    elif a == "1110":
        return "1001"
    elif a == "1111":
        return "0101"

def spn_encr(message, key):
    
    for i in range(5):
        message = exclusiv_or(message, key[i*16:(i+1)*16])
        temp_mess = ""
        for j in range(4):
            temp_mess += s_box(message[j*4:(j+1)*4])
        
        message = ""
        for j in range(4):
            message += temp_mess[j]
            message += temp_mess[j+4]
            message += temp_mess[j+8]
            message += temp_mess[j+12]
    return message

def spn_decr(message, key):
    for i in range(4,-1,-1):
        temp_mess = message
        message = ""
        for j in range(4):
            message += temp_mess[j]
            message += temp_mess[j+4]
            message += temp_mess[j+8]
            message += temp_mess[j+12]     

        temp_mess = ""
        for j in range(4):
            temp_mess += s_box_back(message[j*4:(j+1)*4])
        
        message = temp_mess

        message = exclusiv_or(message, key[i*16:(i+1)*16])

    return message


k1 = "1001100110011001"
k2 = "0011110001010001"
k3 = "1001110001111010"
k4 = "0011111010100010"
k5 = "0110101010001011"

message = "0101001111001010"

encr = spn_encr(message, k1 + k2 + k3 + k4 + k5)

print(encr)

decr = spn_decr(encr, k1 + k2 + k3 + k4 + k5)
print(message)
print(decr)
