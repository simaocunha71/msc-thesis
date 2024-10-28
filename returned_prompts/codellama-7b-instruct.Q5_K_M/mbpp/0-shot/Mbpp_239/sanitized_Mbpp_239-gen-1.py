def get_total_number_of_sequences(m, n):
    return binomial_coefficient(n, 1) * (m - 1) ** (n - 1) + binomial_coefficient(n, 2) * (m - 1) ** (n - 2) + binomial_coefficient(n, 3) * (m - 1) ** (n - 3) + ... + binomial_coefficient(n, n) * (m - 1) ** 0
def binomial_coefficient(n, k):
    return (n - 1) ** (k - 1) * (n - 1 - k) ** (n - k) / (k - 1) ** (k - 1) / (n - 1) ** (k - 1)