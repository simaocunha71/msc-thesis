  let sum = 0;
  let product = 1;

  for (let i = 0; i < numbers.length; i++) {
    sum += numbers[i];
    product *= numbers[i];
  }

  return [sum, product];
} // Not sure why there is an extra argument 'int' in the function definition. It seems to be unused.