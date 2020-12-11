'''
Author: Jacob Mielczarek

Program Name: Morse Code Converter

Program Function: When called, this function will show three options: (1)
Convert from English to Morse Code, (2) Convert Morse Code into English,
and (3) return to the main menu (the Main Program).
'''

def convert_program():
    #Imports
    import copy
    from eng_to_morse_dict import english_morse_dict as eng_morse 
    
    #Variables
    rep = 0
    options = ['1', '2', '3']
    
    #Introduction
    print("\n----------------------------------------------------------------------")
    print("\nOPTIONS MENU")
    print("  - (1) Translate English to Morse Code")
    print("  - (2) Translate Morse Code to English")
    print("  - (3) Return to MAIN MENU")
    
    #Conversion Option
    option = input("Please Select an Option: ")
    
    #Conversion Functions
    def english_to_morse(phrase):
        '''This function converts english into morse code'''
        result_list = []
        for letter in phrase:
            bit = eng_morse.get(letter, None)
            if bit == None:
                return (letter, None)
            result_list.append(bit)
        result = ' '.join(result_list)
        return result
  
    def morse_to_english(code):
        '''This function converts morse code into english'''
        result_list = []
        code_list = code.split('/')
        code_list_copy = copy.deepcopy(code_list)
        for pos, word in enumerate(code_list_copy):
            word = word.strip().split(' ')
            code_list[pos] = word
        
        morse_code_letters = eng_morse.values()
        
        for pos, morse_word in enumerate(code_list):
            result_list.append([])
            for morse_letter in morse_word:
                if morse_letter not in morse_code_letters:
                    return (morse_letter, None)
                for key in eng_morse:
                    if eng_morse[key] == morse_letter:
                        result_list[pos].append(key)
        result_list_copy = copy.deepcopy(result_list)
        
        for pos, word in enumerate(result_list_copy):
            result_list[pos] = ''.join(word)
        result = ' '.join(result_list)
        return result
        
    
    #Conversion Loop
    while option != '3':
        if option not in options:
            option = input("Invalid Entry, Please Enter a Valid Option: ")
            
        if option == '1':
            print("\nEnter English Text (no symbols: . ; , - etc.):")
            phrase = input().lower().strip()
            result = english_to_morse(phrase)
            
            if isinstance(result, str) != True:
                print("\n'{}' is a character in your string that cannont be converted to Morse Code.".format(result[0]))
            else:
                if rep < 1:
                    print("\nRESULT FORMATTING:")
                    print("  - '.' = DOT")
                    print("  - '-' = DASH")
                    print("  - ' ' = Separates Letters")
                    print("  - '/' = Separate Words")
                    rep = 1
            
                print("\nTRANSLATION:", result)
            result = ''
            option = input("Please select what you'd like to do next from the OPTIONS MENU: ")
            
        if option == '2':
            print("\nINPUT FORMAT:")
            print("  - '.' = DOT")
            print("  - '-' = DASH")
            print("  - ' ' = Separates Letters")
            print("  - '/' and '\\' = Separate Words")
            
            print("Enter Morse Code:")
            code = input()
            result = morse_to_english(code)
            
            if isinstance(result, str) != True:
                print("\n'{}' is not a Morse Code character.".format(result[0]))
            else:
                print("\nTRANSLATION:", result.capitalize())
            result = ''
            option = input("Please Select What You'd like to do Next from the OPTIONS MENU: ")
                                    
    print("\nReturning to MAIN MENU...")
    print("\n----------------------------------------------------------------------")