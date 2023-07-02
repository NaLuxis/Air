############### Concat ###############

import sys

from typing import List

### Function ###

def concat(list_to_concat: List[str], separator: str) -> str:

    new_list = []

    for element in list_to_concat:

        if list_to_concat[-1] == element:
            new_list.append(element)
        else:
            new_list.append(element)
            new_list.append(separator)

    for element in new_list:
        concat_string = "".join(new_list)

    return concat_string


def incorrect_argument_count() -> None:

    if len(sys.argv) <= 3:
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

list_to_concat = sys.argv[1:-1]

separator = sys.argv[-1]

### Problem solving ###

concated_string = concat(list_to_concat, separator)

### Result ###

print(concated_string)