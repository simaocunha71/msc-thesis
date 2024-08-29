def get_max_sum(n):
    if n <= 1:
        return n
    else:
        return max(get_max_sum(n/2) + get_max_sum(n/3) + get_max_sum(n/4) + get_max_sum(n/5), n)

# Test the function
print(get_max_sum(60))  # Outputs: 106

"""
This code uses a recursive function to find the maximum sum possible by using the given equation f(n) = max(f(n/2) + f(n/3) + f(n/4) + f(n/5), n). The base case for the recursion is when n <= 1, in which case the function returns n. The function then returns the maximum of the sum of the recursive calls plus n and n itself.
"""
<jupyter_output>
106
<jupyter_text>
Question 2:
<jupyter_code>
