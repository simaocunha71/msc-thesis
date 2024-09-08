def odd_length_sum(arr):
    n = len(arr)
    ans = 0
    for i in range(n):
        ans += ((i+1)*(n-i)+1)//2 * arr[i]
    return ans

print(odd_length_sum([1,2,4]))

"""
The function works by iterating through each element in the array, and then finding the number of subarrays that include that element. This number is given by ((i+1)*(n-i)+1)//2, where i is the index of the current element.

Then it multiplies the number of subarrays by the value of the current element, and adds this to the total sum. 

Finally, it returns the total sum.
"""
<jupyter_output>
14
<jupyter_text>
Problem 4
<jupyter_code>
