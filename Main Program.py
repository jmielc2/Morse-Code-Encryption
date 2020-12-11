'''
Author: Jacob Mielczarek

Purpose: The purpose of this program is to assist in the learning and converting
of morse code.

Function:
This program will first ask whether the user wants to learn, practice, or
convert.
If they want to learn, a game will begin that will help teach the user how to
use morse code.

If they want to practice, the program will ask if they would like to learn how
to read or write. If they want to learn how to read, they will be given a
statement in morse code which they will need to translate. If they want to
write, they will be given a statement which they will need to translate into
morse code.

If they want to convert, they will input a statement in either morse code or
written language which will then be converted into the opposite language.
'''

#Functions
request = 0
def request_func():
    print("\nMAIN MENU:")
    print("  - Enter (1) to Learn Morse Code Game")
    print("  - Enter (2) to Translate")
    print("  - Enter (3) to Quit")
    request = input("What Would You Like To Do?: ")
    return request

#What do you want to do?
request = request_func()

while request != '3':
    #Game/Learn
    if request == '1':
        from MorseCodeGame import game_program
        game_program()
        request = request_func()

    #Convert
    if request == '2':
        from MorseCodeConverter import convert_program
        convert_program()
        request = request_func()

print("\nGoodbye")
