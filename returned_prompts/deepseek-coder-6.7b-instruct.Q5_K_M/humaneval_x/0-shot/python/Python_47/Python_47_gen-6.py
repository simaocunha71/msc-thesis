

    l.sort()
    len_l = len(l)
    if len_l % 2 == 0:
        return (l[len_l // 2 - 1] + l[len_l // 2]) / 2
    else:
        return l[len_l // 2]


if __name__ == "__main__":
    import doctest
    doctest.testmod()

#Testing
print(median([3, 1, 2, 4, 5])) # Output: 3
print(median([-10, 4, 6, 1000, 10, 20])) # Output: 15.0

"""
The function first sorts the list in ascending order. Then it checks if the length of the list is even or odd. If it's even, it returns the average of the two middle elements; if it's odd, it returns the middle element. 

The complexity of the function is O(n log n) due to the sort operation.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Exercise 2: Fibonacci SequenceIn mathematics, the Fibonacci sequence is a sequence of integers, where the first two integers are 0 and 1, and each subsequent integer is the sum of the previous two.Write a Python function that takes a positive integer n as input and returns the nth Fibonacci number.In mathematical terms, the sequence is:0, 1, 1, 2, 3, 5, 8, 13, 21, 34, and so on.
<jupyter_code>
