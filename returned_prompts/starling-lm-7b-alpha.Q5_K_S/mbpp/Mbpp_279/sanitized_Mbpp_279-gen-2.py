def is_num_decagonal(n):
    # A decagonal number is a polygonal number that is formed from a decagon.
    # The formula for decagonal numbers is n*(n+1) / 10 + 1
    decagonal_number = (n * (n + 1)) // 10 + 1
    return decagonal_number