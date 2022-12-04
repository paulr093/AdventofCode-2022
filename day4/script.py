with open("./input.txt", "r") as f:
    ranges = {idx: line.strip().split(",") for idx, line in enumerate(f.readlines())}

    ranges = {
        key: [ranges[key][0].split("-"), ranges[key][1].split("-")] for key in ranges
    }

    pairs = 0
    overlaps = 0

    for key in ranges:
        first_low = int(ranges[key][0][0])
        first_high = int(ranges[key][0][1])
        second_low = int(ranges[key][1][0])
        second_high = int(ranges[key][1][1])

        # part 1
        # if first low is lower than second low than second high has to be lower than first high
        # or if first low is greater than second low than first high has to be les than second high
        if (
            first_low <= second_low
            and second_high <= first_high
            or first_low >= second_low
            and first_high <= second_high
        ):
            print(ranges[key][0], ranges[key][1], "in range")
            pairs += 1

        # part 2 - find overlaps
        # if first low is lower than second low than second low has to be lower than first high
        # or if first low is greater than second low than second high has to be greater than first low
        if (first_low <= second_low and second_low <= first_high) or (
            first_low >= second_low and second_high >= first_low
        ):
            print(ranges[key][0], ranges[key][1], "overlaps")
            overlaps += 1

    print(f"Pairs: {pairs}", f"Overlaps: {overlaps}")
