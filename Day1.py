calories = []

current_calories = 0

with open("input_data/Day1.txt") as file:
    while True:
        line = file.readline()

        # End of inventory
        if line == "\n" or line == "":
            calories.append(current_calories)
            current_calories = 0

            # EOF
            if line == "":
                break
            continue
        else:
            current_calories += int(line.removesuffix("\n"))

calories.sort(reverse=True)

print("Most Calories: ", calories[0])
print("Top 3 Calories: ", calories[0] + calories[1] + calories[2])