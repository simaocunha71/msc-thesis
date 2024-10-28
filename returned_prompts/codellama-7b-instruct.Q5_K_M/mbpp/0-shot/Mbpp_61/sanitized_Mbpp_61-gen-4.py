def count_Substrings(input_string):
    count = 0
    for i in range(len(input_string)):
        for j in range(i, len(input_string)):
            if sum(map(int, input_string[i:j+1])) == j+1:
                count += 1
    return count