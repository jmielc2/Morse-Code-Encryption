'''
Author: Jacob Mielczarek

Program Name: Morse Code Game

Program Function: This program, when called, will first ask if the user will like to play with Morse Code
or with English. It will then ask if the user wants to test letters or words. Once these two are decided,
it will run the program. The program will choose a word from a collection of words and present them. The
user will then input their translation. The program will then convert the word and print whether the
translation is true of false. If the answer is wrong, it will print the correct result. After ten repetitions
the program will print a score and return to the main menu.
'''
#Import statements
from eng_to_morse_dict import english_morse_dict as dictionary
from MorseCodeConverter import english_to_morse
import random, time


#Obtain Game Options
def game_options():
    '''This function runs through a series of dialog and inputs where the user specifies
    the settings of the game they want to play'''
    options = ['1', '2']
    option1 = True
    option2 = True
    #Chooses a language to convert to
    print("\n----------------------------------------------------------------------")
    print("\nCHOOSE A LANGUAGE:\n")
    print("  - Enter (1) to test your Morse Code to English conversion skills")
    print("  - Enter (2) to test your English to Morse Code conversion skills")
    language = input("Please Select An Option: ")
    while option1:
        if language not in options:
            print("Invalid Entry, Please Enter a Valid Option:")
        else:
            option1 = False
    #Chooses whether it will be testing letters or words
    print("\nCHOOSE A MODE:\n")
    print("  - Enter (1) to convert Letters")
    print("  - Enter (2) to convert Words")
    mode = input("Please Select An Option: ")
    while option2:
        if mode not in options:
            print("Invalid Entry, Please Enter a Valid Option:")
        else:
            option2 = False
    return (language, mode)


def choose_Phrase(language, mode):
    '''This function returns a phrase from either the dictionary or the Phrases.txt
    document depending on the settings which are specified as the parameters'''
    if language == '1': #If user is converting from Morse Code to English
        if mode == '1': #If user is converting just singular letters
            letters = dictionary.keys()
            rand_num = random.randint(0, len(letters) - 1)
            chosen_letter = list(letters)[rand_num]
            morse_letter = dictionary[chosen_letter]
            return (morse_letter, chosen_letter)
        else: #If user is converting phrases and words
            all_phrases = open("Phrases.txt", 'r')
            phrases_list = all_phrases.readlines()
            all_phrases.close()
            rand_num = random.randint(0, len(phrases_list) - 1)
            chosen_phrase = phrases_list[rand_num]
            new_phrase = chosen_phrase[:-1]  #Removes the \n character
            morse_phrase = english_to_morse(new_phrase.lower(), dictionary)
            return (morse_phrase, new_phrase)
    else: #If user is converting from English to Morse Code
        if mode == '1': #If user is converting just singular letters
            pass #TODO: Finish the code where you convert English to Morse Code for letters
        else: #If user is converting phrases and words
            pass #TODO: Finish the code where you convert English to Morse Code for phrases


def game_program():
    '''This function is the skeleton of the game and runs all the previous functions
    in certain sequence as the game'''    
    print('\nBeginning Game...')
    selections = game_options()
    tested_list = [' ']
    score = 0
    rep = 1
    time.sleep(3)
    while rep <= 10:
        phrases = choose_Phrase(selections[0], selections[1])
        while phrases[1] in tested_list:
            phrases = choose_Phrase(selections[0], selections[1])
        print('\n----------------------------------------------------------------------')
        print("\n #{} - TRANSLATE:".format(rep), phrases[0])
        user_answer = input("YOUR TRANSLATION: ")
        if user_answer.lower().strip() != phrases[1].lower():
            print("\nIncorrect, the correct translation was '{}'".format(phrases[1]))
            time.sleep(2)
        else:
            print('\nCorrect!')
            score += 1
            tested_list.append(phrases[1])
            time.sleep(2)
        rep += 1
    print('\n----------------------------------------------------------------------')
    print("\nLet's see how you did...")
    time.sleep(2)
    final_score = score / 10
    print('\nFinal Score: {}%'.format(int(final_score * 100)))
    time.sleep(1)
    if final_score <= 0.5:
        print("\nKeep at it! you'll get it someday!")
    elif final_score <= 0.9:
        print("\nNice Job! You almost got a prefect score!")
    else:
        print("\nPerfect Score! Great Job!")
    time.sleep(1)
    print('\n\nReturning to MAIN MENU...')
    print ('\n----------------------------------------------------------------------')
