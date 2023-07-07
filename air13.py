############### Meta exercice ###############

import subprocess

### Function ###

def air_tests() -> None:

    name = ["air00.py", "air01.py", "air02.py", "air03.py", "air04.py", "air05.py",
             "air06.py", "air07.py", "air08.py", "air09.py", "air10.py", "air11.py", "air12.py"]

    arguments_list = [
    [["Bonjour les gars"], ["1"]],
    [["Crevette magique dans la mer des étoiles", "la"], ["1"]],
    [["Je", "test", "des", "trucs", " "], ["1"]],
    [["1", "2", "3", "4", "5", "4", "3", "2", "1"], ["1"]],
    [["Hello milady,   bien ou quoi ??"], ["1", "1"]],
    [["1", "2", "3", "4", "5", "+2"], ["1"]],
    [["Michel", "Albert", "Thérèse", "Benoit", "t"], ["1"]],
    [["1", "3", "4", "2"], ["1"]],
    [["10", "20", "30", "fusion", "15", "25", "35"], ["1"]],
    [["Michel", "Albert", "Thérèse", "Benoit"], ["1"]],
    [["air10.txt"], ["1"]],
    [["A", "10"], ["1"]],
    [["6", "5", "4", "3", "2", "1"], ["1"]],
    ]

    count_success, count_tests = 0, 0

    for index in range(0, len(arguments_list)):
        valide_current_arguments = 0
        total_tests = len(arguments_list[index])

        for arguments in arguments_list[index]:
            process = subprocess.run(['/usr/bin/python3', name[index]] + arguments, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            outpout = process.stdout.decode("utf-8").strip()
                
            if "Error" not in outpout:
                    valide_current_arguments += 1
                    count_success += 1

            count_tests += 1

        if valide_current_arguments == total_tests:
            print(f"{name[index][:5]} ({valide_current_arguments}/{total_tests}) : \033[1;32mSuccess\033[0m")
        else:
            print(f"{name[index][:5]} ({valide_current_arguments}/{total_tests}) : \033[1;31mFailure\033[0m")
                
    print(f"\n    \033[1mTotal success :\033[0m ({count_success}/{count_tests})")

### Error ###



### Parsing ###



### Problem solving ###

tested = air_tests()

### Result ###

print()