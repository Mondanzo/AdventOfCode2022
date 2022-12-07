import typing
import pathlib

test_data = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""
test_solution = 95437
test_solution2 = 24933642

max_size = 70000000
update_size = 30000000

def parse_input(data: str):
    current_folder = "/"
    lines = data.split("\n")

    folder_mapping = {

    }

    reading_folder = False
    for line in lines:
        if line.startswith("$"):
            reading_folder = False
            # Command
            args = line.split(" ")
            if args[1] == "cd":
                path = args[2]
                if path == "..":
                    current_folder = "/".join(current_folder.split("/")[0:-2]) + "/"
                elif path == "/":
                    current_folder = "/"
                else:
                    current_folder += path + "/"
            elif args[1] == "ls":
                reading_folder = True

        elif reading_folder:
            if line.startswith("dir"):
                continue
            folders = current_folder.split("/")
            for t_folder in range(len(folders)):
                folder = ".".join(folders[0:t_folder])
                if t_folder == 0:
                    folder = "/"
                if folder not in folder_mapping:
                    folder_mapping[folder] = 0
                folder_mapping[folder] += int(line.split(" ")[0])

    return folder_mapping


def get_file_size(folder_mapping, threshold=100000):
    sum = 0
    if threshold == -1:
        return folder_mapping["/"]
    for folder in folder_mapping:
        if folder_mapping[folder] <= threshold:
            sum += folder_mapping[folder]
    return sum


def get_size_to_clear(folders, required_size: int, free_size: int):
    print("Required Size:", required_size)
    print("Free Size:", free_size)
    smallest_size = None
    for folder in folders:
        if folders[folder] + free_size >= required_size:
            if smallest_size is None or smallest_size > folders[folder]:
                smallest_size = folders[folder]
    return smallest_size


folder_mapping = parse_input(test_data)

test_result = get_file_size(folder_mapping)
test_result2 = get_size_to_clear(folder_mapping, update_size, max_size - get_file_size(folder_mapping, -1))

print(test_result, test_solution)
print(test_result2, test_solution2)
assert test_result == test_solution
assert test_result2 == test_solution2
print("Tests succeeded")

data = ""
with open("input_data/Day7.txt") as file:
    data = file.read()

mapped_folders = parse_input(data)

result = get_file_size(mapped_folders)
result2 = get_size_to_clear(mapped_folders, update_size, max_size - get_file_size(mapped_folders, -1))

print("Solution:", result)
print("Solution 2:", result2)
