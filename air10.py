############### Afficher le contenu ###############

import sys

### Function ###

def read_my_file(my_file: str) -> str | None:

    try:
        with open(my_file, "r") as f:
            content = f.read()

            if not content:
                print("The file is empty")
                exit()
            
            if content:
                return content
        
    except FileNotFoundError:
        print(f"File : {my_file} don't exist")
        exit()


def incorrect_argument_count() -> None:

    if len(sys.argv) != 2:
        print("Error")
        exit()


### Error ###

incorrect_argument_count()

### Parsing ###

my_file = sys.argv[1]

### Problem solving ###

readed_file = read_my_file(my_file)

### Result ###

print(readed_file)