    letter_grades = [
        "A+",
        "A",
        "A-",
        "B+",
        "B",
        "B-",
        "C+",
        "C",
        "C-",
        "D+",
        "D",
        "D-",
        "E",
    ]
    grades_letter = []
    for grade in grades:
        for i, g in enumerate(letter_grades):
            if grade >= i:
                grades_letter.append(g)
                break
    return grades_letter


