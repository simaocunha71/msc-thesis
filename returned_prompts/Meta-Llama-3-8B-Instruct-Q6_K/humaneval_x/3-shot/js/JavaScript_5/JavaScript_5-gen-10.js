  if (numbers.length < 2) {
    return numbers;
  }
  return [numbers[0]].concat(Array(numbers.length - 1).fill(delimeter).map(() => delimeter)).concat(numbers.slice(1));
}