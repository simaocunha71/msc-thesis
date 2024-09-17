def find_even_pair(lst):
    even_pairs = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if (lst[i] ^ lst[j]) % 2 == 0:
                even_pairs += 1
    return even_pairs