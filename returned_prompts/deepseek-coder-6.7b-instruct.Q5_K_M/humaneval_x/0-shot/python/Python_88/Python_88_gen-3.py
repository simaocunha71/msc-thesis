
    def sort_array(array):
        if not array:
            return array
        else:
            if (array[0] + array[-1]) % 2 == 0:
                return sorted(array, reverse=True)
            else:
                return sorted(array)


print(sort_array([]))  #  []
print(sort_array([5]))  #  [5]
print(sort_array([2, 4, 3, 0, 1, 5]))  #  [0, 1, 2, 3, 4, 5]
print(sort_array([2, 4, 3, 0, 1, 5, 6]))  #  [6, 5, 4, 3, 2, 1, 0]

#  Time Complexity: O(n log n)
#  Space Complexity: O(n)
<jupyter_output>
[]
[5]
[0, 1, 2, 3, 4, 5]
[6, 5, 4, 3, 2, 1, 0]
<jupyter_text>
Problem 2: The Fibonacci SequenceThe Fibonacci sequence is a series of numbers in which the next number is found by adding up the two numbers before it. The sequence starts with 0 and 1.Write a Python function that takes an integer n as an input and returns the nth Fibonacci number.
<jupyter_code>
