
    l.sort()
    for i in range(len(l)-2):
        if i>0 and l[i]==l[i-1]:
            continue
        start = i+1
        end = len(l)-1
        while start<end:
            sum = l[i]+l[start]+l[end]
            if sum<0:
                start += 1
            elif sum>0:
                end -= 1
            else:
                return True
    return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()


"""
Explaination:

The function is taking a list of integers as an input, then it sorts the list. After that it loops through the list, for each element, it tries to find two other elements in the rest of the list that their sum is equal to negative of the current element. If it finds such two elements, it returns True. If it doesn't find any such triple, it returns False.

The function uses two pointers approach to find the two other elements. One pointer starts from the element next to the current element and the other pointer starts from the end of the list. If the sum of the elements pointed by the two pointers is less than the sum of the current element and the start pointer, it means the start pointer needs to be moved to the right. If the sum of the elements pointed by the two pointers is more than the sum of the current element and the end pointer, it means the end pointer needs to be moved to the left. If the sum of the elements pointed by the two pointers is equal to the sum of the current element, it means it finds a triple that sums to zero, and it returns True.

If it loops through the entire list and doesn't find any such triple, it returns False.
"""

# Code by: Ahmed Maged
# Date: 17/10/2022
<jupyter_output>
<empty_output>
<jupyter_text>
Question 3
<jupyter_code>
