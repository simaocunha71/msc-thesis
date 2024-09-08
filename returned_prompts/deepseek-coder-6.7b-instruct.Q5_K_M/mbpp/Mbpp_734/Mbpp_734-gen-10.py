def sum_Of_Subarray_Prod(l):
    n = len(l)
    sum_ = 0
    prod = 1
    for i in range(n):
        prod = 1
        for j in range(i, n):
            prod *= l[j]
            sum_ += prod
    return sum_

print(sum_Of_Subarray_Prod([1,2,3]))


# Time complexity: O(n^2)
# Space complexity: O(1)

# Explanation:
# For each element in the list, we find the product of sublists which include this element.
# We keep adding these products to our total sum.
# We repeat this process for every element in the list.
# This way, we get the sum of all possible sublists.

# Note: In the problem statement, the sublists are inclusive of the element at the end of the list,
# so we start the inner loop at i rather than i+1.
<jupyter_output>
20
<jupyter_text>
Problem 3
<jupyter_code>
