def digit_distance_nums(num1, num2):
    num_str1 = str(num1)
    num_str2 = str(num2)
    if len(num_str1) != len(num_str2):
        raise ValueError("The two numbers must be the same length")
    return sum(abs(int(num_str1[i]) - int(num_str2[i])) for i in range(len(num_str1)))