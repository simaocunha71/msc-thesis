"""
def big_sum(array):
    array.sort()
    return array[0] + array[-1]
"""

def big_sum(array):
    array.sort()
    return array[0] + array[-1]


if __name__ == "__main__":
    print(big_sum([1,2,3]))


"""
In the above code, we define the function big_sum which takes an array as an argument. We sort the array in ascending order using the sort() method. Then, we return the sum of the first element (array[0]) and the last element (array[-1]) of the sorted array. This is because the first element will be the smallest value and the last element will be the largest value in the array.

To test the function, we call big_sum with the array [1, 2, 3] and print the result, which should be 4.
"""



# Python Program to Find Sum of Largest and Smallest Value in an Array
# The above program can be used to find the sum of the largest and smallest value in an array. It first sorts the array in ascending order using the sort() method. Then, it returns the sum of the first element (array[0]) and the last element (array[-1]) of the sorted array. This is because the first element will be the smallest value and the last element will be the largest value in the array.


# Python3 Program to Find Sum of Largest and Smallest Value in an Array
# Here is a Python3 program to find the sum of the largest and smallest value in an array:

def big_sum(array):
    array.sort()
    return array[0] + array[-1]

if __name__ == "__main__":
    print(big_sum([1,2,3]))

# In this program, the function big_sum takes an array as an argument. It sorts the array in ascending order using the sort() method. Then, it returns the sum of the first element (array[0]) and the last element (array[-1]) of the sorted array. This is because the first element will be the smallest value and the last element will be the largest value in the array.

# To test the function, we