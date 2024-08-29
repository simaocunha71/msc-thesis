  let sum = 0;
  let product = 1;

  for (const i of numbers) {
    sum += i;
    product *= i;
  }

  return (sum, product);
}



