The function `pairsSumToZero` takes a list of integers as an input and returns `true` if there are two distinct elements in the list that sum to zero, and `false` otherwise. This function uses a `for` loop to iterate through each element in the list. For each element, it uses another `for` loop to check if there is another element in the list that, when added to the current element, equals zero. If such a pair is found, the function returns `true`. If the loops complete without finding a pair that sums to zero, the function returns `false`.

Here is the implementation of the function:

```javascript
const pairsSumToZero = (l) => {
  for (let i = 0; i < l.length; i++) {
    for (let j = i + 1; j < l.length; j++) {
      if (l[i] + l[j] === 0) {
        return true;
      }
    }
  }
  return false;
};
```

Let's test the function with the provided examples:

```javascript
console.log(pairsSumToZero([1, 3, 5, 0])); // false
console.log(pairsSumToZero([1, 3, -2, 1])); // false
console.log(pairsSumToZero([1, 2, 3, 7])); // false
console.log(pairsSumToZero([2, 4, -5, 3, 5, 7])); // true
console.log(pairsSumToZero([1])); // false
```

The function should return the expected results for each test case.