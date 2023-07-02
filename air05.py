############### Sur chacun d'entre eux ###############

import sys

from typing import List

### Function ###

def addition(a: int, b: int) -> int:

    return a + b


def subtraction(a: int, b: int) -> int:

    return a - b


def multiplication(a: int, b: int) -> int:

    return a * b


def division(a: int, b: int) -> int | float:

    return a / b


def operation(list_to_operate: List[str], operator: str) -> List[int]:

    operated_list = []

    operator_symbol = operator[0]
    operator_number = operator[1:]

    match operator_symbol:

        case "+":
            for number in list_to_operate:
                operated_list.append(addition(int(number), int(operator_number)))
            
        case "-":
            for number in list_to_operate:
                operated_list.append(subtraction(int(number), int(operator_number)))

        case "*":
            for number in list_to_operate:
                operated_list.append(multiplication(int(number), int(operator_number)))

        case "/":
            for number in list_to_operate:
                operated_list.append(round(division(int(number), int(operator_number)), 2))

        case _:
            pass
    
    return operated_list


def print_correct(operated_list: List[int]) -> str:

    for number in operated_list:
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

    if is_number(sys.argv[1]) and is_number(sys.argv[2]):
        pass
    else:
        print("Error")
        exit()


### Error ###

incorrect_argument_count()

error_argument()

### Parsing ###

math_operation_list = sys.argv[1:-1]

operator_argument = sys.argv[-1]

### Problem solving ###

list_operate = operation(math_operation_list, operator_argument)

correct_sentance = print_correct(list_operate)

### Result ###

print(correct_sentance)