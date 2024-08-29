
def sum_Of_Subarray_Prod(arr):
    n = len(arr)
    prod = [0]*n
    sum_total = 0
    for i in range(n):
        for j in range(i, n):
            if i == j:
                prod[i] = arr[i]
            else:
                prod[j] = prod[j-1]*arr[j]
            sum_total += prod[j]
    return sum_total


print(sum_Of_Subarray_Prod([1,2,3]))

Explanation:
The function works by first creating an empty list prod with the same length as the input list arr. 
The function then loops through each element in arr, and for each element, it calculates the product of all elements from the current element to the end of the list, storing these products in the list prod.
After that, it sums up all the elements in the list prod and returns the sum.

The time complexity of this function is O(n^2) because it has a nested loop structure that iterates through each element in arr.
The space complexity of this function is O(n) because it creates a list prod with the same length as arr.
"""

def sum_Of_Subarray_Prod(arr):
    n = len(arr)
    prod = [0]*n
    sum_total = 0
    for i in range(n):
        prod[i] = arr[i]*(i+1)
        sum_total += prod[i]
    return sum_total

print(sum_Of_Subarray_Prod([1,2,3]))

Explanation:
This function works similarly to the previous function, but it calculates the product of each element and the number of elements that come before it in the list, rather than the product of all elements from the current element to the end of the list.
This means that the function calculates the product of each element and its position in the list, rather than the product of all elements from the current element to the end of the list.
The sum of these products is then returned.

The time complexity of this function is O(n) because it has a single loop structure that iterates through each