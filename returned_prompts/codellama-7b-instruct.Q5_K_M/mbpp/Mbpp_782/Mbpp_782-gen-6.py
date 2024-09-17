
def odd_length_sum(my_list: list) -> int:
    if len(my_list) == 0:
        return 0
    else:
        total = 0
        for i in range(0, len(my_list)):
            for j in range(i+1, len(my_list)):
                if j - i + 1 % 2 == 1:
                    total += my_list[j]
        return total


