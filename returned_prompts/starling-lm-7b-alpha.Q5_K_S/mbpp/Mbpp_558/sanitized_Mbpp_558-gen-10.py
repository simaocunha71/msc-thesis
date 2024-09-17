def digit_distance_nums(num_1,num_2):
    #convert to strings to get individual digits
    num_1_str = str(num_1)
    num_2_str = str(num_2)
    #find the length of the strings
    length = max(len(num_1_str),len(num_2_str))
    #if the lengths are different, pad the smaller string
    if length > len(num_1_str):
        num_1_str = "0"*(length-len(num_1_str)) + num_1_str
    if length > len(num_2_str):
        num_2_str = "0"*(length-len(num_2_str)) + num_2_str
    #find the difference between each pair of digits
    diff = 0
    for i in range(length):
        diff += abs(int(num_1_str[i])-int(num_2_str[i]))
    return diff