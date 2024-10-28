  const set = new Set();

  for (let num of l) {
    if (set.has(-num)) {
      return true;
    }
    set.add(num);
  }

  return false;
}

console.log(pairsSumToZero([1, 3, 5, 0])); // false
console.log(pairsSumToZero([1, 3, -2, 1])); // false
console.log(pairsSumToZero([1, 2, 3, 7])); // false
console.log(pairsSumToZero([2, 4, -5, 3, 5, 7])); // true
console.log(pairsSumToZero([1])); // false

```

### Solution:

```javascript
const pairsSumToZero = (l) => {
  const set = new Set();

  for (let num of l) {
    if (set.has(-num)) {
      return true;
    }
    set.add(num);
  }

  return false;
}

console.log(pairsSumToZero([1, 3, 5, 0])); // false
console.log(pairsSumToZero([1, 3, -2, 1])); // false
console.log(pairsSumToZero([1, 2, 3, 7])); // false
console.log(pairsSumToZero([2, 4, -5, 3, 5, 7])); // true
console.log(pairsSumToZero([1])); // false
```

Explanation:

In this solution, we use a set to store the numbers we have seen so far. For each number in the list, we check if its negation is in the set. If it is, that means we have found two numbers that sum to zero, so we return true. If we make it through the entire list without finding two numbers that sum to zero, we return false.

The time complexity of this solution is O(n), where n is the length of the list. This is because we traverse the list once and perform a constant amount of work for each