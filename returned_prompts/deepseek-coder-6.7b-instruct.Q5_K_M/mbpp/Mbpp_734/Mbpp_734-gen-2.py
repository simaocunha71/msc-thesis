def sum_Of_Subarray_Prod(lst):
    n = len(lst)
    prod = [0]*n
    sum_prod = 0

    # Compute product of all subarrays and sum them up
    for i in range(n):
        prod[i] = lst[i] * (i+1) * (n-i)
        sum_prod += prod[i]

    return sum_prod

print(sum_Of_Subarray_Prod([1,2,3]))
assert sum_Of_Subarray_Prod([1,2,3]) == 20
<jupyter_output>
20
<jupyter_text>
Question 5
<jupyter_code>
