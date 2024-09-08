def count_occurance(s):
    count = 0
    for i in range(len(s) - 2):
        if s[i:i+3] == "std":
            count += 1
    return count