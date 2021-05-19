import sys
lookup = {'A':'aaaaa', 'B':'aaaab', 'C':'aaaba', 'D':'aaabb', 'E':'aabaa',
        'F':'aabab', 'G':'aabba', 'H':'aabbb', 'I':'abaaa', 'J':'abaab',
        'K':'ababa', 'L':'ababb', 'M':'abbaa', 'N':'abbab', 'O':'abbba',
        'P':'abbbb', 'Q':'baaaa', 'R':'baaab', 'S':'baaba', 'T':'baabb',
        'U':'babaa', 'V':'babab', 'W':'babba', 'X':'babbb', 'Y':'bbaaa', 'Z':'bbaab'}
  

def encrypt(message):
    cipher = ''
    for letter in message:
        if(letter != ' '):
            cipher += lookup[letter]
        else:
            cipher += ' '
  
    return cipher

def main():
    message = sys.argv[1]
    result = encrypt(message.upper())
    print (result)

if __name__ == '__main__':
    main()