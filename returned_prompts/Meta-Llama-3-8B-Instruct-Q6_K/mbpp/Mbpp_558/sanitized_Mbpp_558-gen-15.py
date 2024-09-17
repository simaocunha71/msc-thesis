def digit_distance_nums(num1, num2):
    max_num = max(num1, num2)
    min_num = min(num1, num2)
    
    distance = 0
    for i in range(len(str(max_num))):
        if i >= len(str(min_num)):
            break
        distance += abs(int(str(max_num)[i]) - int(str(min_num)[i]))
    
    return distance