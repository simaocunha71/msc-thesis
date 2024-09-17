def get_total_number_of_sequences(m, n):
    return int(binomial_coefficient(n, 2) * (m ** n - (m ** 2) ** n) / (n * (m - 1) ** n))
def binomial_coefficient(n, r):
    if r == 0 or r == n:
        return 1
    return binomial_coefficient(n - 1, r - 1) + binomial_coefficient(n - 1, r)