```js
const pluck = (arr) => {
  // edge case: if array is empty, return empty array
  if (arr.length === 0) {
    return [];
  }

  // initialize smallest even value and its index as null and -1 respectively
  let smallestEvenValue = null;
  let smallestEvenIndex = -1;

  // iterate through the array
  for (let i = 0; i < arr.length; i++) {
    // check if current element is even
    if (arr[i] % 2 === 0) {
      // if smallest even value is null or current element is smaller than smallest even value
      if (smallestEvenValue === null || arr[i] < smallestEvenValue) {
        // update smallest even value and its index
        smallestEvenValue = arr[i];
        smallestEvenIndex = i;
      }
    }
  }

  // if no even value is found, return empty array
  if (smallestEvenValue === null) {
    return [];
  }

  // return the smallest even value and its index
  return [smallestEvenValue, smallestEvenIndex];
};

console.log(pluck([4, 2, 3])); // [2, 1]
console.log(pluck([1, 2, 3])); // [2, 1]
console.log(pluck([])); // []
console.log(pluck([5, 0, 3, 0, 4, 2])); // [0, 1]
```
