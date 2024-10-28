
I have tried to solve the problems you've posted:
1.
This function checks if the array 'numbers' has two numbers closer to each other than given 'threshold'.
const hasCloseElements = (numbers, threshold) => {
  for (let i = 0; i < numbers.length; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      if (Math.abs(numbers[i] - numbers[j]) < threshold) {
        return true;
      }
    }
  }
  return false;
}

2.
This function separates groups of nested parentheses from a given string.
const separateParenGroups = (paren_string) => {
  var result = [];
  var current_string = '';
  var current_depth = 0;

  for (const c of paren_string) {
    if (c == '(') {
      current_depth += 1;
      current_string += c;
    } else if (c == ')') {
      current_depth -= 1;
      current_string += c;
      if (current_depth == 0) {
        result.push(current_string);
        current_string = '';
      }
    }
  }

  return result;
}

3.
This function returns the decimal part of a given number.
const truncateNumber = (number) => {
  return number - Math.floor(number);
}

4.
This function returns the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
const fizzBuzz = (n) => {
  var count = 0;
  for (var i = 0; i < n; i++) {
    if (i % 11 == 0 || i % 13 == 0) {
      var s = i.toString();
      for (var j = 0; j < s.length; j++) {
        if (s[j] == '7') {
          count += 1;
        }
      }
    }
  }
  return count;
}