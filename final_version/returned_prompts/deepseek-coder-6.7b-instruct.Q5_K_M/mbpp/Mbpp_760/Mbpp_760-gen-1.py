
def unique_Element(lst):
    return len(set(lst)) == 1

print(unique_Element([1,1,1]))  #True
print(unique_Element([1,2,3]))  #False


"""
Explanation:

In the above function, we are converting the list into a set. A set in python is a collection of unique elements. 
So, if the list contains only one distinct element, the length of the set will be 1.
"""
<jupyter_output>
True
False
<jupyter_text>
Q2:
<jupyter_code>
