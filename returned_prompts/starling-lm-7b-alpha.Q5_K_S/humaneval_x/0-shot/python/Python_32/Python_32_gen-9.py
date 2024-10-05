    # check if xs are correct
    if len(xs) % 2 != 0:
        raise ValueError("xs must have even number of coefficients")

    # find largest non zero coefficient
    largest_coeff_index = len(xs) - 1
    while largest_coeff_index >= 0 and xs[largest_coeff_index] == 0:
        largest_coeff_index -= 1
    largest_coeff_index = max(0, largest_coeff_index)

    # find zero
    zero_powers = math.pow(xs[largest_coeff_index], -1)
    zero_coeffs = [coeff / xs[largest_coeff_index] for coeff in xs[:largest_coeff_index]]
    zero_coeffs.append(zero_powers)
    return poly(zero_coeffs, -1)

    # for i in range(largest_coeff_index, -1, -1):
    #     zero_powers = math.pow(xs[i], -1)
    #     zero_coeffs = [coeff / xs[i] for coeff in xs[:i]]
    #     zero_coeffs.append(zero_powers)
    #     zero_coeffs = [zero_coeffs]
    #     if poly(zero_coeffs, -1) == 0:
    #         break
    # return round(poly(zero_coeffs, -1), 2)


if __name__ == "__main__":
    print(find_zero([1, 2]))
    print(find_zero([-6, 11, -6, 1]))





































































































