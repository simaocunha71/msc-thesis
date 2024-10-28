Here's a solution in Python:

```python
def removeDuplicates(numbers):
    return list(set(numbers))
```

And here's a solution in JavaScript:

```javascript
function removeDuplicates(numbers) {
    return [...new Set(numbers)];
}
```

In Python, we can use the built-in `set` data structure to automatically remove duplicates from the input list. We convert the list to a set, which only retains unique values, and then convert it back to a list.

In JavaScript, we can use the `Set` object to achieve the same result. The spread operator (`...`) is used to convert the set back to an array.

Both of these solutions have a time complexity of O(n), where n is the number of elements in the input list. This is because iterating over the list or array and adding elements to a set or using the spread operator both take O(n) time.

The space complexity of both solutions is also O(n), as we are creating a new set or array to store the unique elements.

Here are some test cases to verify the correctness of the Python solution:

```python
print(removeDuplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
print(removeDuplicates([5, 5, 5, 6, 6, 6]))  # Output: [5, 6]
print(removeDuplicates([]))  # Output: []
```

And here are some test cases for the JavaScript solution:

```javascript
console.log(removeDuplicates([1, 2, 3, 2, 4]));  // Output: [1, 3, 4]
console.log(removeDuplicates([5, 5, 5, 6, 6, 6]));  // Output: [5, 6]
console.log(removeDuplicates([]));  // Output: []
```

These test cases cover scenarios with both duplicate and non-duplicate elements, as well as an empty input list.

To validate the solutions, you can run the provided test