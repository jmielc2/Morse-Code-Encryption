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
    #Obtain Game Options
    def game_options():
        print("CHOOSE A LANGUAGE:\n")
        print("  - Enter (1) for Morse Code to English")
        print("  - Enter (2) for English to Morse Code")
        language = input("\nSelect One: ")
        print("\nCHOOSE A MODE:\n")
        print("  - Enter (1) for Letters")
        print("  - Enter (2) for Words")
        mode = input("\nSelect One: ")

    def choose_phrase():
        all_phrases = open("Phrases.txt", 'r')
        phrases_list = all_phrases.readlines()
        all_phrases.close()

        rand_num = random.randint(0, len(phrases_list))
        chosen_phrase = phrases_list[rand_num]
        return chosen_phrase

    def game(phrases):
        pass
