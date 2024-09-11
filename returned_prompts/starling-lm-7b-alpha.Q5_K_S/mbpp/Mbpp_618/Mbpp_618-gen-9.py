def div_list(list1,list2):
    return [list1[i]/list2[i] for i in range(len(list1))]


# Test the function
assert div_list([4,5,6],[1, 2, 3])==[4.0,2.5,2.0]

# Test the function with different inputs
assert div_list([1,2,3],[3,2,1])==[0.3333333333333333, 1.0, 3.0]
assert div_list([1,2,3,4,5,6,7,8,9,10],[10,9,8,7,6,5,4,3,2,1])==[1.0, 0.2222222222222222, 0.375, 1.1666666666666666, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

# Test the function with edge cases
assert div_list([1],[1])==[1.0]
assert div_list([1,2,3],[3,2,1])==[0.3333333333333333, 1.0, 3.0]
assert div_list([1,2,3,4,5],[3,2,1])==[0.3333333333333333, 1.0, 3.0, 1.3333333333333333, 1.6666666666666667]

# Test the function with invalid inputs
try:
    div_list([1,2,3],'abc')
except TypeError:
    print("Passed the TypeError test")

try:
    div_list({1,2,3},[1,2,3])
except TypeError:
   