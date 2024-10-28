    letter_grades = [
        'E', 'D-', 'D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+']

    result = []

    for gpa in grades:
        for i, letter_grade in enumerate(letter_grades):
            if gpa < i + 0.7:
                result.append(letter_grade)
                break

    return result


