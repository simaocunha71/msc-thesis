def centered_hexagonal_number(n):
    # The centered hexagonal number is a hexagonal number
    # where the first row has one more number than the row below it.
    # The nth centered hexagonal number is the sum of the first n rows
    # of hexagonal numbers, where the nth row has one more number
    # than the previous row.
    # The sum of the first k rows of hexagonal numbers is
    # (k^3 + k) / 6
    # So, the nth centered hexagonal number is
    # (1^3 + 1) / 6 + (2^3 + 2) / 6 + ... + (n^3 + n) / 6
    # = (1 + 2 + ... + n) * (n^2 + n + 2) / 6
    # = (n * (n + 1) * (2n + 1)) / 6
    # = (n * (n + 1) * (2n + 1)) / 6
    return (n * (n + 1) * (2 * n + 1)) // 6