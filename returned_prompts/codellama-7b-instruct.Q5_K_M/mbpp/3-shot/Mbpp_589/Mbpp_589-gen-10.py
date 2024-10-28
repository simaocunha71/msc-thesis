
def perfect_squares(start_num, end_num):
    result = []
    for i in range(start_num, end_num + 1):
        root = i ** 0.5
        if root == int(root):
            result.append(i)
    return result


