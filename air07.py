############### Insertion dans un tableau trié ###############

import sys

from typing import List

### Function ###

def sort_insert(sorted_list: List[str], new_element: int) -> List[int]:

    new_list = []
    inserted = False
    index = 0

    for number in sorted_list:
        number = int(number)
        
        if number < new_element:
            index += 1
            pass
        else:
           if number < new_element or inserted:
                pass
           else:
                new_list.insert(index, new_element)
                index += 1
                inserted = True

        new_list.append(number)

    if not inserted:
        new_list.append(new_element)

    return new_list


def print_correct(sorted_list: List[int]) -> str:

    for number in sorted_list:
        print(f"{number} ", end="")
    
    print("")
    exit()


def incorrect_argument_count() -> None:

    if len(sys.argv) <= 3:
        print("Error")
        exit()


def is_number(target: any) -> bool:

    if str(target).lstrip("-+").isdigit():
        return True
    else:
        return False


def error_argument() -> None:

    for element in sys.argv[1:]:

        if not is_number(element):
            print("Error")
            exit()


### Error ###

incorrect_argument_count()

error_argument()

### Parsing ###

list_sorted = sys.argv[1:-1]

element_to_sort = int(sys.argv[-1])

### Problem solving ###

sorted_insert = sort_insert(list_sorted, element_to_sort)

correct_sentance = print_correct(sorted_insert)

### Result ###

print(correct_sentance)