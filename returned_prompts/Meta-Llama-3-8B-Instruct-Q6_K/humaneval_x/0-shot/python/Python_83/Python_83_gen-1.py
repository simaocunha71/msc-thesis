    def starts_one_ends(n):
        if n < 1:
            return 0
        count = 0
        for i in range(10**(n-1), 10**n):
            if i % 10 == 1 or i//10**n % 10 == 1:
                count += 1
        return count
    print(starts_one_ends(2))  # Expected output: 9
    print(starts_one_ends(3))  # Expected output: 90
    print(starts_one_ends(4))  # Expected output: 900
    print(starts_one_ends(5))  # Expected output: 9000
    print(starts_one_ends(6))  # Expected output: 90000

# Test cases
print(starts_one_ends(2))  # Expected output: 9
print(starts_one_ends(3))  # Expected output: 90
print(starts_one_ends(4))  # Expected output: 900
print(starts_one_ends(5))  # Expected output: 9000
print(starts_one_ends(6))  # Expected output: 90000

# Explanation:
# We iterate over all n-digit numbers and check if they start or end with 1.
# If they do, we increment the count. Finally, we return the count.

# Time complexity: O(10^n)
# Space complexity: O(1)
# The time complexity is O(10^n) because we are iterating over all n-digit numbers.
# The space complexity is O(1) because we are using a constant amount of space to store the count.  # noqa: E501

