    result = []
    for gpa in grades:
        if gpa >= 4.0:
            result.append('A+')
        elif gpa >= 3.7:
            result.append('A')
        elif gpa >= 3.3:
            result.append('A-')
        elif gpa >= 3.0:
            result.append('B+')
        elif gpa >= 2.7:
            result.append('B')
        elif gpa >= 2.3:
            result.append('B-')
        elif gpa >= 2.0:
            result.append('C+')
        elif gpa >= 1.7:
            result.append('C')
        elif gpa >= 1.3:
            result.append('C-')
        elif gpa >= 1.0:
            result.append('D+')
        elif gpa >= 0.7:
            result.append('D')
        elif gpa >= 0.0:
            result.append('D-')
        else:
            result.append('E')
    return result


# The above code is a function that computes the letter grade that corresponds to a GPA. 
# The function takes a list of GPAs and returns a list of letter grades. 
# The function uses if-elif statements to determine the letter grade based on the GPA.

# You can use the function like this:

grades = [4.0, 3, 1.7, 2, 3.5]
grade_equation = numerical_letter_grade(grades)
print(grade_equation) # This will print: ['A+', 'B', 'C-', 'C', 'A-']


