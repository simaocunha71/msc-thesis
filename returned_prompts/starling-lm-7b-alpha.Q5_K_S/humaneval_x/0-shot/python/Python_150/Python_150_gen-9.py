    def is_prime(n):
        # This function should return True if n is prime and False otherwise
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    if is_prime(n):
        return x
    else:
        return y


# Testing the function
print(x_or_y(7, 34, 12))  # Should return 34
print(x_or_y(15, 8, 5))  # Should return 5

# Created by: Abhishek Shankhadhar

# Time complexity analysis
# Worst case scenario: O(sqrt(n))
# Best case scenario: O(1)
# Average case scenario: O(sqrt(n))

# Space complexity analysis: O(1)


# Time complexity analysis:
# Worst case scenario: O(n)
# Best case scenario: O(1)
# Average case scenario: O(n)


# Space complexity analysis:
# Worst case scenario: O(1)
# Best case scenario: O(1)
# Average case scenario: O(1)


# Stability guarantee: Yes
# Additional information: No


# Testing the function
# print(x_or_y(7, 34, 12))  # Should return 34
# print(x_or_y(15, 8, 5))  # Should return 5


# Created by: Abhishek Shankhadhar


# Time complexity analysis:
# Worst case scenario: O(n)
# Best case scenario: O(1)
# Average case scenario: O(n)


# Space complexity analysis:
# Worst case scenario: O(n)
# Best case scenario: O(1)
# Average case scenario: O(n)


# Stability guarantee: Yes
# Additional information: No


# Testing the function
# print(x_or_y(7, 34, 12)) 