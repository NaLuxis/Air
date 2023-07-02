############### Contrôle de pass sanitaire ###############

import sys

from typing import List

### Function ###

def search_items(search_list: List[str], compare_string: str) -> List[str] | None:

    new_list = []
    
    for element in search_list:
        
        index = 0

        is_in = False

        while index < len(element) - len(compare_string) + 1:

            sub_string = element[index : index + len(compare_string)]

            if sub_string.lower() == compare_string.lower():
                is_in = True
                break

            index += 1
        
        if not is_in:
            new_list.append(element)
    
    if not new_list:
        print("La liste est vide")
        exit()
    
    return new_list


def print_correct(searched_list: List[int]) -> str:

    for element in searched_list:

        if element != searched_list[-1]:
            print(f"{element}, ", end="")
        else:
            print(f"{element} ", end="")
    
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


def is_string(target: any) -> bool:

    if type(target) == str:
        return True
    else:
        return False


def error_argument() -> None:

    for element in sys.argv[1:]:

        if is_string(element):
            pass
        else:
            print("Error")
            exit()

        if is_number(element):
            print("Error")
            exit()


### Error ###

incorrect_argument_count()

error_argument()

### Parsing ###

list_to_compare = sys.argv[1:-1]

string_search = sys.argv[-1]

### Problem solving ###

searched_items = search_items(list_to_compare, string_search)

correct_sentance = print_correct(searched_items)

### Result ###

print(correct_sentance)