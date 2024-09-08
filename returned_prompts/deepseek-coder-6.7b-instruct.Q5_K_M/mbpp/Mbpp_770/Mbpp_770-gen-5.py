def odd_num_sum(n):
    sum = 0
    for i in range(2*n):
        if i % 2 != 0:
            sum += i**4
    return sum

print(odd_num_sum(2))
assert odd_num_sum(2) == 82

# Explanation:
# The function odd_num_sum takes one argument n.
# It initializes a variable sum to 0.
# It then loops over the first 2n numbers.
# If a number is odd (i.e., its remainder when divided by 2 is not 0), it takes that number to the power of 4 and adds it to sum.
# Finally, it returns the sum.
# The assertion checks that the function is working correctly by providing an example input.
# If the function returns the correct result for that input, the assertion is True and the program continues to run.
# If the function returns a different result, the assertion is False and the program raises an AssertionError.
<jupyter_output>
82
<jupyter_text>
Question 2
<jupyter_code>
