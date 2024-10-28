const intersperse = (numbers, delimeter) => {
  const res = [];
  for (let i = 0; i < numbers.length; i++) {
    res.push(numbers[i]);
    if (i < numbers.length - 1) {
      res.push(delimeter);
    }
  }
  return res;
}

