############### Split ###############

import sys

from typing import List

### Function ###

def cutting_string(string_to_cut: str, separator: str) -> List[str]:

    string_list = []
    word = ""

    for char in string_to_cut:

        if char in separator:
            
            if word:
                string_list.append(word)
                word = ""
        else:
            word += char

    if word:
        string_list.append(word)
    
    return string_list


def print_correct(list_cutted: List[str]) -> str:

    for word in list_cutted:
        print(word)


def incorrect_argument_count() -> None:

    if len(sys.argv) != 2:
        print("Error")
        exit()


def is_number(target: any) -> bool:

    if str(target).lstrip("-+").isdigit():
        return True
    else:
        return False
    

def is_string(target: any) -> bool:

    if type(target) == str:
        return True
    else:
        return False


def error_argument() -> None:

    if is_string(sys.argv[1]):
        pass
    else:
        print("Error")
        exit()

    if is_number(sys.argv[1]):
        print("Error")
        exit()


### Error ###

incorrect_argument_count()

error_argument()

### Parsing ###

string_to_cut = sys.argv[1]

### Problem solving ###

cutted_string = cutting_string(string_to_cut, " \t\n")

correct_sentence = print_correct(cutted_string)

### Result ###

print(correct_sentence)