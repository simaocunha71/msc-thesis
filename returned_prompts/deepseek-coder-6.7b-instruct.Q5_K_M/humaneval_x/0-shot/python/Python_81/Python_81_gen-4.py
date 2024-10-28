
def numerical_letter_grade(grades):
    result = []
    for gpa in grades:
        if gpa == 4.0:
            result.append('A+')
        elif gpa > 3.7:
            result.append('A')
        elif gpa > 3.3:
            result.append('A-')
        elif gpa > 3.0:
            result.append('B+')
        elif gpa > 2.7:
            result.append('B')
        elif gpa > 2.3:
            result.append('B-')
        elif gpa > 2.0:
            result.append('C+')
        elif gpa > 1.7:
            result.append('C')
        elif gpa > 1.3:
            result.append('C-')
        elif gpa > 1.0:
            result.append('D+')
        elif gpa > 0.7:
            result.append('D')
        elif gpa > 0.0:
            result.append('D-')
        else:
            result.append('E')
    return result

print(numerical_letter_grade([4.0, 3, 1.7, 2, 3.5])) # ['A+', 'B', 'C-', 'C', 'A-']

# Alternative solution with list comprehension:

def numerical_letter_grade(grades):
    return ['A+' if gpa == 4.0 else 'A' if gpa > 3.7 else 'A-' if gpa > 3.3 else 
            'B+' if gpa > 3.0 else 'B' if gpa > 2.7 else 'B-' if gpa > 2.3 else 
            'C+' if gpa > 2.0 else 'C' if gpa > 1.7 else 'C-' if gpa > 1.3 else 
            'D+' if gpa > 1.0 else 'D' if gpa > 0.7 else 'D-' if gpa > 0.0 else 'E' 
            for gpa in grades]

print(numerical_letter_grade([4.