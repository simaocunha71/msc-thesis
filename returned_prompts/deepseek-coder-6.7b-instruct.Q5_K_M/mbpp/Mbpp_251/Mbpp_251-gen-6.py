
def insert_element(lst,element):
    return [element]*(len(lst)*2-1)+lst

print(insert_element(['Red',  'Green',  'Black'],'c'))

#Output: ['c', 'Red', 'c', 'Green', 'c', 'Black']

"""
Explanation:
The function `insert_element` takes a list and an element as input. 
We create a list of the element repeated twice minus one times the length of the list. 
This would result in the element repeated in between each element of the original list.
Finally, we concatenate the newly created list with the original list.
"""
<jupyter_output>
['c', 'Red', 'c', 'Green', 'c', 'Black']
<jupyter_text>
Problem 6
<jupyter_code>
