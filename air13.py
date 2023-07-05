############### Meta exercice ###############

import subprocess

### Function ###

def air_tests() -> None:

    name = ["air00.py", "air01.py", "air02.py", "air03.py", "air04.py", "air05.py",
             "air06.py", "air07.py", "air08.py", "air09.py", "air10.py", "air11.py", "air12.py"]

    arguments = [
    [["Bonjour les gars"]],
    [["Crevette magique dans la mer des étoiles", "la"]],
    [["Je", "test", "des", "trucs", " "]],
    [["1", "2", "3", "4", "5", "4", "3", "2", "1"]],
    [["Hello milady,   bien ou quoi ??"]],
    [["1", "2", "3", "4", "5", "+2"]],
    [["Michel", "Albert", "Thérèse", "Benoit", "t"]],
    [["1", "3", "4", "2"]],
    [["10", "20", "30", "fusion", "15", "25", "35"]],
    [["Michel", "Albert", "Thérèse", "Benoit"]],
    [["air10.txt"]],
    [["A", "10"]],
    [["6", "5", "4", "3", "2", "n"],["6", "5", "4", "3", "2", "n"]],
    ]

    count_success = 0

    for index in range(0, len(arguments)):

        process = subprocess.run(['/usr/bin/python3', name[index]] + arguments[index][0], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if process.returncode == 0:
            outpout = process.stdout.decode("utf-8").strip()

            for argument in arguments[index]:

                if "Error" not in outpout:
                    print(f"{name[index][:5]} ({len(arguments[index][0:])}/{len(arguments[index][0:])}) : Success")
                    count_success += 1
                else:
                    print(f"{name[index][:5]} ({len(argument[0:]) - 1}/{len(argument[0:])}) : Failure")




### Error ###



### Parsing ###



### Problem solving ###

tested = air_tests()

### Result ###

print()