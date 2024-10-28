    def grade_equation(gpa):
        grades = []
        for grade in gpa:
            if grade == 4.0:
                grades.append('A+')
            elif grade > 3.7:
                grades.append('A')
            elif grade > 3.3:
                grades.append('A-')
            elif grade > 3.0:
                grades.append('B+')
            elif grade > 2.7:
                grades.append('B')
            elif grade > 2.3:
                grades.append('B-')
            elif grade > 2.0:
                grades.append('C+')
            elif grade > 1.7:
                grades.append('C')
            elif grade > 1.3:
                grades.append('C-')
            elif grade > 1.0:
                grades.append('D+')
            elif grade > 0.7:
                grades.append('D')
            elif grade > 0.0:
                grades.append('D-')
            else:
                grades.append('E')
        return grades

    return grade_equation(gpa)