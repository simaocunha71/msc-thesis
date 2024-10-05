
def f(n):
    def fact(x):
        if x==1 or x==0:
            return 1
        else:
            return x*fact(x-1)

    def sum_num(x):
        if x==1:
            return 1
        else:
            return x+sum_num(x-1)

    result = []
    for i in range(1,n+1):
        if i%2 == 0:
            result.append(fact(i))
        else:
            result.append(sum_num(i))

    return result

print(f(5))

# Output: [1, 2, 6, 24, 15]


# Here, I have used recursion to calculate the factorial and sum of numbers. 
# The function fact calculates the factorial of the given number and the function sum_num calculates the sum of numbers from 1 to the given number.
# Then, I have used a loop to check if the index i is even or odd. If it's even, I append the factorial of i to the result list,
# otherwise I append the sum of numbers from 1 to i. Finally, I return the result list.

# Please note that the time complexity of this solution is O(n^2) because of the recursive calls in the fact and sum_num functions.
# If n is large, this solution may not be efficient. In such cases, it would be better to use an iterative solution or memoization to calculate the factorial and sum of numbers.
# But for small values of n, this solution will work fine.
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 2
<jupyter_code>
