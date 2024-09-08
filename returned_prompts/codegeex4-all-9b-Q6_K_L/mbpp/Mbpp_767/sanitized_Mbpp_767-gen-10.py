def get_pairs_count(numbers, target_sum):
    count = 0
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == target_sum:
                count += 1
    return count