
    def add_elements(arr, k):
        total = 0
        for i in range(k):
            if arr[i] < 10 or arr[i] >= 100:
                total += arr[i]
        return total

    arr = [111,21,3,4000,5,6,7,8,9]
    k = 4
    print(add_elements(arr, k))

"""
Explanation:

In the given array, the first 4 elements are [111, 21, 3, 4000] which are [1 digit, 2 digits, 1 digit, 4 digits] respectively. 

According to the problem statement, we are only considering elements with at most 2 digits. Hence, 21 and 3 are the only 2 digit numbers in the first 4 elements of the array, so their sum is 24.
"""
<jupyter_output>
24
<jupyter_text>
Problem 2:
<jupyter_code>
"""
