
def concatenate_tuple(tup):
    return "-".join(map(str, tup))

print(concatenate_tuple(("ID", "is", 4, "UTS")))

# OUTPUT:
# ID-is-4-UTS

"""
This solution works by using the `map` function to convert all the elements of the tuple to strings. 
Then it uses the `join` function to concatenate all the strings in the tuple with the '-' delimiter.
"""
<jupyter_output>
ID-is-4-UTS
<jupyter_text>
Question 3.14
<jupyter_code>
