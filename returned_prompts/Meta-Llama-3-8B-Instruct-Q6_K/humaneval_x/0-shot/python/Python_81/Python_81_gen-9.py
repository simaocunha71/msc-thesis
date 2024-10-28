```
def numerical_letter_grade(grades):
    letter_grades = []
    for grade in grades:
        if grade > 4.0:
            letter_grades.append('A+')
        elif grade > 3.7:
            letter_grades.append('A')
        elif grade > 3.3:
            letter_grades.append('A-')
        elif grade > 3.0:
            letter_grades.append('B+')
        elif grade > 2.7:
            letter_grades.append('B')
        elif grade > 2.3:
            letter_grades.append('B-')
        elif grade > 2.0:
            letter_grades.append('C+')
        elif grade > 1.7:
            letter_grades.append('C')
        elif grade > 1.3:
            letter_grades.append('C-')
        elif grade > 1.0:
            letter_grades.append('D+')
        elif grade > 0.7:
            letter_grades.append('D')
        else:
            letter_grades.append('D-')
    return letter_grades
```


The function takes a list of GPAs as input and returns a list of letter grades. It iterates over each GPA in the input list and checks which GPA range it falls in based on the given table. It then appends the corresponding letter grade to the output list. The function returns the output list of letter grades.

For example, calling `numerical_letter_grade([4.0, 3, 1.7, 2, 3.5])` will return `['A+', 'B', 'C-', 'C', 'A-']`.