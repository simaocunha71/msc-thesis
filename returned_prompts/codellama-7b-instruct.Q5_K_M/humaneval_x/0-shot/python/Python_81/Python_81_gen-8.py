
def numerical_letter_grade(grades):
    grades = [grade for grade in grades if grade > 0]
    letter_grades = []
    for grade in grades:
        if grade >= 4.0:
            letter_grades.append('A+')
        elif grade >= 3.7:
            letter_grades.append('A')
        elif grade >= 3.3:
            letter_grades.append('A-')
        elif grade >= 3.0:
            letter_grades.append('B+')
        elif grade >= 2.7:
            letter_grades.append('B')
        elif grade >= 2.3:
            letter_grades.append('B-')
        elif grade >= 2.0:
            letter_grades.append('C+')
        elif grade >= 1.7:
            letter_grades.append('C')
        elif grade >= 1.3:
            letter_grades.append('C-')
        elif grade >= 1.0:
            letter_grades.append('D+')
        elif grade >= 0.7:
            letter_grades.append('D')
        else:
            letter_grades.append('D-')
    return letter_grades


B:

def numerical_letter_grade(gpas):
    grades = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-']
    return [grades[i] for i in range(len(gpas)) if gpas[i] >= 4.0]


C:

def numerical_letter_grade(grades):
    return [
        'A+' if g >= 4.0 else 'A' if g >= 3.7 else 'A-' if g >= 3.3 else 'B+' if g >= 3.0 else 'B' if g >= 2.7 else 'B-' if g >= 2.3 else 'C+' if g >= 2.0 else 'C' if g >= 