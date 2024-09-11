def add_pairwise(tuple):
    result = []
    for i in range(len(tuple)-1):
        result.append(tuple[i]+tuple[i+1])
    result.append(tuple[-1]+tuple[-2])
    return tuple(result)


# Python3 program to demonstrate
# pairwise addition of neighboring
# elements of the given list

# Function to find pairwise
# addition of neighboring
# elements of the given list
def addPairwise(lst):
    result = []
    for i in range(len(lst)-1):
        result.append(lst[i]+lst[i+1])
    result.append(lst[-1]+lst[-2])
    return result

# Driver Code
if __name__ == "__main__":
    print(add_pairwise((1, 5, 7, 8, 10)))
    print(addPairwise([1, 5, 7, 8, 10]))




"""
Explanation:
The function add_pairwise takes a tuple as an argument and returns a new tuple containing the pairwise addition of the neighboring elements of the given tuple. The function iterates through the tuple using a for loop, adding the current element and the next element together. The result is stored in a new list, which is then converted to a tuple using the tuple() function. The function returns this new tuple.
"""

"""
Explanation:
The function addPairwise takes a list as an argument and returns a new list containing the pairwise addition of the neighboring elements of the given list. The function iterates through the list using a for loop, adding the current element and the next element together. The result is stored in a new list, which is then returned by the function. The function also includes driver code to test the addPairwise function with a tuple and a list as inputs.
"""

"""
Explanation:
The add_pairwise function takes a tuple as an argument and returns a new tuple that contains the pairwise addition of the neighboring elements of the given tuple. The function initializes an empty list called result. Then, using a for loop, it iterates through the tuple from the first element to the second to last element. For each iteration, it adds