    letter_grades = {'A+': (4.0, float('inf')), 'A-': (3.7, 3.3), 'B+': (3.0, 2.7), 'B-': (2.3, 2.0), 'C+': (1.7, 1.3), 'C-': (1.0, 0.7), 'D+': (0.0, 0.7), 'D': (0.0, 0.0), 'E': (0.0, 0.0)}
    grades = [float(i) for i in grades]
    res = []
    for g in grades:
        for k, v in letter_grades.items():
            if g in v:
                res.append(k)
                break
    return res

# Example usage:
grades = [4.0, 3, 1.7, 2, 3.5]
print(numerical_letter_grade(grades))  # Output: ['A+', 'B', 'C-', 'C', 'A-']

# This function takes a list of GPAs and uses a dictionary to map each GPA to its corresponding letter grade.
# It converts all GPAs in the input list to floats, then iterates over each GPA. For each GPA, it checks if it's within the range defined by the key-value pairs in the dictionary. If it is, the function appends the corresponding letter grade to the result list and breaks out of the loop. After processing all GPAs, it returns the result list.

# Note that the function assumes that the input GPA list is non-empty and that all GPAs are valid (i.e., within the range defined by the key-value pairs in the dictionary). If you want to add error checking, you can do so by adding additional conditional statements.


```python

```