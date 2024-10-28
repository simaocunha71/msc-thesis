```
  // create copy of array
  let copy = [...array];

  // get sum of first and last element
  let sum = copy[0] + copy[copy.length - 1];

  // check if sum is odd or even
  if (sum % 2 !== 0) {
    // if sum is odd, sort array in ascending order
    copy.sort((a, b) => a - b);
  } else {
    // if sum is even, sort array in descending order
    copy.sort((a, b) => b - a);
  }

  return copy;
};
```