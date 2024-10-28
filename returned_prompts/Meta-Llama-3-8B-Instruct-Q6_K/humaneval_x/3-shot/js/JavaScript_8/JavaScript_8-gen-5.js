  let sum = 0;
  let product = 1;
  for (let n of numbers) {
    sum += n;
    product *= n;
  }
  return [sum, product];
} // Note: This function doesn't take any argument other than the list of numbers. If you want to handle the case of an empty list, you can add a check at the beginning of the function. For example: if (numbers.length === 0) return [0, 1]; // Return default values for sum and product.