  if (numbers.length <= 1) {
    return numbers;
  } else {
    return [numbers[0]].concat(Array(numbers.length - 1).fill(delimeter).map(() => delimeter)).concat(numbers.slice(1));
  }
} 