
    return sum(lst[i] for i in range(1, len(lst), 2) if lst[i] % 2 == 0)


# Test cases
print(add([4, 2, 6, 7]))  # Expected output: 2
print(add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # Expected output: 20
print(add([2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))  # Expected output: 28
print(add([11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))  # Expected output: 160
print(add([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))  # Expected output: 40

# Note: The sum of the even numbers at odd indices in the list [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] is 40.
<jupyter_output>
2
20
28
160
40
<jupyter_text>
Q2:
<jupyter_code>
