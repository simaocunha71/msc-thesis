
def can_arrange(arr):
    for i in range(len(arr)-1, 0, -1):
        if arr[i] < arr[i-1]:
            return i
    return -1

print(can_arrange([1,2,4,3,5])) # 3
print(can_arrange([1,2,3])) # -1

# The function loops through the array in reverse order. If it finds an element that is less than the previous one, it returns the index. If it doesn't find such an element, it returns -1.
<jupyter_output>
3
-1
<jupyter_text>
Problem 2Given a list of integers, write a function that returns True if the list is a palindrome and False if it is not. A palindrome is a list that remains the same when reversed.
<jupyter_code>
