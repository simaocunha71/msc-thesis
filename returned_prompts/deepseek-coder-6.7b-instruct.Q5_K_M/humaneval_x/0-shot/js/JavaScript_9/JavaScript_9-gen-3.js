  let max = -Infinity;
  return numbers.map(n => Math.max(max, max = n));
}

console.log(rollingMax([1, 2, 3, 2, 3, 4, 2])); // [1, 2, 3, 3, 3, 4, 4]

Explanation:
The function `rollingMax` maps over the input `numbers` array. For each `n` in `numbers`, it computes the maximum of `max` and `n` and assigns the result back to `max`. The maximum of `max` and `n` is the rolling maximum number encountered so far in the sequence. The result is a new array with these maximums.
*/

const rollingMax = (numbers) => {
  let max = -Infinity;
  return numbers.map(n => Math.max(max, max = n));
}

console.log(rollingMax([1, 2, 3, 2, 3, 4, 2])); // [1, 2, 3, 3, 3, 4, 4]

/*
This solution uses JavaScript's `Array.prototype.map` method to create a new array. For each element in the input array, the function `Math.max` is called with the current `max` and the current element `n`. The result is the maximum of the two, which is the rolling maximum so far. The `max = n` part updates `max` to the current element `n`.
*/

// Explanation:
// The function `rollingMax` maps over the input `numbers` array. For each `n` in `numbers`, it computes the maximum of `max` and `n` and assigns the result back to `max`. The maximum of `max` and `n` is the rolling maximum number encountered so far in the sequence. The result is a new array with these maximums.

// This solution uses JavaScript's `Array.prototype.map` method to create a new array. For each element in the input array, the function `Math.max` is called with the current `max` and the current element `n`. The result