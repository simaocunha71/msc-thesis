
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

function separateParenGroups(paren_string) {
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

const truncateNumber = (number) => {
  return number % 1.0;
}

const sortEven = (l) => {
  var even = l.filter((num, i) => i % 2 == 0);
  even.sort();

  for (let i = 0; i < even.length; i++) {
    l[i * 2] = even[i];
  }

  return l;
}