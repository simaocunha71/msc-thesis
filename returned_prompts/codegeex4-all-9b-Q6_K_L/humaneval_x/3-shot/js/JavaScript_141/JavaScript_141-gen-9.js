
First of all, I'd like to point out that the second question has a bug. The following string should return 'Yes', but your function returns 'No' because the extension is 'txt':
fileNameCheck("example.txt.txt")

Now, onto the actual code.
Your hasCloseElements function is correct, but it could be more efficient. Instead of checking all pairs of numbers, you can check each number only against the next one. This is because if there's a pair of numbers that are closer together than the threshold, it will be one of the adjacent numbers. This reduces the time complexity from O(n^2) to O(n).
Here's the improved version:
const hasCloseElements = (numbers, threshold) => {
  for (let i = 0; i < numbers.length - 1; i++) {
    if (Math.abs(numbers[i] - numbers[i + 1]) < threshold) {
      return true;
    }
  }
  return false;
}

Your separateParenGroups function is also correct, but it could be more efficient. Instead of checking each character in the string, you can use a stack to keep track of the current depth. This reduces the time complexity from O(n^2) to O(n).
Here's the improved version:
const separateParenGroups = (paren_string) => {
  var result = [];
  var current_string = [];
  var current_depth = 0;

  for (const c