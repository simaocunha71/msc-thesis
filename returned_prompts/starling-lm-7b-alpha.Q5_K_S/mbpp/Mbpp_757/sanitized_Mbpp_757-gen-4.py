def count_reverse_pairs(s_list):
    pairs = 0
    for i in range(len(s_list)):
        for j in range(i + 1, len(s_list)):
            if s_list[i] == s_list[j][::-1]:
                pairs += 1
    return pairs