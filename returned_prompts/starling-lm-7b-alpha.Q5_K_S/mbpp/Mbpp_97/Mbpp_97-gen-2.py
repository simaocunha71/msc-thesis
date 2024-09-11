def frequency_lists(lst):
    d = {}
    for i in lst:
        for j in i:
            if j in d:
                d[j] += 1
            else:
                d[j] = 1
    return d



def frequency_lists(lst):
    d = {}
    for i in lst:
        for j in i:
            d[j] = d.get(j, 0) + 1
    return d

def frequency_lists(lst):
    d = {}
    for i in lst:
        for j in i:
            d[j] = d.get(j, 0) + 1
    return d

def frequency_lists(lst):
    d = {}
    for i in lst:
        for j in i:
            d[j] = d.get(j, 0) + 1
    return d

def frequency_lists(lst):
    d = {}
    for i in lst:
        for j in i:
            d[j] = d.get(j, 0) + 1
    return d






"""
Explanation:

1. The problem is asking to create a function that takes a flattened list of lists and returns a dictionary with each element as the key and the count of each element in the list as the value.

2. The function should handle flattened lists of varying lengths and with different types of elements.

3. The function should return a dictionary with the counts of each element in the flattened list.

4. The function should be able to handle lists with duplicate elements and should count the frequency of each element correctly.

5. The function should use a dictionary to store the counts of each element.

6. The function should use a loop to iterate through each element in the flattened list and update the count of each element in the dictionary.

7. The function should use the built-in `get()` method of dictionaries to get the current count of each element and increment it by 1. If the element is not in the dictionary, the `get()` method will return 0 and the function will increment the count