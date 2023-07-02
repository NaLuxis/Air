############### Mélanger deux tableaux triés ###############

import sys

from typing import List

### Function ###

def fusion_split(list_to_split: List[str]) -> List[List[int]]:

    first_list = []
    second_list = []

    fusion = False

    for element in list_to_split:
        
        if element.lstrip("+-").isdigit() and not fusion:
            first_list.append(int(element))
        
        if element.lstrip("+-").isdigit() and fusion:
            second_list.append(int(element))

        if not element.isdigit():
            fusion = True
    
    return [first_list, second_list]

    
def fusion_sort(base_list: List[int], fusion_list: List[int]) -> List[int]:

    new_list = []
    base_index, fusion_index = 0, 0

    while base_index < len(base_list) and fusion_index < len(fusion_list):

        if base_list[base_index] < fusion_list[fusion_index]:
            new_list.append(base_list[base_index])
            base_index += 1
        else:
            new_list.append(fusion_list[fusion_index])
            fusion_index += 1

    while base_index < len(base_list):
        new_list.append(base_list[base_index])
        base_index += 1

    while fusion_index < len(fusion_list):
        new_list.append(fusion_list[fusion_index])
        fusion_index += 1

    return new_list


def print_correct(fusion_list: List[int]) -> str:

    for number in fusion_list:
        print(f"{number} ", end="")
    
    print("")
    exit()


def incorrect_argument_count() -> None:

    if len(sys.argv) <= 3:
        print("Error")
        exit()


### Error ###

incorrect_argument_count()

### Parsing ###

complete_list = sys.argv[1:]

### Problem solving ###

fusion = fusion_split(complete_list)

sorted_fusion = fusion_sort(fusion[0],fusion[1])

correct_sentence = print_correct(sorted_fusion)

### Result ###

print(correct_sentence)