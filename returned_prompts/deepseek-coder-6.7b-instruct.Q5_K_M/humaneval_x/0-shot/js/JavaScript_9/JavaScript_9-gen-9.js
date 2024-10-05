  let max = -Infinity;
  return numbers.map((number) => {
    max = Math.max(max, number);
    return max;
  });
};

console.log(rollingMax([1, 2, 3, 2, 3, 4, 2])); // [1, 2, 3, 3, 3, 4, 4]
```

In this solution, we use JavaScript's `map` function to create a new array. For each element in the input array, we calculate the new maximum number seen so far and return this maximum number. The maximum number seen so far is maintained in a variable `max`, which is initialized to `-Infinity`.

This solution has a time complexity of O(n), where n is the length of the input array. This is because we perform a constant amount of work for each element in the array, resulting in a linear time complexity.

The space complexity is also O(n), where n is the length of the input array. This is because we store a new array of the same length as the input array.

This solution assumes that the input array will not be empty and will contain only integers. If these conditions are not met, the solution may not work as expected.

**Note:** The `rollingMax` function uses the `Math.max` method to compare the current number in the array to the current maximum value, and returns the maximum of the two. If the current number is greater than the current maximum, it is set as the new maximum. This process is repeated for each number in the array, creating a new array where each element is the maximum number seen so far.

This solution works by using JavaScript's built-in `map` function, which creates a new array with the results of calling a provided function on every element in the array. The function we provide takes the current number and the current maximum value, and returns the maximum of the two. This new maximum value is then used in the next calculation.

This solution is efficient because it uses a single pass through the input array to calculate the rolling maximum. It also uses a constant amount of space to store the output array.

This solution assumes that the input array will be a non-empty array of integers. If this is not the case, the behavior of the solution is