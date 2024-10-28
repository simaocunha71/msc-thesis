
def search(lst):
    from collections import Counter
    count = Counter(lst)
    numbers = sorted([i for i in count if count[i] >= i])
    return numbers[-1] if numbers else -1

print(search([4, 1, 2, 2, 3, 1])) # 2
print(search([1, 2, 2, 3, 3, 3, 4, 4, 4])) # 3
print(search([5, 5, 4, 4, 4])) # -1


In this solution, we first count the frequency of each number in the list using the Counter class from the collections module. Then, we sort the list of keys in the Counter object (which are the numbers in the original list), based on the frequency of the number (which is the value in the Counter object). We only keep the numbers that have a frequency greater than or equal to their value. Finally, we return the greatest number in the sorted list. If the list is empty (which means no such number exists), we return -1.


This solution runs in O(n log n) time because of the sorting step. The counting step takes O(n) time and the creation of the list to return takes O(n) time. The space complexity is also O(n) because we store the counter object and the list of numbers.


The Counter object is a dictionary subclass for counting hashable objects. It's a collection where elements are stored as dictionary keys and their counts are stored as dictionary values.
    '''
    pass
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 2:
<jupyter_code>
