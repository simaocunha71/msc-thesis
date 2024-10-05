
def by_length(arr):
    num_names = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    result = []
    for i in arr:
        if 1 <= i <= 9:
            result.append(i)
    result.sort(reverse=True)
    return [num_names[i-1] for i in result]

print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))  # ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
print(by_length([]))  # []
print(by_length([1, -1, 55]))  # ['One']

# The function `by_length` first creates an empty list `result`. Then it iterates through `arr` and if a number is between 1 and 9 inclusive, it is appended to `result`. After sorting `result` in descending order, it replaces each digit by its corresponding name from `num_names` and returns the result.

# Note: The list `num_names` is zero-indexed, so when it is used to index into `result`, `i-1` is used to account for this.

# The function handles empty arrays by returning an empty array immediately when `arr` is empty.

# If `arr` contains numbers outside the 1-9 range, they are ignored because they are not appended to `result`.

# The function handles strange numbers by ignoring them, because they are not appended to `result`.

# The time complexity of this function is O(n log n) because of the sorting operation, where n is the length of `arr`. The space complexity is O(n) for storing the result.

# This function assumes that the input is always an array of integers. If this is not the case, additional error checking should be added.

# Test the function with some examples to verify that it works as expected.
print(by_length([2, 1, 1, 4, 5, 8, 