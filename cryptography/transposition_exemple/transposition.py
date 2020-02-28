

def transpo_encr(message,rule):
    rule_size = len(rule)
    while len(message)%rule_size != 0:
        message += "z"

    
    encr = ""
    for i in range(int(len(message)/rule_size)):
        temp_rule = rule
        for ind in range(rule_size):
            new_rule = ""
            for j in range(rule_size):
                if temp_rule[j] == '1':
                    encr += message[i*rule_size+j]
                new_rule += chr(ord(temp_rule[j])-1)
            temp_rule = new_rule
    return encr

def transpo_decr(encr, rule):
    decr = ""
    for i in range(int(len(encr)/len(rule))):
        for r in rule:
            decr += encr[i*len(rule)+int(r)-1]
    return decr



#print("règle :")
#rule = input()
#print("message :")
#message = input()
#encr = transpo_encr(message, rule)
#print(encr)
#print(transpo_decr(encr, rule))
