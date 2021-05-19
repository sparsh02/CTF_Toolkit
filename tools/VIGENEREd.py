import sys

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def vigenere_decrypt(cipher_text, key):

	cipher_text = cipher_text.upper()
	key = key.upper()

	plain_text = ''
	key_index = 0

	for character in cipher_text:
		if character == ' ':
			plain_text += ' '
		else :
			index = (ALPHABET.find(character)-(ALPHABET.find(key[key_index])))%len(ALPHABET)
			plain_text += ALPHABET[index]
			key_index = key_index + 1

		if key_index == len(key):
			key_index = 0

	return plain_text

enc_msg = sys.argv[1]
key = sys.argv[2]
decrypted = vigenere_decrypt(enc_msg,key)
print(decrypted)