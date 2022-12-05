import typing
import copy

test_data = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

test_solution = "CMZ"
test_solution2 = "MCD"


def read_data(data:str) -> list[typing.Dict[int, list[str]], list[list[int]]]:
    lines = data.splitlines()
    crates_stack: typing.Dict[int, list[str]] = {}
    cleaned_crates = []
    commands = []

    reading_commands = False

    for line in lines:
        if "1" in line and not reading_commands:
            for d in line.replace(" ", ""):
                crates_stack[int(d)] = []
            continue

        elif line == "":
            reading_commands = True

        if reading_commands and line.startswith("move"):
            command = [int(i) for i in line.split(" ")[1:6:2]]
            commands.append(command)

        elif not reading_commands:
            counter = 0
            crates = []
            t_line = ""
            for l in line:
                counter += 1
                if counter == 4:
                    crates.append(t_line)
                    t_line = ""
                    counter = 0
                    continue
                t_line += l
            crates.append(t_line)
            cleaned_crates.append(crates)

    for clean_crates in cleaned_crates:
        for i in range(0, len(clean_crates)):
            if not clean_crates[i].strip(" ") == "":
                crates_stack.get(i + 1).append(clean_crates[i][1])

    for k in crates_stack.keys():
        crates_stack.get(k).reverse()

    return crates_stack, commands

def sort_crates(crts: typing.Dict[int, list[str]], commands: list[list[int]], multiple=False, debug=False):
    if(debug):
        print(crts)
    for command in commands:
        if(debug):
            print("move {0} from {1} to {2}".format(command[0], command[1], command[2]))
        if not multiple:
            for _c in range(command[0]):
                crts[command[2]].append(crts[command[1]].pop())
        else:
            crts[command[2]].extend(crts[command[1]][-command[0]:])
            crts[command[1]] = crts[command[1]][0:-command[0]]
            if(debug):
                print(crts)


def get_top_crates(crates):
    result = ""
    for crate_row in crates.values():
        result += crate_row[-1]

    return result

crates, commands = read_data(test_data)
crates2 = copy.deepcopy(crates)
sort_crates(crates, commands)
sort_crates(crates2, commands, True, True)

test_result = get_top_crates(crates)
test_result2 = get_top_crates(crates2)

print("Test Result 2:", test_result2, "==", test_solution2)
print("Test Result:", test_result, "==", test_solution)
if test_result == test_solution:
    data = ""
    with open("input_data/Day5.txt") as file:
        data = file.read()
    probe_crates, commands = read_data(data)
    probe_crates2 = copy.deepcopy(probe_crates)

    sort_crates(probe_crates, commands)
    solution = get_top_crates(probe_crates)

    sort_crates(probe_crates2, commands, True)
    solution2 = get_top_crates(probe_crates2)
    print("Solution:", solution)
    print("Solution 2:", solution2)