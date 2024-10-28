    if b == 0:
        return a
    else:
        return GreatestCommonDivisor(b, a % b)
}

# This function is recursive. It uses the Euclidean algorithm to find the GCD of two integers.
# The algorithm works by repeatedly replacing (a, b) with (b, a % b) until b is zero.
# At that point, a is the GCD.

# Example: GreatestCommonDivisor(3, 5) will call GreatestCommonDivisor(5, 3) and then GreatestCommonDivisor(3, 1)
# Then GreatestCommonDivisor(1, 0) is called, which returns 1, which is the GCD.

# Time complexity: O(log min(a, b)) because the algorithm reduces the problem size by a factor of at least 1 each time.
# Space complexity: O(log min(a, b)) because of the recursive call stack.

# Test cases:
print(GreatestCommonDivisor(3, 5)) # Output: 1
print(GreatestCommonDivisor(25, 15)) # Output: 5
print(GreatestCommonDivisor(10, 20)) # Output: 10
print(GreatestCommonDivisor(12, 15)) # Output: 3
print(GreatestCommonDivisor(48, 18)) # Output: 6
print(GreatestCommonDivisor(15, 30)) # Output: 15
print(GreatestCommonDivisor(0, 0)) # Output: 0
print(GreatestCommonDivisor(0, 5)) # Output: 5
print(GreatestCommonDivisor(5, 0)) # Output: 5
print(GreatestCommonDivisor(0, 10)) # Output: 10
print(GreatestCommonDivisor(10, 0)) # Output: 10
print(GreatestCommonDivisor(0, 20)) # Output: 20
print(GreatestCommonDivisor(20, 0)) # Output: 20
print(GreatestCommonDivisor(0, 30)) # Output: 30
print(GreatestCommonDivisor(30, 0)) # Output: 30
print(GreatestCommonDivisor(0, 40)) # Output: 40
print(GreatestCommonDivisor(40, 0)) # Output: 40
print(GreatestCommonDivisor(0