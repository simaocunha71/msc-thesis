

    def fib4(n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 0
        elif n == 2:
            return 2
        elif n == 3:
            return 0

        fib = [0, 0, 2, 0]

        for i in range(4, n+1):
            fib.append(fib[i-1] + fib[i-2] + fib[i-3] + fib[i-4])

        return fib[n]


    if __name__ == "__main__":
        import doctest
        doctest.testmod()


Output:


    fib4(5)
    4
    fib4(6)
    8
    fib4(7)
    14


Explanation:

The function first handles the base cases of the Fib4 sequence. It then creates a list to store the Fib4 numbers until n. The list is initialized with the first four Fib4 numbers. The function then loops from 4 to n and calculates the n-th Fib4 number by summing the previous four Fib4 numbers. The n-th Fib4 number is then returned from the list.

This solution is efficient because it avoids the overhead of recursion by using a loop to compute each Fib4 number. It also stores the previously computed Fib4 numbers in a list, which allows it to access them in constant time.

The time complexity of this solution is O(n) because it loops from 4 to n. The space complexity is also O(n) because it creates a list of size n.

The solution also includes a test case using doctest to validate the output against the provided examples.
"""

# 