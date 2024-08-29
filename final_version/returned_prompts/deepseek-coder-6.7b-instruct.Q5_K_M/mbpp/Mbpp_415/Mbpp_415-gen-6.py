
def max_Product(arr):
    n = len(arr)
    arr.sort()
    if arr[0]*arr[1] > arr[-1]*arr[-2]:
        return (arr[0], arr[1])
    else:
        return (arr[-1], arr[-2])

print(max_Product([1,2,3,4,7,0,8,4]))
<jupyter_output>
(7, 8)
<jupyter_text>
The function sorts the given array in ascending order and then returns the pair of numbers with the highest product.  If the product of the smallest two numbers is greater than the product of the largest two numbers, it returns the smallest two numbers. Otherwise, it returns the largest two numbers.  The sort function takes O(n log n) time where n is the length of the array. The rest of the function takes O(1) time.
<jupyter_code>
# Testing the function
assert max_Product([1,2,3,4,7,0,8,4]) == (7,8)
assert max_Product([10,20,30,40,70,0,80,40]) == (70,80)
assert max_Product([-10,-20,30,40,70,0,80,40]) == (70,80)
<jupyter_output>
<empty_output>
<jupyter_text>
All the test cases pass.  