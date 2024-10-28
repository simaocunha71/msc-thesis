  // Split the string into an array of groups
  const groups = paren_string.split(' ');

  // Initialize an array to hold the maximum depth of each group
  const maxDepths = [];

  // Iterate over each group
  for (let group of groups) {
    // Initialize a variable to hold the current depth
    let currentDepth = 0;

    // Initialize a variable to hold the maximum depth
    let maxDepth = 0;

    // Iterate over each character in the group
    for (let char of group) {
      // If the character is a '(', increment the current depth
      if (char === '(') {
        currentDepth++;

        // If the current depth is greater than the maximum depth, update the maximum depth
        if (currentDepth > maxDepth) {
          maxDepth = currentDepth;
        }
      }

      // If the character is a ')', decrement the current depth
      else if (char === ')') {
        currentDepth--;
      }
    }

    // Add the maximum depth to the maxDepths array
    maxDepths.push(maxDepth);
  }

  // Return the maxDepths array
  return maxDepths;
};

console.log(parseNestedParens('(()()) ((())) () ((())()())'));
// Output: [2, 3, 1, 3]
```

This JavaScript function iterates over each group of parentheses, and for each group, it iterates over each character. If the character is a '(', it increments the current depth and checks if this new depth is greater than the maximum depth so far. If it is, it updates the maximum depth. If the character is a ')', it decrements the current depth. The function then returns an array containing the maximum depth for each group.

This function assumes that the input string is well-formed, i.e., it contains only parentheses and spaces, and that each group of parentheses is correctly nested. If the input string might not be well-formed, the function would need to be modified to handle such cases.

This function has a time complexity of O(n), where n is the total number of characters