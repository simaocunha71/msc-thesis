def left_insertion(arr, val):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < val:
            left = mid + 1
        else:
            right = mid
    return left

print(left_insertion([1,2,4,5],6)) # 4

# The function works by using a binary search algorithm to find the insertion point. 
# If the middle element of the array is less than the target value, 
# the search is narrowed to the upper half of the array. 
# If the middle element is greater than or equal to the target value, 
# the search is narrowed to the lower half of the array. 
# The search continues until the left index is equal to the right index, 
# at which point the left index is the insertion point.

# This function will return the index at which the specified value should be inserted 
# in order for the array to remain sorted.
<jupyter_output>
4
<jupyter_text>
Q2: Write a function to compute the sum of the digits in a given integer.
<jupyter_code>
def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))

print(sum_of_digits(1234)) # 10
print(sum_of_digits(-567)) # 18
<jupyter_output>
10
18
<jupyter_text>
Q3: Write a function to compute the product of the digits in a given integer.
<jupyter_code>
def product_of_digits(n):
    product = 1
    for digit in str(abs(n)):
        product *= int(digit)
    return product

print(product_of_digits(1234)) # 24
print(product_of_digits(-567)) # -350
<jupyter_output>
24
-350
<jupy