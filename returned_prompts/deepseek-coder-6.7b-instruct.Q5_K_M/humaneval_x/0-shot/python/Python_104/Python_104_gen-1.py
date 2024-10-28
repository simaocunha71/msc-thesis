
def unique_digits(x):
    result = []
    for num in x:
        if all(int(digit) % 2 != 0 for digit in str(num)):
            result.append(num)
    return sorted(result)

print(unique_digits([15, 33, 1422, 1]))
print(unique_digits([152, 323, 1422, 10]))

# Test case 2
# Input: [15, 33, 1422, 1]
# Expected Output: [1, 15, 33]
#
# Test case 3
# Input: [152, 323, 1422, 10]
# Expected Output: []

This solution works by iterating over each number in the input list, and for each number, it converts the number to a string and checks if all digits are odd by using the all() function and an if statement. If the condition is met, the number is added to the result list. Finally, the result list is sorted in increasing order before it is returned.

This solution has a time complexity of O(n*m) where n is the number of elements in the input list and m is the number of digits in the maximum number in the list. This is because for each number in the list, we are iterating over each digit in the number. This is an efficient solution as it only requires a single pass over the input list.

This solution also has a space complexity of O(n) where n is the number of elements in the input list. This is because we are storing the result in a new list.

This solution is correct as it correctly identifies and returns the numbers with all odd digits and in sorted order.
<jupyter_output>
<empty_output>
<jupyter_text>
