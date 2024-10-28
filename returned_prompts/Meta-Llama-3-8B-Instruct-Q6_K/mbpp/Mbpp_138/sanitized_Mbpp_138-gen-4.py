def is_Sum_Of_Powers_Of_Two(n):
    powers_of_two = 0
    while powers_of_two < n:
        powers_of_two += 2 ** (powers_of_two.bit_length() - 1)
    return powers_of_two == n