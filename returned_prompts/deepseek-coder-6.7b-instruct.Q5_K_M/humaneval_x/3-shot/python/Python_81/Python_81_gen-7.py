    def grade_equation(gpas):
        grades = []
        for gpa in gpas:
            if gpa == 4.0:
                grades.append('A+')
            elif gpa > 3.7:
                grades.append('A')
            elif gpa > 3.3:
                grades.append('A-')
            elif gpa > 3.0:
                grades.append('B+')
            elif gpa > 2.7:
                grades.append('B')
            elif gpa > 2.3:
                grades.append('B-')
            elif gpa > 2.0:
                grades.append('C+')
            elif gpa > 1.7:
                grades.append('C')
            elif gpa > 1.3:
                grades.append('C-')
            elif gpa > 1.0:
                grades.append('D+')
            elif gpa > 0.7:
                grades.append('D')
            elif gpa > 0.0:
                grades.append('D-')
            else:
                grades.append('E')
        return grades

    return grade_equation(grades)


