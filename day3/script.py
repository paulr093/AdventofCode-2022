lower_case = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

upper_case = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]

# part 1
# with open("./input.txt", "r") as f:
#     allLines = [
#         [line.strip()[: len(line.strip()) // 2], line.strip()[len(line.strip()) // 2 :]]
#         for line in f.readlines()
#     ]

#     sim_letters = {}
#     all_priority_nums = []

#     for idx, combo in enumerate(allLines):
#         priority = 0
#         for letter in combo[0]:
#             if letter in combo[1]:
#                 sim_letters[idx] = letter

#     for lett in sim_letters:
#         if sim_letters[lett] in lower_case:
#             all_priority_nums.append(lower_case.index(sim_letters[lett]) + 1)
#         else:
#             all_priority_nums.append(upper_case.index(sim_letters[lett]) + 27)

#     print(sum(all_priority_nums), len(allLines), len(all_priority_nums))

# part 2
with open("./input.txt", "r") as f:
    all_lines = [line.strip() for line in f.readlines()]
    lines_grouped_by_three = {}
    starting_idx = 0

    for idx, line in enumerate(all_lines):
        if idx % 3 == 0:
            starting_idx += 1

        if starting_idx in lines_grouped_by_three:
            lines_grouped_by_three[starting_idx].append(line)
        else:
            lines_grouped_by_three[starting_idx] = [line]

    sim_lett_by_group = {}

    # print(lines_grouped_by_three[1][0])
    for group in lines_grouped_by_three:
        for char in lines_grouped_by_three[group][0]:
            if (
                char in lines_grouped_by_three[group][1]
                and char in lines_grouped_by_three[group][2]
            ):
                sim_lett_by_group[group] = char

    priority_nums_grouped = []

    for key in sim_lett_by_group:
        if sim_lett_by_group[key] in lower_case:
            priority_nums_grouped.append(lower_case.index(sim_lett_by_group[key]) + 1)
        else:
            priority_nums_grouped.append(upper_case.index(sim_lett_by_group[key]) + 27)

    print(sum(priority_nums_grouped))
