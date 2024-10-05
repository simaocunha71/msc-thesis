    grades_list = []
    for gpa in grades:
        if gpa == 4.0:
            grades_list.append('A+')
        elif gpa > 3.7:
            grades_list.append('A')
        elif gpa > 3.3:
grace_point_list.append('A-')
        elif gpa > 3.0:
            grades_list.append('B+')
        elif gpa > 2.7:
            grades_list.append('B')
        elif gpa > 2.3:
            grades_list.append('B-')
        elif gpa > 2.0:
            grades_list.append('C+')
        elif gpa > 1.7:
            grades_list.append('C')
        elif gpa > 1.3:
            grades_list.append('C-')
        elif gpa > 1.0:
            grades_list.append('D+')
        elif gpa > 0.7:
            grades_list.append('D')
        elif gpa > 0.0:
            grades_list.append('D-')
        else:
            grades_list.append('E')
    return grades_list

