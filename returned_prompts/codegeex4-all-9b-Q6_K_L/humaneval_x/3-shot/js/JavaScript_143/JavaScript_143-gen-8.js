
hasCloseElements
There's a lot of redundancy here. First, you can iterate over the list once instead of twice. Second, you don't actually need to calculate the distance. You're just looking for any two numbers that are within a certain distance of each other, so you can just check if the difference between the two numbers is less than the threshold.

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

separateParenGroups
This is a good job of using a loop to iterate over the string and a variable to keep track of the current depth. However, there are a couple of issues. First, you're not checking for balanced parentheses. This means that if you have a string like '(( ))', it will be split into ['()', '()', ''] instead of ['()', '(())']. Second, you're not ignoring spaces.

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

truncateNumber
This is a good job of using the modulus operator to calculate the decimal part of a number. However, there's a more straightforward way to do this using the built-in toFixed() method.

const truncateNumber = (number) => {
  return number % 1.0;
}

wordsInSentence
This is a good job of