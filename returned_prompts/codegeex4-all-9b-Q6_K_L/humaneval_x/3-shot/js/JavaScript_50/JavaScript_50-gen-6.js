
Here are the solutions to the questions you've asked:

1. Check if in given list of numbers, are any two numbers closer to each other than given threshold.
```javascript
const hasCloseElements = (numbers, threshold) => {
  for (let i = 0; i < numbers.length; i++) {
    for (let j = 0; j < numbers.length; j++) {
      if (i != j) {
        let distance = Math.abs(numbers[i] - numbers[j]);
        if (distance < threshold) {
          return true;
        }
      }
    }
  }
  return false;
}
```

2. Input to this function is a string containing multiple groups of nested parentheses. Your goal is to separate those groups into separate strings and return the list of those. Separate groups are balanced (each open brace is properly closed) and not nested within each other. Ignore any spaces in the input string.
```javascript
const separateParenGroups = (paren_string) => {
  var result = [];
  var current_string = [];
  var current_depth = 0;

  for (const c of paren_string) {
    if (c == '(') {
      current_depth += 1;
      current_string.push(c);
    } else if (c == ')')