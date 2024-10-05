  let sum = 0;
  for (let i = 0; i < lst.length; i++) {
    if (lst[i] > 0 && Number.isInteger(lst[i]) && lst[i] % 2 !== 0) {
      sum += lst[i] ** 2;
    }
  }
  return sum;
};

console.log(doubleTheDifference([1, 3, 2, 0])); // 10
console.log(doubleTheDifference([-1, -2, 0])); // 0
console.log(doubleTheDifference([9, -2])); // 81
console.log(doubleTheDifference([0])); // 0
console.log(doubleTheDifference([])); // 0

```

## Problem 3

```js
