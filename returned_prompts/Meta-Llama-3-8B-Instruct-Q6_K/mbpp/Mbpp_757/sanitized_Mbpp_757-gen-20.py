def count_reverse_pairs(lst):
    reverse_pairs = 0
    for string in lst:
        reversed_str = string[::-1]
        if reversed_str in lst and string != reversed_str:
            reverse_pairs += 1
    return reverse_pairs