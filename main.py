import random

# Morse to english dictionary
CODE = {'A': '.-', 'B': '-...', 'C': '-.-.',
        'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',

        '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..',
        '9': '----.', ' ': ' ', '.': '.-.-.-', ',': '--..--'
        }


# Detects if input user input is english or morse
def is_english(w):
    english_to_morse = True
    word = w.upper()
    for key, value in CODE.items():
        if key in word and key != ' ' and key != '.' and key != ',':
            english_to_morse = True
            break
        else:
            english_to_morse = False
    return english_to_morse


# Function to find the key from a dict by its value
def get_key_from_in_dict(value):
    for key, v in CODE.items():
        if value == v:
            return key
    return False


# Function to change input from morse to english
def morse_to_english(word):
    """:arg word: input morse code to convert to english"""
    word_arr = word.split(CODE[' '])
    translated_word = ''
    translated_word_arr = []
    for word in word_arr:
        letter_arr = word.split('/')
        for letter in letter_arr:

            if get_key_from_in_dict(letter):
                translated_word += get_key_from_in_dict(letter)
            else:
                translated_word += letter
        translated_word_arr.append(translated_word)
        translated_word = ''
    translated_sentence = ' '.join(translated_word_arr).capitalize()
    return translated_sentence

# Function to convert to morse code
def english_to_morse(word):
    """word: input word to convert to morse code"""
    translated_sentence = ''
    word = word.upper()
    for i in range(len(word)):

        try:
            translated_sentence += CODE[word[i]]

            try:
                if CODE[word[i]] != ' ' and CODE[word[i + 1]] != ' ':
                    translated_sentence += '/'
            except IndexError:
                pass
            except KeyError:
                pass
        except KeyError:
            translated_sentence += word[i]
    return translated_sentence


translate_is_active = True


while translate_is_active:
    user_input = input(
        'Please input the word/code to translate, use space to seperate words and / to seperate letters. q to quit: ').upper()
    if user_input == 'Q':
        translate_is_active = False
    elif is_english(user_input):
        # Translate from english to morse
        print(english_to_morse(user_input))

    else:
        # Translate from morse to english
        print(morse_to_english(user_input))
