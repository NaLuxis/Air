############### Chercher l'intrus ###############

import sys

from typing import List

### Function ###

def find_intruder(array_to_find: List[str | int]) -> str | int:
    
    intruder_deleter_array = {}

    here = 1

    for element in array_to_find:

        if not element in intruder_deleter_array:
            intruder_deleter_array[f"{element}"] = here
        else:
            intruder_deleter_array[f"{element}"] = here + 1

    for key, value in intruder_deleter_array.items():

        if value == 1:
            return key



def incorrect_argument_count() -> None:

    if len(sys.argv) <= 3:
        print("Error")
        exit()


### Error ###

incorrect_argument_count()


### Parsing ###

array_intruder = sys.argv[1:]

### Problem solving ###

finded_intruder = find_intruder(array_intruder)

### Result ###

print(finded_intruder)