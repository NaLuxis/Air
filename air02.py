############### Concat ###############

import sys

### Function ###




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



### Result ###

print()