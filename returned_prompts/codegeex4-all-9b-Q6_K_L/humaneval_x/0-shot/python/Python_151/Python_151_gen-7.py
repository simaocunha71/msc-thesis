def double_the_difference(lst):
    return sum([abs(x)**2 for x in lst if x%2!=0 and x>=0 and isinstance(x,int)])

print(double_the_difference([1, 3, 2, 0]))
print(double_the_difference([-1, -2, 0]))
print(double_the_difference([9, -2]))
print(double_the_difference([0]))