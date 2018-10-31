"""
A morse code translator. Morse code input must be
in proper format i.e. spaces between each character.
program could be expanded upon to include more complex characters
reference material: https://morsecode.scphillips.com/morse2.html
Author: Chris Roach
Date: 10/31/2018
"""

import character_hash

translated = []
done = False


def get_char(morse):
    return_char = character_hash.character_dict[morse]
    return return_char


while done == False:
    try:
        morse_code = input("Enter morse code string: ")
        split_char = morse_code.split(" ")
        for char in split_char:
            new_char = get_char(char)
            translated.append(new_char)
        done = True
    except:
        print("Error in morse code message, try again")
        translated = []
        done = False

done = True
message = ''.join(translated)

print(message.lower())
