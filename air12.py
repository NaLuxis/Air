############### Le roi des tris ###############

import sys

from typing import List

### Function ###

def quick_sort(list_to_sort: List[str]) -> List[int]:

    if len(list_to_sort) < 2:
        return list_to_sort

    pivot = list_to_sort[-1]

    shorter = [element for element in list_to_sort[:-1] if element <= pivot]
    greater = [element for element in list_to_sort[:-1] if element > pivot]

    return quick_sort(shorter) + [pivot] + quick_sort(greater)


def print_correct(quick_list: List[int]) -> str:

    for number in quick_list:
        print(f"{number} ", end="")
    
    print("")
    exit()


def incorrect_argument_count() -> None:

    if len(sys.argv) <= 2:
        print("Error")
        exit()

def is_number(target: any) -> bool:

    if str(target).lstrip("-+").isdigit():
        return True
    else:
        return False


def error_argument() -> None:

    incorrect_argument_count()

    for element in sys.argv[1:]:

        if not is_number(element):
            print("Error")
            exit()


### Error ###

error_argument()

### Parsing ###

list_to_quick_sort = sys.argv[1:]

### Problem solving ###

sorted_quick = quick_sort(list_to_quick_sort)

correct_sentence = print_correct(sorted_quick)

### Result ###

print(correct_sentence)