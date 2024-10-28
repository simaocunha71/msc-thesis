def find_even_pair(lst):
    even_count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] ^ lst[j] % 2 == 0:
                even_count += 1
    return even_count