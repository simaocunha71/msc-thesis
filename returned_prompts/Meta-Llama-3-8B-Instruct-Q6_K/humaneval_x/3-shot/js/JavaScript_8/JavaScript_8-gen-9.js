  let sum = 0;
  let product = 1;

  for (let i = 0; i < numbers.length; i++) {
    sum += numbers[i];
    product *= numbers[i];
  }
  return [sum, product];
}  // or return [numbers.reduce((a, b) => a + b, 0), numbers.reduce((a, b) => a * b, 1)]



