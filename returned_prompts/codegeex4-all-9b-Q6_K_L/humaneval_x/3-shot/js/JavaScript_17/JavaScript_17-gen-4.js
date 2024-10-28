
1. Check if in given list of numbers, are any two numbers closer to each other than given threshold.

It seems you are looking for two numbers that have a distance less than the threshold. You can use the following approach:

Use a nested loop to iterate over all pairs of numbers in the list.
For each pair, calculate the absolute difference between the two numbers.
If the difference is less than the threshold, return true immediately.
If no such pair is found, return false at the end.

Here is the updated code:

```javascript
const hasCloseElements = (numbers, threshold) => {
  for (let i = 0; i < numbers.length; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      let distance = Math.abs(numbers[i] - numbers[j]);
      if (distance < threshold) {
        return true;
      }
    }
  }
  return false;
}
```

2. Input to this function is a string containing multiple groups of nested parentheses. Your goal is to separate those group into separate strings and return the list of those.

You can use a stack to keep track of the nested parentheses. Here is the updated code:

```javascript
const separateParenGroups = (paren_string) => {
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
        result.push(current_string.join(''));
        current_string = [];
      }
    }
  }

  return result;
}
```

3. Given a positive floating point number, it can be decomposed into an integer part (largest integer smaller than given number) and decimals (leftover part always smaller than 1). Return the decimal part of the number.

You can use the modulus operator