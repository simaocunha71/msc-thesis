def count_Substrings(str):
    count = 0
    for i in range(1,len(str)+1):
        for j in range(len(str)):
            if len(str[j:j+i]) == sum([int(x) for x in str[j:j+i]]):
                count += 1
    return count