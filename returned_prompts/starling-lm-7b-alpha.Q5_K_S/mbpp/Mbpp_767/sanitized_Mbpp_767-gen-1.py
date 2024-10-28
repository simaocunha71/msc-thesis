def get_pairs_count(num_list, sum):
    count = 0
    for i in range(len(num_list)):
        for j in range(i + 1, len(num_list)):
            if num_list[i] + num_list[j] == sum:
                count += 1
    return count