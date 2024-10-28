    def largest_divisor(n: int) -> int:
        """ For a given number n, find the largest number that divides n evenly, smaller than n """
        if n < 2:
            return 1
        for i in range(n-1, 0, -1):
            if n % i == 0:
                return i
        return 1
    # Test the function
    print(largest_divisor(15))  # Output: 5
    print(largest_divisor(12))  # Output: 6
    print(largest_divisor(17))  # Output: 1

Explanation:

*   The function `largest_divisor(n)` takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`.
*   The function starts by checking if `n` is less than 2. If it is, the function returns 1, as the only number that divides 0 or 1 is 1 itself.
*   If `n` is 2 or greater, the function iterates from `n-1` down to 1, checking each number to see if it divides `n` evenly (i.e., `n % i == 0`). The first number it finds that divides `n` evenly is the largest number that divides `n` evenly, smaller than `n`, so it returns that number.
*   If no number divides `n` evenly, the function returns 1, as the only number that divides `n` is `n` itself.
*   The function is tested with the inputs 15, 12, and 17, and the expected outputs are 5, 6, and 1, respectively. These outputs are printed using the `print` function.