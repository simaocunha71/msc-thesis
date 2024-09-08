def find_sum(lst):
    return sum(set(lst))

print(find_sum([1,2,3,1,1,4,5,6]))

# Output: 21
<jupyter_output>
21
<jupyter_text>
Explanation:In the function, I used a set to remove any repeated elements in the list. Then I used the built-in sum() function to add up all the non-repeated numbers in the list.
<jupyter_code>
