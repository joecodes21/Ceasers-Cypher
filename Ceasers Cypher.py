###########################################//CEASERS CIPHER//###########################################################
import nltk
from nltk.corpus import words

def decrypt_caesar_cipher(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            is_upper = char.isupper()
            char_code = ord(char)
            shifted_code = (char_code - shift - ord('A' if is_upper else 'a')) % 26 + ord('A' if is_upper else 'a')
            decrypted_text += chr(shifted_code)
        else:
            decrypted_text += char


    #checking for words in the dataset
        # Get the set of English words
        english_words = set(words.words())
        # Tokenize the input text into words
        word_tokens = nltk.word_tokenize(decrypted_text)
        # Identify real words from the given text
        real_words = [word for word in word_tokens if word.lower() in english_words]

        print(real_words)



    return decrypted_text

def break_caesar_cipher(ciphertext):
    for shift in range(26):
        decrypted_text = decrypt_caesar_cipher(ciphertext, shift)

        print(f"Shift {shift}: {decrypted_text}")


# Example usage
encrypted_message = "haahjr ha vujl"
break_caesar_cipher(encrypted_message)



