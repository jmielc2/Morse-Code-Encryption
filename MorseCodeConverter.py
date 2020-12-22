'''
Author: Jacob Mielczarek

Program Name: Morse Code Converter

Program Function: When called, this function will show three options: (1)
Convert from English to Morse Code, (2) Convert Morse Code into English,
and (3) return to the main menu (the Main Program).
'''
#Import statements
import time, re
from eng_to_morse_dict import english_morse_dict as eng_morse

#Removes extra spaces and other characters
def remove_spaces1(phrase):
    '''This function removes unwanted phrases and characters from the given
    text'''
    regexSpaces = re.compile(r'\W+|_')
    matches = regexSpaces.findall(phrase)
    for match in matches:
        if match != "'":
            phrase = phrase.replace(match, ' ')
        else:
            phrase = phrase.replace(match, '')
    return phrase

def remove_spaces2(code):
    '''This function will remove extra spaces and unknown characters from a
    given morse code string'''
    rep = 1
    while rep <= 2:
        regexCode = re.compile(r'\s{2,}|[^-./ ]')
        matches = regexCode.findall(code)
        for match in matches:
            code = code.replace(match, ' ')
        rep += 1
    return code

#Converts English to Morse Code
def english_to_morse(phrase, eng_morse):
    '''This function converts english into morse code'''     
    result_list = []
    phrase = remove_spaces1(phrase) #removes unwanted characters and extra spaces
    for letter in phrase.strip():
        bit = eng_morse.get(letter, None)
        if bit == None:
            return (letter, None)
        result_list.append(bit)
    result = ' '.join(result_list)
    return result


#Converts Morse Code to English
def morse_to_english(code, eng_morse):
    '''This function converts morse code into english'''
    result_list = []
    code = remove_spaces2(code) #Removes extra spaces and unwanted characters
    code_list = code.split('/')
    code_list_copy = code_list[:]
    morse_code_letters = eng_morse.values()
    #Breaks words down into their morse code letters and returns a list of morse letters original list
    for pos, word in enumerate(code_list_copy):
        word = word.strip().split(' ')
        code_list[pos] = word
    #Goes through each 'word' in code_list then converts each morse letter into a real letter and adds it to the result list
    for pos, morse_word in enumerate(code_list):
        result_list.append([])
        for morse_letter in morse_word:
            if morse_letter not in morse_code_letters:
                return (morse_letter, None)
            for key in eng_morse:
                if eng_morse[key] == morse_letter:
                    result_list[pos].append(key)
    result_list_copy = result_list[:]
    #Combines the letters for each word into one word then combines all the words into a sentence and returns the sentence
    for pos, word in enumerate(result_list_copy):
        result_list[pos] = ''.join(word)
    result = ' '.join(result_list)
    return result


#This is the main convert_program
def convert_program():
    #Variables
    options = ['1', '2', '3']

    #Introduction
    print("\n----------------------------------------------------------------------")
    print("\nOPTIONS MENU")
    print("  - (1) Translate English to Morse Code")
    print("  - (2) Translate Morse Code to English")

    #Conversion Option
    option = input("Please Select an Option: ")

    #Conversion Loop
    if option not in options:
        option = input("Invalid Entry, Please Enter a Valid Option: ")

    if option == '1':
        print("\nEnter English Text:")
        phrase = input().lower().strip()
        result = english_to_morse(phrase, eng_morse)
        while isinstance(result, str) != True:
            time.sleep(1)
            print("\n'{}' is a character in your string that cannont be converted to Morse Code.".format(result[0]))
            print("Please Re-enter your phrase:")
            phrase = input().lower().strip()
            result = english_to_morse(phrase, eng_morse)
        print('\n----------------------------------------------------------------------')
        print("\nTRANSLATION FORMATTING:")
        print("  - '.' = DOT")
        print("  - '-' = DASH")
        print("  - ' ' = Separates Letters")
        print("  - '/' = Separates Words")
        time.sleep(2)
        print("\nTRANSLATION:", result)
        time.sleep(3)
        result = ''

    if option == '2':
        print("\nINPUT FORMAT:")
        print("  - '.' = DOT")
        print("  - '-' = DASH")
        print("  - ' ' = Separates Letters")
        print("  - '/' = Separate Words")
        print("Enter Morse Code:")
        code = input().strip()
        result = morse_to_english(code, eng_morse)
        while isinstance(result, str) != True:
            print("\n'{}' is not a Morse Code character.".format(result[0]))
            print("Please Re-enter your phrase:")
            code = input().lower().strip()
            result = morse_to_english(code, eng_morse)
        print("\nTRANSLATION:", result.capitalize())
        time.sleep(3)
        result = ''

    print("\n\nReturning to MAIN MENU...")
    print("\n----------------------------------------------------------------------")
