  lst.sort((a, b) => a - b);
  let result = [];
  while (lst.length) {
    result.push(lst.shift()); // Get and remove the first element
    if (lst.length) {
      result.push(lst.pop()); // Get and remove the last element
    }
  }
  return result;
};

console.log(strangeSortList([1, 2, 3, 4])); // [1, 4, 2, 3]
console.log(strangeSortList([5, 5, 5, 5])); // [5, 5, 5, 5]
console.log(strangeSortList([])); // []

```

The `strangeSortList` function first sorts the input list in ascending order. Then, it alternatively takes and removes the first and last elements from the list, adding them to the result, until the list is empty. The result will be a list sorted in a strange order.

The `while` loop continues until the list is empty. The `shift()` function removes the first element from the list, and the `pop()` function removes the last element. The `result` array accumulates the elements in the strange order.

This solution has a time complexity of O(n log n) because of the sorting operation, and a space complexity of O(n) for the result array.

Please note that the problem description and examples don't match. The examples suggest that the function should return the elements in a "strange" order, but the problem description doesn't clarify what the "strange" order should be. The provided solution assumes that the "strange" order is alternating between the smallest and largest remaining elements, which is consistent with the examples given.

```

```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```