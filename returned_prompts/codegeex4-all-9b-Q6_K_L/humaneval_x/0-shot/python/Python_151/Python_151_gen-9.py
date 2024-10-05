def double_the_difference(lst):
    return sum([i*i for i in lst if i>0 and i%2==1])

print(double_the_difference([1, 3, 2, 0]))
print(double_the_difference([-1, -2, 0]))
print(double_the_difference([9, -2]))
print(double_the_difference([0]))

print(double_the_difference([]))