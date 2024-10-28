def get_total_number_of_sequences(m: int, n: int) -> int:
    def helper(i: int, prev: int) -> int:
        if i == n:
            return 1
        count = 0
        for j in range(2 * prev, min(m, 2 * prev + 1)):
            count += helper(i + 1, j)
        return count
    return helper(0, 0)