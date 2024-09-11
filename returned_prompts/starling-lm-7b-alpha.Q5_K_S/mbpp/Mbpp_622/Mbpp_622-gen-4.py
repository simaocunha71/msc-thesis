"""
To find the median of two sorted lists, we can follow these steps:

First, merge the two lists into a single sorted list. This can be done by iterating through both lists and comparing the elements. If an element from the first list is smaller, add it to the merged list. If an element from the second list is smaller, add it to the merged list. If the elements are equal, add either one to the merged list.

Once the merged list is obtained, we can find the median by checking the length of the merged list. If the length is odd, the median is the element at the middle index. If the length is even, the median is the average of the elements at the two middle indices.

Here's an example implementation of the function in Python:

def get_median(list1, list2, size):
    merged_list = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    merged_list += list1[i:] + list2[j:]
    if len(merged_list) % 2 == 0:
        return (merged_list[len(merged_list) // 2 - 1] + merged_list[len(merged_list) // 2]) / 2.0
    else:
        return merged_list[len(merged_list) // 2]

In the example implementation, we initialize an empty list called merged_list to store the merged elements. We use two pointers, i and j, to iterate through list1 and list2 respectively. We compare the elements at the current indices and append the smaller element to merged_list. After merging the lists, we add any remaining elements from list1 or list2 to merged_list. Finally, we check the length of merged_list and return the median accordingly.

The assert statement provided in the question can be used to test the function and verify that it returns the correct median for the given input.
"""

# Python