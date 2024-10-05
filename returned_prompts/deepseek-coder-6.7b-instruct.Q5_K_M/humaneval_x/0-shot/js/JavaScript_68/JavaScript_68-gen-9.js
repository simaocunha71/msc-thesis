  let smallestEven = [Infinity, -1];

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] % 2 === 0 && arr[i] < smallestEven[0]) {
      smallestEven = [arr[i], i];
    }
  }

  return smallestEven[1] === -1 ? [] : smallestEven;
};

console.log(pluck([4,2,3])); // [2, 1]
console.log(pluck([1,2,3])); // [2, 1]
console.log(pluck([])); // []
console.log(pluck([5, 0, 3, 0, 4, 2])); // [0, 1]

module.exports = pluck;

```

### 2. Testing

Test the pluck function in the following ways:

- Pass an array with a single element where the only element is even. The function should return the element and its index.
- Pass an array with a single element where the only element is odd. The function should return an empty array.
- Pass an array with two elements where the first is the smallest even number. The function should return the number and its index.
- Pass an array with two elements where the second is the smallest even number. The function should return the number and its index.
- Pass an array with three elements where one of them is the smallest even number. The function should return the number and its index.
- Pass an array with three elements where the smallest even number appears twice. The function should return the smallest number and its index.
- Pass an empty array. The function should return an empty array.
- Pass an array with a large number of elements. The function should return the smallest even number and its index.
- Pass an array with all odd numbers. The function should return an empty array.

### 3. Debugging

If the function is not working as expected, debug it by:

- Stepping through the code with a debugger to see where it is failing.
- Printing the value of variables at different points in the code to understand what is happening.
- Comparing the output of the function to expected output.
-