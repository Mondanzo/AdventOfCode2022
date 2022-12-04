test_data = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

test_solution = 2
test_solution2 = 4

def process_data(text):
    pairs = text.split("\n")
    edited_data = []
    for pairRaw in pairs:
        pair = pairRaw.split(",")
        pairData = []
        for elf in pair:
            rangeStart, rangeEnd = elf.split("-")
            r = [d for d in range(int(rangeStart), int(rangeEnd) + 1)]
            pairData.append(r)
        pairData.sort(key=len)
        edited_data.append(pairData)
    return edited_data

def count_overlapping_pairs(data, at_all=False):
    counted_pairs = 0
    for dataField in data:
        if at_all:
            for d in dataField[0]:
                if d in dataField[1]:
                    counted_pairs += 1
                    break
        else:
            got_through = True
            for d in dataField[0]:
                if not d in dataField[1]:
                    got_through = False
                    break
            if got_through:
                counted_pairs += 1
    return counted_pairs


data = process_data(test_data)

guess_data_raw = ""
with open("input_data/Day4.txt") as file:
    guess_data_raw = file.read()
    
guess_data = process_data(guess_data_raw)
    
result = count_overlapping_pairs(data)
result2 = count_overlapping_pairs(data, True)
print("Test Result:", result, "==", test_solution)
print("Test Result 2:", result2, "==", test_solution2)
if result == test_solution and result2 == test_solution2:
    overlaps = count_overlapping_pairs(guess_data)
    at_all_overlaps = count_overlapping_pairs(guess_data, True)
    print("Solution:", overlaps)
    print("Solution 2:", at_all_overlaps)