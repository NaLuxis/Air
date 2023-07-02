############### Rotation vers la gauche ###############

import sys

from typing import List

### Function ###

def rotate_left(list_to_rotate: List[str]) -> List[str]:

    new_list = []

    for element in list_to_rotate[1:]:
        new_list.append(element)

    new_list.append(list_to_rotate[0])

    return new_list


def print_correct(rotate_list: List[int]) -> str:

    for element in rotate_list:

        if element != rotate_list[-1]:
            print(f"{element}, ", end="")
        else:
            print(f"{element} ", end="")
    
    print("")
    exit()


def incorrect_argument_count() -> None:

    if len(sys.argv) <= 2:
        print("Error")
        exit()

### Error ###

incorrect_argument_count()

### Parsing ###

complete_list = sys.argv[1:]

### Problem solving ###

rotated_left = rotate_left(complete_list)

correct_sentence = print_correct(rotated_left)

### Result ###

print(correct_sentence)