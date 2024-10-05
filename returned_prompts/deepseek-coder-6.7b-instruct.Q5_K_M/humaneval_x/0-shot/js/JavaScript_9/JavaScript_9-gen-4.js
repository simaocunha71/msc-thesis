  let maxSoFar = -Infinity;
  return numbers.map(num => {
    maxSoFar = Math.max(maxSoFar, num);
    return maxSoFar;
  });
}

console.log(rollingMax([1, 2, 3, 2, 3, 4, 2])); // [1, 2, 3, 3, 3, 4, 4]

The function rollingMax takes an array of integers and returns a new array where each element i is the maximum of numbers[0..i].

The variable maxSoFar is initialized to -Infinity (a very small number), and for each number in the input array, it is updated to be the maximum of its current value and the current number.

This works because:

- For the first number, maxSoFar is not updated and remains -Infinity, so the result array starts with -Infinity.
- For each subsequent number, maxSoFar is updated to be the maximum of its current value and the current number, so the result array is a list of the rolling maximums.
- Finally, the function returns the result array.
*/


// Test cases
console.log(rollingMax([1, 2, 3, 2, 3, 4, 2])); // [1, 2, 3, 3, 3, 4, 4]
console.log(rollingMax([5, 4, 3, 2, 1])); // [5, 5, 5, 5, 5]
console.log(rollingMax([1, 1, 1, 1, 1])); // [1, 1, 1, 1, 1]
console.log(rollingMax([])); // []




























































































