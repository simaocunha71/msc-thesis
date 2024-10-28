  // First, we split the input string by spaces to get the individual groups.
  let groups = paren_string.split(' ');

  // Then, we initialize an array to store the maximum depth for each group.
  let depths = [];

  // For each group, we calculate its maximum depth and add it to the array.
  for (let group of groups) {
    let maxDepth = 0;
    let currentDepth = 0;

    // We iterate over each character in the group.
    for (let char of group) {
      if (char === '(') {
        currentDepth += 1;
        if (currentDepth > maxDepth) {
          maxDepth = currentDepth;
        }
      } else if (char === ')') {
        currentDepth -= 1;
      }
    }

    // We add the maximum depth to the depths array.
    depths.push(maxDepth);
  }

  // Finally, we return the depths array.
  return depths;
};

console.log(parseNestedParens('(()()) ((())) () ((())()())'));
// Expected output: [2, 3, 1, 3]
```

## 13. 객체 비교

