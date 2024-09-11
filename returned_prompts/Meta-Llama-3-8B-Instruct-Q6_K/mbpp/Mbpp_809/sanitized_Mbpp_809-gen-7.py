def check_smaller(tup1, tup2):
    return all(i < j for i, j in zip(tup1, tup2))  # Check if each element in tup2 is smaller than its corresponding element in tup1