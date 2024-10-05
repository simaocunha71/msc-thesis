    grade_dict = {4.0: 'A+', 3.7: 'A', 3.3: 'A-', 3.0: 'B+', 2.7: 'B', 2.3: 'B-', 2.0: 'C+', 1.7: 'C', 1.3: "C-", 1.0: 'D+', 0.7: 'D', 0: 'E'}
    grades_list = []
    for grade in grades:
        for k in sorted(grade_dict.keys(), reverse=True):
            if grade >= k:
                grades_list.append(grade_dict[k])
                break
    return grades_list



A: 
    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx  != idx2:
                distance  = abs(elem  - elem2)
                if distance  < threshold:
                    return True

    return False


