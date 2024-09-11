def merge_sorted_list(a, b, c):
    result = []
    i = 0
    j = 0
    k = 0
    while i < len(a) and j < len(b) and k < len(c):
        if a[i] < b[j]:
            if a[i] < c[k]:
                result.append(a[i])
                i += 1
            else:
                result.append(c[k])
                k += 1
        else:
            if b[j] < c[k]:
                result.append(b[j])
                j += 1
            else:
                result.append(c[k])
                k += 1
    result += a[i:] + b[j:] + c[k:]
    return result

merge_sorted_list([25, 24, 15, 4, 5, 29, 110],[19, 20, 11, 56, 25, 233, 154],[24, 26, 54, 48])

"""
Explanation:
The function merge_sorted_list takes three lists as input and returns a single sorted list.

It initializes an empty list called result. It also initializes three variables i, j, and k to keep track of the indices of the lists a, b, and c respectively.

The function then enters a while loop that continues until one of the indices reaches the end of its respective list. Inside the while loop, it compares the elements at the current indices i, j, and k of the lists a, b, and c.

If the element in list a at index i is less than the element in list b at index j, it checks if the element in list a is also less than the element in list c at index k. If it is, it appends the element from list a to the result list and increments the index i. Otherwise, it appends the element from list c to the result list and increments the index k.

If the element in list b at index j is less than the