
def double_the_difference(lst):
    return sum(x**2 for x in lst if x > 0 and x % 2 == 1)


print(double_the_difference([1, 3, 2, 0]))
print(double_the_difference([-1, -2, 0]))
print(double_the_difference([9, -2]))
print(double_the_difference([0]))
print(double_the_difference([]))
<jupyter_output>
10
0
81
0
0
<jupyter_text>
