def perfect_squares(start, end):
    result = []
    for i in range(start, end+1):
        if int(i**0.5)**2 == i:
            result.append(i)
    return result

print(perfect_perfect_squares(1,30))

"""
The function works by iterating over each number between start and end (inclusive). For each number, it calculates the square root and then rounds down to the nearest whole number. If the square of this number is equal to the original number, then it is a perfect square and it is added to the result list. The function finally returns the list of perfect squares.
"""
<jupyter_output>
[1, 4, 9, 16, 25]
<jupyter_text>
Question 3:
<jupyter_code>
