  let smallestEvenValueIndex = -1;
  let smallestEvenValue = Infinity;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] < smallestEvenValue && arr[i] % 2 === 0) {
      smallestEvenValue = arr[i];
      smallestEvenValueIndex = i;
    }
  }

  return smallestEvenValueIndex === -1 ? [] : [smallestEvenValue, smallestEvenValueIndex];
};

console.log(pluck([4,2,3])); // [2, 1]
console.log(pluck([1,2,3])); // [2, 1]
console.log(pluck([])); // []
console.log(pluck([5, 0, 3, 0, 4, 2])); // [0, 1]

// Time Complexity: O(n)
// Space Complexity: O(1)

// Where, n is the number of elements in the array.

```

## JavaScript (ES6)
```javascript
