
def search(lst):
    from collections import Counter
    count = Counter(lst)
    max_value = max(count.keys())
    for i in range(max_value, 0, -1):
        if i in count and count[i] >= i:
            return i
    return -1

print(search([4, 1, 2, 2, 3, 1]))  # 2
print(search([1, 2, 2, 3, 3, 3, 4, 4, 4]))  # 3
print(search([5, 5, 4, 4, 4]))  # -1

Explanation:

This function uses the Counter class from the collections module to count the frequency of each integer in the list. It then starts from the maximum value in the list and checks if its frequency is greater than or equal to its value. If it is, it returns the value. If it isn't, it continues to the next largest value, and so on until it finds a value that meets the criteria or it has checked all values. If it hasn't found such a value, it returns -1.

This solution has a time complexity of O(n) as it goes through the list twice: once to count the frequencies and once to find the desired value.

The space complexity is also O(n) because of the space required to store the Counter object.

Note: This solution assumes that all elements in the list are positive integers. If this is not the case, the function should be modified to handle the non-positive integers accordingly.

Also note that the problem statement is a bit ambiguous. It mentions that the frequency of an integer is the number of times it appears in the list, but it also mentions that the frequency of an integer is greater than or equal to the integer itself. This can lead to some confusion. In the examples provided, the frequency of 2 is 2, which is greater than the integer 2 itself, but the frequency of 3 is 3, which is not greater than the integer 3 itself. If the problem statement is to count the number of times the integer itself appears, then the function should be modified to count the frequency of the integer itself.

Here is the modified function:
