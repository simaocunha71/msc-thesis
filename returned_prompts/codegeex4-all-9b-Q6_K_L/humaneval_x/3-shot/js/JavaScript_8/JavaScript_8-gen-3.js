  let sum = 0;
  let product = 1;
  for (const n of numbers) {
    sum += n;
    product *= n;
  }
  return (sum, product);
}

