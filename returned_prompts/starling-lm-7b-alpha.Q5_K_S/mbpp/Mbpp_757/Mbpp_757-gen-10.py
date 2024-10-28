
def count_reverse_pairs(words):
    cnt = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if words[i] == words[j][::-1]:
                cnt += 1
    return cnt


