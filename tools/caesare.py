import sys

ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
KEY = int(sys.argv[2])


def caesar_encrypt(plain_text):

	cipher_text = ''
	plain_text = plain_text.upper()

	for c in plain_text:
		index = ALPHABET.find(c)
		index = (index+KEY)%len(ALPHABET)
		cipher_text = cipher_text + ALPHABET[index]
		
	return cipher_text

	
if __name__ == "__main__":
	
	plaintext = sys.argv[1]
	encrypted = caesar_encrypt(plaintext)
	print(encrypted)
