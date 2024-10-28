

def sum_to_n(n: int):
    if n <= 0:
        return 0
    else:
        return n + sum_to_n(n - 1)


print(sum_to_n(30))
print(sum_to_n(100))
print(sum_to_n(5))
print(sum_to_n(10))
print(sum_to_n(1))

# Output:
# 465
# 5050
# 15
# 55
# 1


# Note: This solution uses the concept of recursion. Recursion is when a function calls itself. In the case of the sum_to_n function, the function is calling itself with the argument decreased by 1 in each recursive call until it reaches 0. At that point, the function returns 0 and the recursion stops.
<jupyter_output>
465
5050
15
55
1
<jupyter_text>
