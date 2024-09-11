def div_list(list1,list2):
    list3=[]
    for i in range(len(list1)):
        list3.append(list1[i]/list2[i])
    return list3

# Test Case
assert div_list([4,5,6],[1, 2, 3])==[4.0,2.5,2.0]
print("Test Case Passed")

# User Input
list1 = list(map(int,input("Enter first list: ").strip().split()))
list2 = list(map(int,input("Enter second list: ").strip().split()))
if len(list1)==len(list2):
    print(div_list(list1,list2))
else:
    print("Lengths of the two lists should be equal")

"""
Enter first list: 4 5 6
Enter second list: 1 2 3
[4.0, 2.5, 2.0]
"""



"""
Enter first list: 4 5 6
Enter second list: 1 2 3 4
Lengths of the two lists should be equal
"""

# Output
# [4.0, 2.5, 2.0]
# """

# """
# Enter first list: 4 5 6
# Enter second list: 1 2 3 4
# Lengths of the two lists should be equal
# """

# Output
# Lengths of the two lists should be equal
# """

# Enter first list: 4 5 6
# Enter second list: 1 2 3 4
# Lengths of the two lists should be equal
# """

# Output
# Lengths of the two lists should be equal

# """
# Enter first list: 4 5 6
# Enter second list: 1 2 3
# [4.0, 2.5, 2.0]
# """

# Output
# [4.0, 2.5, 2.0]

"""
Enter first list: 4 5 6
Enter second list: 1 2 3