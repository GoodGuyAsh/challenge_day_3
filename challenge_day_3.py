#!/usr/bin/env python3

LETTERS_UPPERCASE = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
LETTERS_LOWERCASE = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


ciphered_letters = []
ciphered_words = []

deciphered_letters = []
deciphered_words = []


def cipher(text, shift):                                                                          ## This function cipher's 1 single alphabet with the given shift value
	
	try:
	
		if text.isupper():
	
			for i in range(0, 26):
	
				if LETTERS_UPPERCASE[i] == text:
					encrypt = (i + shift) % 26
					encrypt_letter = LETTERS_UPPERCASE[encrypt]
					return encrypt_letter
		
		elif text.islower():
	
			for i in range(0, 26):
	
				if LETTERS_LOWERCASE[i] == text:
					encrypt = (i + shift) % 26
					encrypt_letter = LETTERS_LOWERCASE[encrypt]
					return encrypt_letter

	except TypeError:

		return "ERROR: Please enter an Alphabet only!"
   
def decipher(text, shift):                                                                          ## This function decipher's 1 single alphabet with the given shift value
	
	try:
	
		if text.isupper():
	
			for i in range(0, 26):
	
				if LETTERS_UPPERCASE[i] == text:
					encrypt = (i - shift) % 26
					encrypt_letter = LETTERS_UPPERCASE[encrypt]
					return encrypt_letter
		
		elif text.islower():
	
			for i in range(0, 26):
	
				if LETTERS_LOWERCASE[i] == text:
					encrypt = (i - shift) % 26
					encrypt_letter = LETTERS_LOWERCASE[encrypt]
					return encrypt_letter

	except TypeError:

		return "ERROR: Please enter an Alphabet only!"
   

def ceasar_cipher(line, shift):                                                       ## This function cipher's string with any number of words in it with the given shift value
	line = line.split(" ")
	# DEBUG: 
	# print(line)

	for word in line:

		for letter in word:

			ciphered_letter = cipher(letter, shift)
			ciphered_letters.append(ciphered_letter)

		ciphered_word = "".join(ciphered_letters)
		ciphered_letters.clear()

		ciphered_words.append(ciphered_word)

	

	return " ".join(ciphered_words)


def ceasar_decipher(line, shift):                                                                ## This function decipher's string with any number of words in it with the given shift value
	line = line.split(" ")
	# DEBUG: 
	# print(line)
	
	for word in line:
	
		for letter in word:
	
			deciphered_letter = decipher(letter, shift)
			deciphered_letters.append(deciphered_letter)

		deciphered_word = "".join(deciphered_letters)
		deciphered_letters.clear()
	
		deciphered_words.append(deciphered_word)

	

	return " ".join(deciphered_words)


if __name__ == '__main__':

	print(ceasar_decipher("Txmh jwm Snaah qjen vjbbren kajrwb", 9))
