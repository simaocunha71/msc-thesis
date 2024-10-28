  let evenIndices = l.filter((_, i) => i % 2 === 0);
  evenIndices.sort((a, b) => a - b);

  return l.map((_, i) => (i % 2 === 0) ? evenIndices.shift() : l[i]);
}

console.log(sortEven([1, 2, 3])); // [1, 2, 3]
console.log(sortEven([5, 6, 3, 4])); // [3, 6, 5, 4]
```

This code works by first creating a new array `evenIndices` with the values at the even indices of the input list `l`, then sorting this array in ascending order. Then it creates a new list that contains the values at the even indices replaced with the sorted values from `evenIndices` and the values at the odd indices left as they are in the input list `l`.

The `map` function is used to create the new list, and the `shift` method is used to remove and return the first element from `evenIndices` after it has been used. This ensures that the values at the even indices of the output list are sorted in ascending order.

The time complexity of this function is O(n log n), where n is the length of the input list `l`. This is because it sorts the list of values at the even indices, which takes O(n log n) time. The rest of the function runs in linear time, so the total time complexity is dominated by the sorting step.

The space complexity is also O(n), where n is the length of the input list `l`. This is because it creates a new list with the values at the even indices, which requires O(n) space. The rest of the function also creates a new list, so the total space complexity is dominated by the list of values at the even indices.
</details>

<details>
<summary>
<b>Task 4:</b> Implement the function `filterOddSquare`.
</summary>

