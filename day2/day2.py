def check_result(round: list[str]):
    opponentOptions = ["A", "B", "C"]
    ourOptions = ["X", "Y", "Z"]
    theirPlay = round[0]
    ourPlay = round[1]

    scoreForShape = ourOptions.index(ourPlay) + 1
    resultScore = 0

    # Paper(1) beats Rock(0)
    # Scissors(2) beats Paper(1)
    # Rock(0) beats Scissors(2)

    if ourPlay == "Z" and theirPlay == "A":
        # we lose keep resultScore the same - 0
        pass
    elif ourPlay == "X" and theirPlay == "C":
        # we win, resultScore = 6
        resultScore = 6
    elif ourOptions.index(ourPlay) == opponentOptions.index(theirPlay):
        # tie, resultScore = 3
        resultScore = 3
    elif ourOptions.index(ourPlay) < opponentOptions.index(theirPlay):
        # we lose keep resultScore the same - 0
        pass
    else:
        # we win any other scenario
        resultScore = 6

    # adds score for selection and result
    return scoreForShape + resultScore


def checkResultPart2(round):
    opponentOptions = ["A", "B", "C"]
    ourOptions = ["X", "Y", "Z"]
    theirPlay = round[0]
    ourPlay = round[1]
    # ourChoice = ""

    resultScore = 0

    if theirPlay == "A":  # rock
        # lose
        if ourPlay == "X":
            ourChoice = "Z"
        # tie
        elif ourPlay == "Y":
            resultScore = 3
            ourChoice = "X"
        # win
        else:
            resultScore = 6
            ourChoice = "Y"
    elif theirPlay == "B":  # paper
        if ourPlay == "X":
            ourChoice = "X"
        elif ourPlay == "Y":
            resultScore = 3
            ourChoice = "Y"
        else:
            resultScore = 6
            ourChoice = "Z"
    elif theirPlay == "C":  # scissors
        if ourPlay == "X":  # lose
            ourChoice = "Y"  # scissors beats paper
        elif ourPlay == "Y":  # tie
            resultScore = 3
            ourChoice = "Z"  # scissors tie scissors
        else:  # win
            resultScore = 6
            ourChoice = "X"

    scoreForShape = ourOptions.index(ourChoice) + 1

    # print(
    #     theirPlay,
    #     ourPlay,
    #     ourChoice,
    #     scoreForShape,
    #     resultScore,
    #     scoreForShape + resultScore,
    # )

    return scoreForShape + resultScore


with open("./day2.txt", "r") as f:
    rounds = [play.strip().split(" ") for play in f.readlines()]

    # scores = [check_result(round) for round in rounds]
    # print(sum(scores))

    scoresPart2 = [checkResultPart2(round) for round in rounds]
    print(sum(scoresPart2))
