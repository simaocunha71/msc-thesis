"""
def even_position(lst):
    lst = lst[::2]
    if len(set(lst)) == 1:
        return True
    else:
        return False
"""

def even_position(lst):
    if lst[0] % 2 != 0:
        return False
    for i in range(1,len(lst),2):
        if lst[i] % 2 == 0:
            return False
    return True


print(even_position([3,2,1]))
print(even_position([2,4,3,1]))
print(even_position([2,4,3,2]))
print(even_position([3,2,3,1]))
print(even_position([3,2,3,2]))
print(even_position([3,2,3,0]))

```
