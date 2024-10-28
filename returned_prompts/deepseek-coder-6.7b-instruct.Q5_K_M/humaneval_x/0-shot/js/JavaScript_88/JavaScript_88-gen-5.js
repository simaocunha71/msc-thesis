  const newArray = array.slice();
  const sum = array[0] + array[array.length - 1];

  return newArray.sort((a, b) => {
    if (sum % 2 === 0) {
      return b - a;
    } else {
      return a - b;
    }
  });
};

console.log(sortArray([])); // []
console.log(sortArray([5])); // [5]
console.log(sortArray([2, 4, 3, 0, 1, 5])); // [0, 1, 2, 3, 4, 5]
console.log(sortArray([2, 4, 3, 0, 1, 5, 6])); // [6, 5, 4, 3, 2, 1, 0]

/*
  Explanation:
  * First, we create a copy of the given array to avoid mutating the original array.
  * Then, we calculate the sum of the first and last element of the array.
  * If the sum is even, we sort the array in descending order.
  * If the sum is odd, we sort the array in ascending order.
 */
```

## 3. Sum of Two Lowest Positive Integers

```js
