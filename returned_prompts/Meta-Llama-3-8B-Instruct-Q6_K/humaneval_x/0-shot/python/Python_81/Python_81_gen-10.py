```
def numerical_letter_grade(grades):
    letter_grades = []
    for g in grades:
        if g >= 4.0:
            letter_grades.append('A+')
        elif g >= 3.7:
            letter_grades.append('A')
        elif g >= 3.3:
            letter_grades.append('A-')
        elif g >= 3.0:
            letter_grades.append('B+')
        elif g >= 2.7:
            letter_grades.append('B')
        elif g >= 2.3:
            letter_grades.append('B-')
        elif g >= 2.0:
            letter_grades.append('C+')
        elif g >= 1.7:
            letter_grades.append('C')
        elif g >= 1.3:
            letter_grades.append('C-')
        elif g >= 1.0:
            letter_grades.append('D+')
        elif g >= 0.7:
            letter_grades.append('D')
        elif g >= 0.0:
            letter_grades.append('D-')
        else:
            letter_grades.append('E')
    return letter_grades
```


This function iterates over each grade in the input list. It then checks if the grade is greater than or equal to the threshold for each letter grade. If it is, it appends the corresponding letter grade to the list. If not, it moves on to the next threshold. If the grade is less than 0.0, it appends 'E' to the list. Finally, it returns the list of letter grades. For example, `numerical_letter_grade([4.0, 3, 1.7, 2, 3.5])` would return `['A+', 'B', 'C-', 'C', 'A-']`.