
    def add_elements(arr, k):
        sum = 0
        for i in range(k):
            if len(str(arr[i])) <= 2:
                sum += arr[i]
        return sum

    arr = [111,21,3,4000,5,6,7,8,9]
    k = 4
    print(add_elements(arr, k))


"""
Test Case:

Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
Output: 24
Explanation: The sum of the elements with at most two digits from the first 4 elements of arr (21 and 3) is 24.
"""

arr = [111,21,3,4000,5,6,7,8,9]
k = 4
print(add_elements(arr, k))

"""
Test Case:

Input: arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], k = 10
Output: 60
Explanation: The sum of the elements with at most two digits from the first 10 elements of arr (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) is 60.
"""

arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
k = 10
print(add_elements(arr, k))

"""
Test Case:

Input: arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000], k = 5
Output: 150