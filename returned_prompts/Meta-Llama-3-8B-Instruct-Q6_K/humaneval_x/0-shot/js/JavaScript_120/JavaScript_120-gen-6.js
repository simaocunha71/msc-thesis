The problem can be solved by sorting the array in descending order and then selecting the top k elements. Here is a JavaScript solution:
```
const maximum = (arr, k) => {
  return arr.sort((a, b) => b - a).slice(0, k);
};
```
This solution uses the `sort()` method to sort the array in descending order, and then uses the `slice()` method to select the top k elements. The `slice()` method returns a new array with the elements from the original array, starting from the beginning and ending at the specified index (in this case, `k`).

For example, if `arr` is `[-3, -4, 5]` and `k` is `3`, the solution will return `[-4, -3, 5]`, which are the top 3 elements in the sorted array.

Here is the explanation:

1. `arr.sort((a, b) => b - a)`: This line sorts the array in descending order. The comparison function `(a, b) => b - a` returns a negative value if `b` is greater than `a`, which means that `b` will come before `a` in the sorted array.
2. `slice(0, k)`: This line selects the top `k` elements from the sorted array. The `slice()` method returns a new array with the elements from the original array, starting from the beginning and ending at the specified index (`k`).

The time complexity of this solution is O(n log n), where `n` is the length of the array, because the `sort()` method has a time complexity of O(n log n). The space complexity is O(1), because only a few extra variables are needed to store the result.