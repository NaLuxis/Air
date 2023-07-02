############### Un seul à là fois ###############

import sys

### Function ###

def delete_adjacent_char(string_to_clean: str) -> str:

    new_string = ""

    index = 0 

    for lenght in range(index, len(string_to_clean)):

        if index < len(string_to_clean) - 1:  

            if string_to_clean[index] == string_to_clean[index + 1]:
                index += 1
            else:
                new_string += string_to_clean[index]
                index += 1
        else:
            new_string += string_to_clean[index]

    return new_string


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

### Parsing ###

arg_string = sys.argv[1]

### Problem solving ###

without_double = delete_adjacent_char(arg_string)

### Result ###

print(without_double)