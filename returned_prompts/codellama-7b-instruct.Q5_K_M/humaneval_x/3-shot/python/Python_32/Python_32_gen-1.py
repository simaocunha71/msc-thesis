    # find max abs coefficient
    max_coeff = max(abs(x) for x in xs)

    # find max abs x
    max_abs_x = max(abs(x) for x in xs[:-1])

    # find max abs x^n
    max_abs_x_power_n = max(abs(x) for x in xs[:-2])

    # find max abs x^n * (x - 1) * (x - 2) * ... * (x - n)
    max_abs_x_power_n_prod = max(
        abs(x * y) for x in xs[:-1] for y in xs[:-2]
    )

    x_max = max(max_abs_x, max_abs_x_power_n, max_abs_x_power_n_prod)

    if max_coeff > x_max:
        x_max = max_coeff

    # binary search
    low = 0
    high = x_max
    while low < high:
        mid = (low + high) // 2
        if poly(xs, mid) > 0:
            high = mid
        else:
            low = mid + 1

    return low


