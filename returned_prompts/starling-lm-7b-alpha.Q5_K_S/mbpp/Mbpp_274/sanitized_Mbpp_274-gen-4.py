def even_binomial_Coeff_Sum(n):
    assert n>0, "Input should be a positive integer"
    coeff_list = [1]
    for i in range(n):
        coeff_list.append(coeff_list[i] * (n - i) / (i + 1))
    return sum([coeff_list[i] for i in range(0, n, 2)])