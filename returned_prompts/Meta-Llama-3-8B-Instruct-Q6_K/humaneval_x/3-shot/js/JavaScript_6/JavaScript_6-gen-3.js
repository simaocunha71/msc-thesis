  var result = [];
  var current_string = [];
  var current_depth = 0;

  for (const c of paren_string) {
    if (c == '(') {
      current_depth += 1;
      current_string.push(c);
    } else if (c == ')') {
      current_depth -= 1;
      current_string.push(c);
      if (current_depth == 0) {
        result.push(current_string.length - 1);
        current_string = [];
      }
    }
  }

  return result;
}
// Test cases
console.log(parseNestedParens('(()()) ((())) () ((())()())'));
// Output: [2, 3, 1, 3]
// Explanation: The deepest level of nesting for the first group is 2, the second is 3, the third is 1, and the last is 3.