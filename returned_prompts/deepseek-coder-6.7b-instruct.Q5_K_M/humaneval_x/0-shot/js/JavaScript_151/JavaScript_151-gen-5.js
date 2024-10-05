  let sum = 0;
  lst.forEach(num => {
    if (num > 0 && num % 2 !== 0) {
      sum += num * num;
    }
  });
  return sum;
};

console.log(doubleTheDifference([1, 3, 2, 0]));  // 10
console.log(doubleTheDifference([-1, -2, 0]));  // 0
console.log(doubleTheDifference([9, -2]));  // 81
console.log(doubleTheDifference([0]));  // 0
console.log(doubleTheDifference([]));  // 0

```

## Task 3

Write a function called `removeEvens` that takes a list of numbers as its parameter and returns a new list with all the odd numbers from the original list.

```javascript
