
def count_reverse_pairs(strings):
    count = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if strings[i][::-1] == strings[j]:
                count += 1
    return count