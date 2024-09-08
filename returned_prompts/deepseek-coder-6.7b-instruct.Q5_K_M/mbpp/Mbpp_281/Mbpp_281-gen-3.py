def all_unique(lst):
    return len(lst) == len(set(lst))

print(all_unique([1,2,3])) #== True
"""
The function all_unique takes a list as input. It converts the list to a set, which automatically removes any duplicate elements because sets only allow unique elements. If the length of the original list and the set are the same, it means that all elements in the list were unique, so the function returns True. Otherwise, it returns False.
"""

# or without using set
def all_unique(lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] == lst[j]:
                return False
    return True

print(all_unique([1,2,3])) #== True
"""
This function all_unique takes a list as input. It iterates over each element in the list, and for each element, it checks all the elements that come after it in the list. If it finds a duplicate element, it returns False. If it doesn't find any duplicates, it returns True.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2:
<jupyter_code>
