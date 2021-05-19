import sys
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def vigenere_encrypt(plain_text, key):

	plain_text = plain_text.upper()
	key = key.upper()

	cipher_text = ''
	key_index = 0
	
	for character in plain_text:
		if character == ' ':
			cipher_text = cipher_text + ' '
		else:
			index = (ALPHABET.find(character)+(ALPHABET.find(key[key_index])))%len(ALPHABET)
			cipher_text += ALPHABET[index]
			key_index = key_index + 1
		if key_index == len(key):
			key_index = 0

	return cipher_text

plain_text = sys.argv[1]
key = sys.argv[2]
encrypted = vigenere_encrypt(plain_text,key)
print(encrypted)