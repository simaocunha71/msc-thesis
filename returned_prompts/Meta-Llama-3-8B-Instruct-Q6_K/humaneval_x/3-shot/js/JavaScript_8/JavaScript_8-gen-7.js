  let sum = 0;
  let product = 1;

  for (let i of numbers) {
    sum += i;
    product *= i;
  }

  return [sum, product];
}  // or return (sum, product) if you prefer a tuple. It depends on the language you are using.