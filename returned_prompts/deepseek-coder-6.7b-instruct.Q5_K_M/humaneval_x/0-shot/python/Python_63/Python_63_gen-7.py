

def fibfib(n: int):
    fib_sequence = [0, 0, 1]
    while len(fib_sequence) < n + 1:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2] + fib_sequence[-3])
    return fib_sequence[n]


# Test cases
print(fibfib(1))  # 0
print(fibfib(5))  # 4
print(fibfib(8))  # 24


# Explaination:
# The function fibfib(n) is created to calculate the n-th element in the fibfib number sequence. The fibfib number sequence is defined as follows:
# fibfib(0) = 0, fibfib(1) = 0, fibfib(2) = 1
# fibfib(n) = fibfib(n-1) + fibfib(n-2) + fibfib(n-3) for n > 2
# The function uses a dynamic programming approach to solve the problem. It starts with the first three elements of the sequence and then continuously adds new elements to the sequence until it reaches the n-th element. This approach ensures that the time complexity of the function is O(n), which is efficient for large n.
# The function returns the n-th element of the fibfib number sequence.

# The test cases verify that the function is working correctly by comparing the output of the function with the expected output.

# The function prints:
# 0
# 4
# 24
# which are the first, fifth and eighth elements of the fibfib number sequence respectively.

# The function is working as expected.


# Note: This solution uses a list to store the fibfib numbers. If n is large, this might not be the most memory-efficient solution. In such cases, you may want to consider using a generator or an iterative approach.
<jupyter_output>
<empty_output>
<jupyter_text>
Exercise 2: Write a Python function that takes as input a list of integers and returns a new list containing only the prime numbers from the input list. A prime number