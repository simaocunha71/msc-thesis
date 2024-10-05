  let sortedNumbers = numbers.slice().sort((a, b) => a - b);
  let smallestDifference = Infinity;
  let closestElements = [];

  for (let i = 0; i < sortedNumbers.length - 1; i++) {
    let difference = sortedNumbers[i + 1] - sortedNumbers[i];

    if (difference < smallestDifference) {
      smallestDifference = difference;
      closestElements = [sortedNumbers[i], sortedNumbers[i + 1]];
    }
  }

  return closestElements;
};

// Tests
console.log(findClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])); // (2.0, 2.2)
console.log(findClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])); // (2.0, 2.0)
```

# 5. Split a number into its digits and return them in a list:
