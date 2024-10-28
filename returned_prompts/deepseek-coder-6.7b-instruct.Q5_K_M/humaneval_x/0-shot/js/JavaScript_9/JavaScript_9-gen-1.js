let max = -Infinity;
return numbers.map(n => {
  max = Math.max(n, max);
  return max;
});
}
```

The function `rollingMax` takes an array of numbers as input and returns a new array where each element is the maximum of the current element and the previous maximum. It does this by initializing `max` to `-Infinity` and then updating `max` to the maximum of `n` and `max` at each step of the `map`.

The `map` function is used to create a new array where each element is the result of calling the provided function on the corresponding element of the input array. The provided function takes a number `n` and returns the maximum of `n` and `max`. The result is a new array where each element is the maximum of the input array up to the corresponding index.

The time complexity of this function is O(n), where n is the length of the input array. This is because it needs to iterate over the input array once. The space complexity is also O(n), because it creates a new array of the same length as the input array.

The function `rollingMax` can be used to find the maximum element in a sequence of numbers, which can be useful for a variety of applications, such as finding the maximum value in a sliding window of data or in a data stream.

*/

/*
