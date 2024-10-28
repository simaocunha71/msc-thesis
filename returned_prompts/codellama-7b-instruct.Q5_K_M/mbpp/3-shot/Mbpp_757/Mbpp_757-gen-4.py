
def count_reverse_pairs(my_list: list) -> int:
    count = 0
    for i in range(len(my_list)):
        for j in range(i, len(my_list)):
            if my_list[i] == my_list[j][::-1]:
                count += 1
    return count


