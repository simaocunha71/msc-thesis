  let sum = 0;
  let product = 1;
  for (let n of numbers) {
    sum += n;
    product *= n;
  }
  return [sum, product];
}
// or
const sumProduct = (numbers) => {
  let sum = 0;
  let product = 1;
  for (let n of numbers) {
    sum += n;
    product *= n;
  }
  return [sum, product];
} // Note: You can remove int parameter as it is not used in your function.



