def get_max_sum(n):
    # Initialize list to store computed f values
    f_values = [0]*(n+1)

    # Compute f values for 1 to n
    for i in range(1, n+1):
        f_values[i] = max(f_values[i//2] + f_values[i//3] + f_values[i//4] + f_values[i//5], i)

    # Return computed f value for n
    return f_values[n]