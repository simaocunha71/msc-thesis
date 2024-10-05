To solve this problem, we can iterate through the array and keep track of the smallest even value and its index. We start by setting the smallest even value to Infinity and the index to -1. As we iterate through the array, we check if the current number is even and if it is smaller than the current smallest even value. If it is, we update the smallest even value and the index. Finally, we return the smallest even value and its index in a list. If there are no even values or the array is empty, we return an empty list.

Here is the implementation in JavaScript:

```javascript
const pluck = (arr) => {
  let smallestEvenValue = Infinity;
  let index = -1;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] % 2 === 0 && arr[i] < smallestEvenValue) {
      smallestEvenValue = arr[i];
      index = i;
    }
  }

  if (smallestEvenValue === Infinity) {
    return [];
  } else {
    return [smallestEvenValue, index];
  }
}
```

We can test the function with the given examples:

```javascript
console.log(pluck([4, 2, 3])); // [2, 1]
console.log(pluck([1, 2, 3])); // [2, 1]
console.log(pluck([])); // []
console.log(pluck([5, 0, 3, 0, 4, 2])); // [0, 1]
```