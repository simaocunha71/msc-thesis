def all_unique(lst):
    return len(lst) == len(set(lst))
"""
In this function, we are converting the list to a set, which automatically removes duplicate elements. 
If the lengths of the list and the set are equal, that means all elements in the list were unique. 
If not, that means there were duplicate elements in the list.
"""

# Test the function
print(all_unique([1,2,3])) # Should return True
print(all_unique([1,2,2])) # Should return False

#end

# Python program to check if all elements in a list are unique

def unique(lst):
    num_set = set(lst)
    if len(num_list) == len(num_set):
        return True
    return False

num_list = [1,2,3]
print(unique(num_list))

num_list = [1,2,2]
print(unique(num_list))
<jupyter_output>
<empty_output>
<jupyter_text>
The above Python code will return True if all elements in the list are unique and False if there are any duplicates.
<jupyter_code>
#end
<jupyter_output>
<empty_output>
<jupyter_text>
