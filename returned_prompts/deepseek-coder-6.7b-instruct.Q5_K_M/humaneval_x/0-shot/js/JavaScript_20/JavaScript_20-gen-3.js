  numbers.sort((a, b) => a - b);
  let minDifference = Infinity;
  let closestPair;

  for (let i = 0; i < numbers.length - 1; i++) {
    const difference = numbers[i + 1] - numbers[i];
    if (difference < minDifference) {
      minDifference = difference;
      closestPair = [numbers[i], numbers[i + 1]];
    }
  }

  return closestPair;
};

console.log(findClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])); // (2.0, 2.2)
console.log(findClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])); // (2.0, 2.0)

// The solution sorts the input array in ascending order. This allows it to iterate over the array and compute the differences between each pair of successive numbers. 
// If the difference is smaller than the currently smallest difference, it updates the smallest difference and the closest pair. 
// Finally, it returns the closest pair.

// The time complexity of this solution is O(n log n) due to the sorting operation. 
// The space complexity is O(1) because it only uses a constant amount of extra space.








































































































































































