  for(let i = 0; i < l.length; i++) {
    for(let j = i + 1; j < l.length; j++) {
      if(l[i] + l[j] === 0) {
        return true;
      }
    }
  }
  return false;
}

module.exports = pairsSumToZero;

// The time complexity of this function is O(n^2), where n is the length of the input list.
// This is because for each element in the list, we are checking all the other elements to see if they sum to zero.
// So the total number of operations is n * (n - 1) / 2, which is quadratic.
// The space complexity is O(1) because we are not using any additional space that scales with the size of the input.
// The function works by iterating over each pair of elements in the list and checking if they sum to zero.
// If it finds such a pair, it immediately returns true. If it goes through the entire list without finding such a pair, it returns false.
// This solution assumes that the input list contains no duplicate elements. If duplicate elements are allowed, the function would need to be modified to check for pairs of distinct elements.

```

## 1.4.10.2. JavaScript (ES6)

```js
