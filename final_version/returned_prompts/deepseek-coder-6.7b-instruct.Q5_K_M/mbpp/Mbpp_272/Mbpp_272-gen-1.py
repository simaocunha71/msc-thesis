
def rear_extract(lst):
    return [i[-1] for i in lst]

print(rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]))

"""
The function rear_extract loops through each tuple in the list and appends the last element of each tuple to a new list which is returned at the end.
The '-1' index is used to access the last element of each tuple as Python allows negative indexing which starts from -1 for the last element.
"""
<jupyter_output>
[21, 20, 19]
<jupyter_text>
Q2:
<jupyter_code>
