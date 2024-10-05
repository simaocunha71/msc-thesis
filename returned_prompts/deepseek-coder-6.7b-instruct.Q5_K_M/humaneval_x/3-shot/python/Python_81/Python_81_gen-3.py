    def grade_equation(grades):
        grades_out = []
        for grade in grades:
            if grade == 4.0:
                grades_out.append('A+')
            elif grade > 3.7:
                grades_out.append('A')
            elif grade > 3.3:
                grades_out.append('A-')
            elif grade > 3.0:
                grades_out.append('B+')
            elif grade > 2.7:
                grades_out.append('B')
            elif grade > 2.3:
                grades_out.append('B-')
            elif grade > 2.0:
                grades_out.append('C+')
            elif grade > 1.7:
                grades_out.append('C')
            elif grade > 1.3:
                grades_out.append('C-')
            elif grade > 1.0:
                grades_out.append('D+