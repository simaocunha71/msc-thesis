
def pluck(arr):
    smallest = float('inf')
    index = -1
    for i, num in enumerate(arr):
        if num < smallest and num % 2 == 0:
            smallest = num
            index = i
    if smallest == float('inf'):
        return []
    else:
        return [smallest, index]

# Test Cases
print(pluck([4,2,3])) # Output: [2, 1]
print(pluck([1,2,3])) # Output: [2, 1]
print(pluck([])) # Output: []
print(pluck([5, 0, 3, 0, 4, 2])) # Output: [0, 1]

# Complexity Analysis
# Time Complexity: O(n) as we traverse the list once.
# Space Complexity: O(1) as we use constant amount of space.

# The function works by iterating over each element in the array, checking if it is an even number and if it is smaller than the current smallest.
# If it is, we update the smallest and index. If there are multiple smallest even numbers, we keep the one with the smallest index.
# If no even number is found, we return an empty list.
# If an even number is found, we return a list with the number and its index.
<jupyter_output>
<empty_output>
<jupyter_text>
5. Problem 5: Reverse Linked ListGiven the head of a singly linked list, reverse the list, and return the reversed list. Example 1:Input: head = [1,2,3,4,5]Output: [5,4,3,2,1]Example 2:Input: head = [1,2]Output: [2,1]Example 3:Input: head = []Output: [] Constraints:The number of nodes in the list is the range [0, 5000].-5000 <= Node.val <= 5000Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
<jupyter_code>
