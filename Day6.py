test_data = [{
    "data": "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
    "solution": 7,
    "solution2": 19
}, {
    "data": "bvwbjplbgvbhsrlpgdmjqwftvncz",
    "solution": 5,
    "solution2": 23
}, {
    "data": "nppdvjthqldpwncqszvftbrmjlhg",
    "solution": 6,
    "solution2": 23
}, {
    "data": "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
    "solution": 10,
    "solution": 29
}, {
    "data": "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",
    "solution": 11,
    "solution": 26
}]

def get_start_pos(data, uniques=4):
    for i in range(0, len(data)):
        if i < len(data) - uniques - 1:
            seq: str = data[i:i + uniques]
            double = False
            for l in seq:
                if seq.count(l) > 1:
                    double = True
                    break

            if double:
                continue

            return i + uniques

for test in test_data:
    assert get_start_pos(test["data"]), test["solution"]
    assert get_start_pos(test["data"], 14), test["solution2"]

print("Test's passed")
data = ""
with open("input_data/Day6.txt") as file:
    data = file.read()

print("Solution: ", get_start_pos(data))
print("Solution 2: ", get_start_pos(data, 14))