def square_Sum(n):
    sum = 0
    num = 1
    for i in range(n):
        sum += num*num
        num += 2
    return sum

print(square_Sum(2))


# This code works by initializing a variable sum to 0 which will store the sum of squares. It also initializes a variable num to 1, which will be the current odd number. The for loop runs n times, each time adding the square of num to sum and incrementing num by 2 to get the next odd number. Finally, it returns the sum.

# In the provided example, the function square_Sum(2) is called, and it returns the sum of the squares of the first 2 odd natural numbers: 1*1 + 3*3 = 1 + 9 = 10.
<jupyter_output>
10
<jupyter_text>
Question 2
<jupyter_code>
