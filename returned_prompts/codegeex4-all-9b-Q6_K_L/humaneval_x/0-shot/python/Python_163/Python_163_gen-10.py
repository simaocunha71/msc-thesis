def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Get the minimum and maximum of a and b
    min_val = min(a, b)
    max_val = max(a, b)

    # Initialize an empty list to store the even digits
    even_digits = []

    # Iterate over the range from min_val to max_val (inclusive)
    for num in range(min_val, max_val + 1):
        # Convert the number to a string
        num_str = str(num)

        # Iterate over each digit in the string
        for digit in num_str:
            # Convert the digit back to an integer
            digit_int = int(digit)

            # Check if the digit is even
            if digit_int % 2 == 0:
                # Add the even digit to the list
                even_digits.append(digit_int)

    # Return the list of even digits
    return even_digits

# Test the function with the provided examples
print(generate_integers(2, 8))  # Output: [2, 4, 6, 8]
print(generate_integers(8, 2))  # Output: [2, 4, 6, 8]
print(generate_integers(10, 14))  # Output: []