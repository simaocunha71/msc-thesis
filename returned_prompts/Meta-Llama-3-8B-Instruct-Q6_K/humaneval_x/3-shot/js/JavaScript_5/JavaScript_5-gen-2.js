  if (numbers.length === 0) {
    return numbers;
  }
  return [numbers[0]].concat.apply([].concat, numbers.slice(1).map(x => [delimeter, x])).slice(1);
}