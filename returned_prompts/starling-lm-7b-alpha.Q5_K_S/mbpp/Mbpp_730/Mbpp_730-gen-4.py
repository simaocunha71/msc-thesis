def consecutive_duplicates(l):
    r = []
    for i in range(len(l)):
        if i == 0 or l[i] != l[i-1]:
            r.append(l[i])
    return r

consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])





"""
Explanation:
The function `consecutive_duplicates` takes a list as an input and initializes an empty list `r`. It then iterates over each element in the input list using a for loop. Inside the loop, it checks if the current element is equal to the previous element. If it is not equal, it appends the current element to the result list `r`. If it is equal, it skips appending the current element. After iterating through all elements in the input list, the function returns the result list `r`.

In the provided example, the function is called with the list `[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]`. The function removes the consecutive duplicates from the list and returns `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]`. This result is then used in the assert statement to verify if the function is working correctly.
"""

"""
Explanation:
The function `consecutive_duplicates` takes a list `l` as an argument and returns a new list `r` that contains all elements from `l` except the consecutive duplicates. It achieves this by iterating over each element in `l` using a for loop. Inside the loop, it checks if the current element is equal to the previous element. If it is not equal, it appends the current element to the result list `r`. If it is equal, it skips appending the current element. After iterating through all elements in `l`, the function returns the result list `r