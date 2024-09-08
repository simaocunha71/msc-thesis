def odd_length_sum(arr):
    n = len(arr)
    res = 0

    for i in range(n):
        res += ((i+1)*(n-i)+1)//2*arr[i]

    return res

print(odd_length_sum([1,2,4]))

# This code calculates the sum of all subarrays of odd length of the given array.
# For each element at index 'i' in the array, the code calculates the number of subarrays that can be formed starting from index 'i' 
# and adds the sum of those subarrays to the result. The sum of subarrays can be calculated using the formula ((i+1)*(n-i)+1)//2.
# Finally, the function returns the sum of all subarrays of odd length.
<jupyter_output>
<empty_output>
<jupyter_text>
Question 3:
<jupyter_code>
