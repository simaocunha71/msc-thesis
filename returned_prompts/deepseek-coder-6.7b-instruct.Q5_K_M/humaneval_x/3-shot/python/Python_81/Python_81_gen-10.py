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
            grades_out.append('D+')
        elif grade > 0.7:
            grades_out.append('D')
        elif grade > 0.0:
            grades_out.append('D-')
        else:
            grades_out.append('E')
    return grades_out


