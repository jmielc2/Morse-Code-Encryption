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

def game_program():
    import random
    from eng_to_morse_dict import english_morse_dict as dictionary
    from MorseCodeConverter import convert_program
    options = ['1', '2']

    #Obtain Game Options
    def game_options():
        option1 = True
        option2 = True
        #Chooses a language to convert to
        print("\n----------------------------------------------------------------------")
        print("\nCHOOSE A LANGUAGE:\n")
        print("  - Enter (1) for Morse Code to English")
        print("  - Enter (2) for English to Morse Code")
        language = input("\nPlease Select An Option: ")
        while option1:
            if language not in options:
                print("Invalid Entry, Please Enter a Valid Option:")
            else:
                option1 = False
        #Chooses whether it will be testing letters or words
        print("\nCHOOSE A MODE:\n")
        print("  - Enter (1) for Letters")
        print("  - Enter (2) for Words")
        mode = input("\nSelect One: ")
        while option2:
            if mode not in options:
                print("Invalid Entry, Please Enter a Valid Option:")
            else:
                option2 = False
        return (language, mode)

    #Choose A Phrase
    def choose_Phrase(language, mode):
        if language == '1':
            if mode == '1':
                #FIXME: Create a list of Morse Code letters to be used for 
                #the game
                pass
            else:
                all_phrases = open("Phrases.txt", 'r')
                phrases_list = all_phrases.readlines()
                all_phrases.close()
        rand_num = random.randint(0, len(phrases_list))
        chosen_phrase = phrases_list[rand_num]
        return chosen_phrase
    
    print("\n----------------------------------------------------------------------")
    print("\nGAME PROGRAM RUNS THEN QUITS HERE")
    print("\nReturning to MAIN MENU...")
    print("\n----------------------------------------------------------------------")

#game_program
