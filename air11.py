############### Afficher une pyramide ###############

import sys

### Function ###

def create_pyramide(char: str, stage: int) -> None:

    with open("pyramide.txt", mode="w") as f:

        index = 0
        number_char = 1

        while index < stage:
            
            space_one = stage - 1 - index
            space_two = stage - 1 + index

            if index < stage - 1:
                f.write(" " * space_one + char * number_char + " " * space_two + "\n" )
            else:
                f.write(" " * space_one + char * number_char + " " * space_two)
          
            index += 1
            number_char += 2


def display_pyramide() -> None:

    with open("pyramide.txt", mode="r") as f:
        content = f.read()

        if not content:
            print("The file is empty")
            exit()
        
        if content:
            return content


def incorrect_argument_count() -> None:

    if len(sys.argv) != 3:
        print("Error")
        exit()

def is_number(target: any) -> bool:

    if str(target).lstrip("-+").isdigit():
        return True
    else:
        return False


def error_argument() -> None:

    incorrect_argument_count()

    if not is_number(sys.argv[2]):
        print("Error")
        exit()

### Error ###

error_argument()

### Parsing ###

pyramide_char = sys.argv[1]

pyramide_stage = int(sys.argv[2])

### Problem solving ###

created_pyramide = create_pyramide(pyramide_char, pyramide_stage)

show_pyramide = display_pyramide()

### Result ###

print(show_pyramide)