```
  let seen = new Set();
  let result = [];

  for (let num of numbers) {
    if (!seen.has(num)) {
      seen.add(num);
      result.push(num);
    }
  }

  return result;
}
```

Explanation:
The problem asks to remove duplicates from a list of integers while preserving the order of elements. We can achieve this by iterating over the input list and adding each element to a set (which automatically removes duplicates) and a result array.

The `Set` data structure in JavaScript is a collection of unique values. We iterate over the input list and for each number, we check if it's already present in the `Set`. If not, we add it to the `Set` and the result array. This way, we ensure that each number appears only once in the result.

The time complexity of this solution is O(n), where n is the length of the input list, because we're iterating over the list once. The space complexity is also O(n), because in the worst case, the size of the `Set` and the result array can be equal to the size of the input list. However, in practice, the space complexity is usually less than O(n) because the `Set` will contain fewer elements than the input list.