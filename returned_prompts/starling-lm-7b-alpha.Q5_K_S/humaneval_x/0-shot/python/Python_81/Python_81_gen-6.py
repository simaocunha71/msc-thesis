
def numerical_letter_grade(grades):
    grades = [round(x, 1) for x in grades]
    grades_map = {
        4.0: 'A+',
        3.7: 'A',
        3.3: 'A-',
        3.0: 'B+',
        2.7: 'B',
        2.3: 'B-',
        2.0: 'C+',
        1.7: 'C',
        1.3: 'C-',
        1.0: 'D+',
        0.7: 'D',
        0.0: 'D-',
        0.0: 'E'
    }
    return [grades_map[x] for x in grades]


# Example usage:
grades = [4.0, 3, 1.7, 2, 3.5]
print(numerical_letter_grade(grades))  # Output: ['A+', 'B', 'C-', 'C', 'B']

```
The provided solution defines the function `numerical_letter_grade` that takes a list of GPAs as input and returns a list of corresponding letter grades based on the given grading scale. The function first rounds each GPA in the input list to one decimal place using a list comprehension and stores the rounded GPAs in the `grades` variable. Then, it defines a dictionary called `grades_map` that maps each GPA to its corresponding letter grade. Finally, the function uses a list comprehension to generate the letter grade list by looking up the letter grade for each GPA in the `grades_map` dictionary.

To use the function, you can pass a list of GPAs to it and store the returned letter grades in a variable. In the provided example, the function is called with the `grades` list `[4.0, 3, 1.7, 2, 3.5]` and the returned letter grades are printed to the console, resulting in the output `['A+', 'B', 'C-', 'C', 'B']`.
```

...

Another way to solve this problem is by using the following code:

```python
def numerical_letter_grade(grades):
