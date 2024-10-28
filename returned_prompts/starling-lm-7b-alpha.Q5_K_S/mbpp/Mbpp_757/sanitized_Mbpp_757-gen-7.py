def count_reverse_pairs(strings):
    # Your code here
    count = 0
    for s in strings:
        reverse = s[::-1]
        if reverse in strings:
            count += 1
    return count