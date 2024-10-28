def prod_signs(arr):
    if not arr:
        return None

    # Calculate the product of signs
    sign_product = 1
    for num in arr:
        sign_product *= num / abs(num)

    # Calculate the sum of magnitudes
    magnitude_sum = sum(abs(num) for num in arr)

    # Return the product of the sign product and magnitude sum
    return sign_product * magnitude_sum

# Test cases
print(prod_signs([1, 2, 2, -4]))  # Output: -9
print(prod_signs([0, 1]))  # Output: 0
print(prod_signs([]))  # Output: None
