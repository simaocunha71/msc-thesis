def div_list(list1, list2):
    if len(list1) != len(list2):
        return "Lists are of different lengths"
    result = []
    for i in range(len(list1)):
        if list2[i] == 0:
            return "Division by zero is not allowed"
        result.append(list1[i] / list2[i])
    return result