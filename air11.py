############### Afficher une pyramide ###############

import sys

### Function ###

def create_pyramide(char: str, stage: int) -> None:

    with open("pyramide.txt", mode="w") as f:
        
        index = 0
        # ↓↓↓ CODE DANGER ↓↓↓
        # while index < stage:
            
        #     space = stage - 1 + index

        #     f.write(f"{space}{char}{space}")



   


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

### Result ###

print(created_pyramide)