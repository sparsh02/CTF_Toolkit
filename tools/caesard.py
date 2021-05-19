import sys

ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
KEY = int(sys.argv[2])


def caesar_decrypt(cipher_text):

	plain_text = ''
	
	for c in cipher_text:
		index = ALPHABET.find(c)
		index = (index-KEY)%len(ALPHABET)
		plain_text = plain_text + ALPHABET[index]
		
	return plain_text
	
if __name__ == "__main__":
	
	plaintext = sys.argv[1]
	decrypted = caesar_decrypt(plaintext)
	print(decrypted)
	