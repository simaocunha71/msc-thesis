
def count_samepair(list1, list2, list3):
    count = 0
    for i in range(len(list1)):
        if list1[i] == list2[i] == list3[i]:
            count += 1
    return count

print(count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9]))

"""
The function works by using a for loop to iterate through each index of the first list. If the items at the current index in all three lists are equal, it increments the count. At the end of the loop, it returns the count.
"""
<jupyter_output>
3
<jupyter_text>
Q2:Write a function to get the unique items from each of the given lists and returns the list of unique items in the order they appear in the first list.
<jupyter_code>
def get_unique(list1, list2, list3):
    unique_items = []
    for i in range(len(list1)):
        if list1[i] not in unique_items:
            unique_items.append(list1[i])
        if list2[i] not in unique_items:
            unique_items.append(list2[i])
        if list3[i] not in unique_items:
            unique_items.append(list3[i])
    return unique_items

print(get_unique([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9]))
<jupyter_output>
[1, 2, 3, 4, 5, 6, 7, 8, 9]
<jupyter_text>
Q3:Write a function to get the common items from each of the given lists.
<jupyter_code>
def get_common(list1, list2, list3):