
Your hasCloseElements function is inefficient, and can be fixed by reducing the number of comparisons you need to make.
Instead of checking every pair of elements, you can sort the array first and then check only adjacent elements. This will reduce the time complexity from O(n^2) to O(n log n).
Here's the updated function:
const hasCloseElements = (numbers, threshold) => {
  numbers.sort((a, b) => a - b);
  for (let i = 0; i < numbers.length - 1; i++) {
    if (numbers[i + 1] - numbers[i] < threshold) {
      return true;
    }
  }
  return false;
}

Your separateParenGroups function has a bug. It only checks for balanced parentheses, but it doesn't account for the fact that separate groups of parentheses can be nested inside each other.
Here's a corrected version of the function:
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
        current