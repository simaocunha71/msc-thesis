  let sum = 0;
  let product = 1;
  for (const number of numbers) {
    sum += number;
    product *= number;
  }
  return [sum, product];
} // or return [numbers.reduce((a, b) => a + b, 0), numbers.reduce((a, b) => a * b, 1)]



