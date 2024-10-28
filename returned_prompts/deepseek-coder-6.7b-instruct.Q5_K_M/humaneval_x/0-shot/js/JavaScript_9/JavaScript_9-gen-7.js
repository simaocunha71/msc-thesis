  let max = -Infinity;
  return numbers.map(number => {
    max = Math.max(max, number);
    return max;
  });
}

console.log(rollingMax([1, 2, 3, 2, 3, 4, 2])) // [1, 2, 3, 3, 3, 4, 4]

Explanation:
This solution uses the JavaScript built-in `map` function to create a new array. For each element in the input array, the function checks whether the current number is greater than the current maximum. If it is, the current number becomes the new maximum. If not, the current maximum remains unchanged.

The maximum value is then added to the new array. This continues for all elements in the input array. The result is a new array where each element is the maximum value found in the input array up to that point.

This solution has a time complexity of O(n), where n is the length of the input array.

Also, it uses the `Math.max` function, which returns the largest of zero or more numbers.
*/

// Test cases
console.log(rollingMax([1])) // [1]
console.log(rollingMax([1, 1])) // [1, 1]
console.log(rollingMax([1, 2, 3])) // [1, 2, 3]
console.log(rollingMax([3, 2, 1])) // [3, 3, 3]
console.log(rollingMax([])) // []

/*
Expected output:
[1, 2, 3, 3, 3, 4, 4]
[1]
[1, 1]
[3, 3, 3]
[]
*/

// End of solution
```

## Explanation

This solution uses the JavaScript built-in `map` function to create a new array. For each element in the input array, the function checks whether the current number is greater than the current maximum. If it is, the current number becomes the new maximum. If not, the current maximum remains unchanged.

The maximum value is then added to the new array. This continues for all elements in the input array.