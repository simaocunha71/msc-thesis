def magic_square_test(matrix):
    def is_square(matrix):
        return all(len(row) == len(matrix) for row in matrix)

    def is_magic(matrix):
        n = len(matrix)
        expected_sum = sum(matrix[0])

        # Check rows
        for row in matrix:
            if sum(row) != expected_sum:
                return False

        # Check columns
        for col in range(n):
            if sum(matrix[row][col] for row in range(n)) != expected_sum:
                return False

        # Check diagonals
        if sum(matrix[i][i] for i in range(n)) != expected_sum:
            return False
        if sum(matrix[i][n-i-1] for i in range(n)) != expected_sum:
            return False

        return True

    return is_square(matrix) and is_magic(matrix)