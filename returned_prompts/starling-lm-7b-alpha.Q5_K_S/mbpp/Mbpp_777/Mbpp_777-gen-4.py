def find_sum(list):
    non_repeated_list = []
    for i in list:
        if list.count(i) == 1:
            non_repeated_list.append(i)
    return sum(non_repeated_list)


# assert find_sum([1,2,3,1,1,4,5,6]) == 21
# print(find_sum([1,2,3,1,1,4,5,6]))



# Time complexity: O(n)
# Auxiliary Space: O(n)
# Here we are using a list to store non_repeated_elements.

# We can optimize this to O(1) auxiliary space as follows:

def find_sum_optimized(list):
    sum = 0
    for i in list:
        if list.count(i) == 1:
            sum += i
    return sum

# assert find_sum_optimized([1,2,3,1,1,4,5,6]) == 21
# print(find_sum_optimized([1,2,3,1,1,4,5,6]))

# Time complexity: O(n)
# Auxiliary Space: O(1)



# Another approach to find the sum of non-repeated elements in a given list is as follows:

def find_sum_another(list):
    return sum(set(list))

# assert find_sum_another([1,2,3,1,1,4,5,6]) == 21
# print(find_sum_another([1,2,3,1,1,4,5,6]))

# Time complexity: O(n)
# Auxiliary Space: O(n)

"""
Here we are converting the list to set. Since a set only allows unique elements,
so it removes the repeated elements from the list. Then we find the sum of the set.
"""









































