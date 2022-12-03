test_data = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
test_solution = 157
test_solution2 = 70

alphabet = " abcdefghijklmnopqrstuvwxyz"

def do_the_thing(data: str):
    rucksacks = data.split("\n")

    sum = 0

    for rucksack in rucksacks:
        compartmentOne = rucksack[0:int(len(rucksack) / 2)]
        compartmentTwo = rucksack[int(len(rucksack) / 2):]
        for l in compartmentOne:
            if l in compartmentTwo:
                sum += get_priority(l)
                break

    return sum

def do_the_group_thing(data: str):
    rucksacks = data.split("\n")
    sum = 0
    
    for i in range(0, len(rucksacks), 3):
        rucksack = rucksacks[i]
        group_letter = ""
        for l in rucksack:
            if l in rucksacks[i + 1] and l in rucksacks[i + 2]:
                group_letter = l
                break
        sum += get_priority(group_letter)
    return sum

def get_priority(letter: str):
    value = alphabet.find(letter.lower())
    if letter.isupper():
        value += 26
    return value

data = ""
with open("input_data/Day3.txt") as file:
    data = file.read()

test_result = do_the_thing(test_data)
print("Test Result: {} ==".format(test_solution), test_result, test_result == test_solution)
if test_solution == test_solution:    
    print("Solution: ", do_the_thing(data))
    
test_result = do_the_group_thing(test_data)
print("Test Result: {}".format(test_solution2), test_result, test_result == test_solution2)
if test_solution2 == test_result:
    print("Solution 2:", do_the_group_thing(data))