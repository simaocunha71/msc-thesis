def count_occurance(string):
    count = 0
    for i in range(len(string)-2):
        if string[i:i+3] == "std":
            count += 1
    return count