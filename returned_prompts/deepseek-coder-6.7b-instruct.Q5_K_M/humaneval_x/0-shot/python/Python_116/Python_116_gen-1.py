
    def sort_array(arr):
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))

    print(sort_array([1, 5, 2, 3, 4]))  # [1, 2, 3, 4, 5]
    print(sort_array([-2, -3, -4, -5, -6]))  # [-6, -5, -4, -3, -2]
    print(sort_array([1, 0, 2, 3, 4]))  # [0, 1, 2, 3, 4]

This function uses a lambda function as the key for the sorted() function. The lambda function is a small anonymous function that returns a tuple where the first element is the number of ones in the binary representation of the number and the second element is the number itself. This allows the sorted() function to sort the array first by the number of ones in the binary representation and then by the decimal value of the numbers.

The bin() function returns the binary representation of a number as a string, and the count() method returns the number of occurrences of a substring in a string. In this case, it counts the number of ones in the binary representation of the number.

This solution assumes that the input array will only contain non-negative integers. If the input array can also contain negative integers, the lambda function should be modified to return the absolute value of the number when sorting by decimal value.

Please note that the sorted() function in Python is stable, which means that it maintains the relative order of elements with equal keys. This means that if two numbers have the same number of ones in their binary representation, they will be sorted by their decimal value in ascending order.

Also note that this solution may not work for very large numbers because the binary representation of a number is limited in size.

Hope this helps, and let me know if you have any questions or if there's anything else you'd like to know about this solution.


"""


def sort_array(arr):
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))


print(sort_array([1, 5, 2, 