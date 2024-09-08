def sequential_search(array, element):
    for i in range(len(array)):
        if array[i] == element:
            return (True, i)
    return (False, -1)

print(sequential_search([11,23,58,31,56,77,43,12,65,19],31))

# Output: (True, 3)
<jupyter_output>
(True, 3)
<jupyter_text>
**Explanation:** The function sequential_search iterates over each element in the array. When it finds the element, it immediately returns a tuple containing True and the index of the element. If it doesn't find the element after checking all elements, it returns a tuple containing False and -1.
<jupyter_code>
# Test case
print(sequential_search([11,23,58,31,56,77,43,12,65,19],99))

# Output: (False, -1)
<jupyter_output>
(False, -1)
<jupyter_text>
**Explanation:** In this test case, the function sequential_search returns (False, -1) because the element 99 is not in the given array. **Complexity Analysis:** The time complexity of the sequential search algorithm is O(n) where n is the length of the array. This is because in the worst-case scenario, the algorithm has to traverse through the entire array. The space complexity is O(1) as it uses a constant amount of space.
<jupyter_code>

<jupyter_output>
<empty_output>
<jupyter_text>
**Problem:**Given a string s and an integer k, return the length of the longest substring that contains at most k distinct characters.**Example:**Input: s = "eceba", k = 2Output: 3Explanation: The longest substring with 2 distinct characters is "ece".**Solution:**This problem can be solved using the sliding window technique. We can use