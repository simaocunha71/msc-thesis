def larg_nnum(lst, n):
    lst.sort(reverse=True)
    return lst[:n]

print(set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2)))

# Output: {100, 90}

# Alternatively, we can use the heapq module to achieve the same result:

import heapq

def largest_n(lst, n):
    return heapq.nlargest(n, lst)

print(set(largest_n([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100], 2)))

# Output: {100, 90}

# Both of these methods work by sorting the list in descending order and returning the first n elements.
# The heapq.nlargest function is more efficient for larger lists.
<jupyter_output>
{100, 90}
{100, 90}
<jupyter_text>
**Problem 2**
<jupyter_code>
