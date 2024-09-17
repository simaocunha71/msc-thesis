
def count_reverse_pairs(words:list)->int:
    count = 0
    for i in range(len(words)):
        if words[i] == words[i][::-1]:
            count += 1
    return count


