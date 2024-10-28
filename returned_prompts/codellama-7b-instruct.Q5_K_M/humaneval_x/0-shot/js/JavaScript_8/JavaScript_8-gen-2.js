const sumProduct = (numbers) => {
  const sum = numbers.reduce((a, b) => a + b, 0);
  const product = numbers.reduce((a, b) => a * b, 1);
  return [sum, product];
}

