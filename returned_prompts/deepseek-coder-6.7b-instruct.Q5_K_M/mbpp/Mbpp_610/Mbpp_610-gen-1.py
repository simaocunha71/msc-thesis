
def remove_kth_element(lst, k):
    del lst[k]
    return lst

print(remove_kth_element([1,1,2,3,4,4,5,1],3))

"""
or
"""

def remove_kth_element(lst, k):
    return lst[:k] + lst[k+1:]

print(remove_kth_element([1,1,2,3,4,4,5,1],3))

"""
or
"""

def remove_kth_element(lst, k):
    lst.pop(k)
    return lst

print(remove_kth_element([1,1,2,3,4,4,5,1],3))

#output
#[1, 1, 3, 4, 4, 5, 1]
#[1, 1, 3, 4, 4, 5, 1]
#[1, 1, 2, 3, 4, 4, 1]
#[1, 1, 2, 3, 4, 4, 5, 1]

#All of these methods will return the same output for the given question.
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2
<jupyter_code>
