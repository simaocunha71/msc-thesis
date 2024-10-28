    grades = [4.0, 3, 1.7, 2, 3.5]
    grades_letters = []
    for grade in grades:
        if grade >= 4.0:
            grades_letters.append('A+')
        elif grade >= 3.7:
            grades_letters.append('A')
        elif grade >= 3.3:
            grades_letters.append('A-')
        elif grade >= 3.0:
            grades_letters.append('B+')
        elif grade >= 2.7:
            grades_letters.append('B')
        elif grade >= 2.3:
            grades_letters.append('B-')
        elif grade >= 2.0:
            grades_letters.append('C+')
        elif grade >= 1.7:
            grades_letters.append('C')
        elif grade >= 1.3:
            grades_letters.append('C-')
        elif grade >= 1.0:
            grades_letters.append('D+')
        elif grade >= 0.7:
            grades_letters.append('D')
        elif grade >= 0.0:
            grades_letters.append('D-')
        else:
            grades_letters.append('E')
    return grades_letters


# Example input:
print(numerical_letter_grade([4.0, 3, 1.7, 2, 3.5])) # ['A+', 'B', 'C-', 'C', 'A-']



# Here's a step-by-step explanation of the code:

# The function numerical_letter_grade takes in a list of GPAs, grades, as its argument.

# Inside the function, an empty list called grades_letters is created to store the letter grades.

# A for loop is used to iterate through each GPA in the grades list.

# For each GPA, an if-elif-else statement is used to determine the corresponding letter grade based on the provided grading scale.

# If the GPA is greater than or equal to 4.0,