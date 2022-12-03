puzzle_clues = {
    "A": 0,  # Rock
    "X": 0,
    "B": 1, # Paper
    "Y": 1,
    "C": 2, # Scissors
    "Z": 2
}

rock_paper_scissors = [
    1,
    2,
    3
]

round_outcomes = {
    "lose": 0,
    "draw": 3,
    "win": 6
}

def get_shape_score(shape):
    if shape >= len(rock_paper_scissors):
        shape = 0
    return rock_paper_scissors[shape]


def get_round_outcome(encrypted):
    if encrypted == "X":
        return "lose"
    if encrypted == "Y":
        return "draw"
    if encrypted == "Z":
        return "win"


# Solution Part 1
def calculate_round(enemy_action: str, my_action: str):
    if  get_shape_score(puzzle_clues[enemy_action]) == get_shape_score(puzzle_clues[my_action]):
        return round_outcomes["draw"] + get_shape_score(puzzle_clues[my_action])

    if get_shape_score(puzzle_clues[my_action] - 1) == get_shape_score(puzzle_clues[enemy_action]):
        return round_outcomes["win"] + get_shape_score(puzzle_clues[my_action])
    
    return round_outcomes["lose"] + get_shape_score(puzzle_clues[my_action])


# Solution Part 2
def calculate_round_part_two(enemy_action: str, outcome: str):
    if get_round_outcome(outcome) == "draw":
        return round_outcomes["draw"] + get_shape_score(puzzle_clues[enemy_action])
    if get_round_outcome(outcome) == "lose":
        return round_outcomes["lose"] + get_shape_score(puzzle_clues[enemy_action] - 1)
    if get_round_outcome(outcome) == "win":
        return round_outcomes["win"] + get_shape_score(puzzle_clues[enemy_action] + 1)



puzzle_input = list()
with open("input_data/Day2.txt") as file:
    while True:
        line = file.readline()

        if line == "":
            break

        puzzle_input.append(line.removesuffix("\n"))

total_score = 0
total_score_fraud = 0

for round in puzzle_input:
    args = round.split(" ")
    total_score += calculate_round(args[0], args[1])
    total_score_fraud += calculate_round_part_two(args[0], args[1])

print("Total Score 1: ", total_score)
print("Total Score 2: ", total_score_fraud)