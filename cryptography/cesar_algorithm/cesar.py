
def cesar_encr(message, key) :
	encr_message = ""
	for letter in message:
		if letter != " " :
			encr_message += chr(((ord(letter)-97+key)%26)+97)
		else :
			encr_message += " "
	return encr_message

def cesar_decr(encr_message, key) :
	decr_message = ""
	for letter in encr_message :
		if letter != " " :
			decr_message += chr(((ord(letter)-97-key)%26)+97)
		else :
			decr_message += " "
	return decr_message

#key = 3
#encr = cesar_encr("bonjour bounou", key)
#print(encr)
#decr = cesar_decr(encr, key)
#print(decr)

