def count_occurance(str):
    count = 0
    for i in range(len(str)):
        if str[i:i+3] == 'std':
            count += 1
    return count