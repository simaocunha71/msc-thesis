
hasCloseElements
Your nested loop is fine, but it can be made a little more efficient by sorting the array first.  This way, you only need to check the next element in the sorted array (instead of looping over the entire array).
const hasCloseElements = (numbers, threshold) => {
  numbers.sort((a, b) => a - b);

  for (let i = 0; i < numbers.length - 1; i++) {
    if (numbers[i + 1] - numbers[i] < threshold) {
      return true;
    }
  }

  return false;
}

separateParenGroups
Your implementation is fine, but you can make it more concise by using Array.reduce.
const separateParenGroups = (paren_string) => {
  const result = [];
  let current_string = [];
  let current_depth = 0;

  for (const c of paren_string) {
    if (c === '(') {
      current_depth += 1;
    } else if (c === ')') {
      current_depth -= 1;
    }

    current_string.push(c);

    if (current_depth === 0) {
      result.push(current_string.join(''));
      current_string = [];
    }
  }

  return result;
}

truncateNumber
Your implementation is fine, but you can make it more concise by using Math.trunc.
const truncateNumber = (number) => {
  return Math.trunc(number);
}

isEqualToSumEven
Your implementation is fine, but you can make it more efficient by using Array.reduce.
const isEqualToSumEven = (n) => {
  const numbers = Array.from({ length: n / 2 }, (_, i) => i * 2 + 2);
  return numbers.reduce((total, num) => total