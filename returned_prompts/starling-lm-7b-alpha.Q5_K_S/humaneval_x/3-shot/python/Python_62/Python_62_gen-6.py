    def create_derivative_table(xs: List[int]) -> List[List[int]]:
        table = [[0 for _ in range(len(xs))] for _ in range(len(xs))]
        for i in range(len(xs)):
            table[i][0] = xs[i]
        for j in range(1, len(xs)):
            for i in range(j, len(xs)):
                table[i][j] = table[i-1][j-1] * (i - j + 1)
        return table

    def find_maximum(xs: List[int], table: List[List[int]]) -> int:
        maximum = len(table) - 1
        for idx in range(len(table)):
            if table[idx][maximum] != 0:
                maximum = idx
        return maximum

    def extract_derivative(xs: List[int], maximum: int) -> List[int]:
        result = []
        for i in range(maximum + 1):
            result.append(table[maximum][i] * xs[i])
        return result

    table = create_derivative_table(xs)
    maximum = find_maximum(xs, table)
    return extract_derivative(xs, maximum)


