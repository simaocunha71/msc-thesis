  let seen = {};
  for (let num of l) {
    if (seen[num]) {
      return true;
    }
    seen[-num] = true;
  }
  return false;
};

console.log(pairsSumToZero([1, 3, 5, 0])); // false
console.log(pairsSumToZero([1, 3, -2, 1])); // false
console.log(pairsSumToZero([1, 2, 3, 7])); // false
console.log(pairsSumToZero([2, 4, -5, 3, 5, 7])); // true
console.log(pairsSumToZero([1])); // false
```

## TASK 2

```js
