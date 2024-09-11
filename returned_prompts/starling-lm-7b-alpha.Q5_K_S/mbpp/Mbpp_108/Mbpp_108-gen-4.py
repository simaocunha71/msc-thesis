def merge_sorted_list(list_a, list_b, list_c):
    list_a.extend(list_b)
    list_a.extend(list_c)
    list_a.sort()
    return list_a

merge_sorted_list([25, 24, 15, 4, 5, 29, 110],[19, 20, 11, 56, 25, 233, 154],[24, 26, 54, 48])

# Alternative solution
def merge_sorted_list(list_a, list_b, list_c):
    return sorted(list(list_a) + list(list_b) + list(list_c))

merge_sorted_list([25, 24, 15, 4, 5, 29, 110],[19, 20, 11, 56, 25, 233, 154],[24, 26, 54, 48])


# Another solution
def merge_sorted_list(list_a, list_b, list_c):
    return sorted(list_a + list_b + list_c)

merge_sorted_list([25, 24, 15, 4, 5, 29, 110],[19, 20, 11, 56, 25, 233, 154],[24, 26, 54, 48])

# Another alternative solution
def merge_sorted_list(list_a, list_b, list_c):
    return sorted(list_a + list_b + list_c, reverse=True)

merge_sorted_list([25, 24, 15, 4, 5, 29, 110],[19, 20, 11, 56, 25, 233, 154],[2