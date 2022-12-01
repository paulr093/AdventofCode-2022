with open("./day1input.txt", "r") as f:
    allNums = [num.rstrip() for num in f]

    arrayOfSections = []
    secArray = []

    for ele in allNums:
        if ele == "":
            arrayOfSections.append(secArray)
            secArray = []
        else:
            secArray.append(int(ele))

    sumOfSection = [sum(sec) for sec in arrayOfSections]

    sumOfTop3 = sum(sorted(sumOfSection, reverse=True)[:3])

    print("Your max number is " + str(max(sumOfSection)))

    print(f"Here is your top 3 total: {sumOfTop3}")
