
def count_reverse_pairs(string_list):
    cnt = 0
    for i in range(len(string_list)):
        for j in range(i+1, len(string_list)):
            if string_list[i] == string_list[j][::-1]:
                cnt += 1
    return cnt


