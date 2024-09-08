def perfect_squares(start, end):
    return [i * i for i in range(int(start ** 0.5), int(end ** 0.5) + 1)]

print(perfect_squares(1, 30))

# This program uses list comprehension to generate a list of perfect squares in the given range. The range is calculated by taking the square root of the start and end numbers and rounding them down, and then rounding them up. The squares of numbers in this range are calculated by squaring the numbers and added to the list.
<jupyter_output>
[1, 4, 9, 16, 25]
<jupyter_text>
Question 3:
<jupyter_code>
