def sum_to_n(n: int):
    if n < 1:
        return 0
    else:
        return n + sum_to_n(n - 1)
    # return sum(range(1, n + 1))  # Alternative solution using built-in sum function
    # return sum([i for i in range(1, n + 1)])  # Alternative solution using list comprehension
    # return sum(map(int, [str(i) for i in range(1, n + 1)]))  # Alternative solution using map function and str conversion

# Example usage:
print(sum_to_n(30))  # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))  # Output: 15
print(sum_to_n(10))  # Output: 55
print(sum_to_n(1))  # Output: 1

Note: The provided solution is recursive. If you want to use an iterative solution, you can use the built-in sum function or list comprehension as shown in the comments. The recursive solution has a time complexity of O(n) and a space complexity of O(n) due to the call stack. The iterative solutions have a time complexity of O(n) and a space complexity of O(1).