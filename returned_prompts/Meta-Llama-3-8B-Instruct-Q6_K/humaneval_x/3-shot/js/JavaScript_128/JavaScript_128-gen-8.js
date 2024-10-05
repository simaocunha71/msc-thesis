  if (arr.length === 0) {
    return null;
  }
  let productSign = 1;
  let sumMagnitude = 0;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] < 0) {
      productSign *= -1;
    }
    sumMagnitude += Math.abs(arr[i]);
  }
  return productSign * sumMagnitude;
}
// You can use Math.sign() instead of checking the sign yourself
const prodSigns = (arr) => {
  if (arr.length === 0) {
    return null;
  }
  let productSign = Math.exp(arr.reduce((a, b) => a + Math.log(Math.abs(b)), 0));
  return productSign * arr.reduce((a, b) => a + Math.abs(b), 0);
};
// or even more concise with reduce()
const prodSigns = (arr) => {
  if (arr.length === 0) {
    return null;
  }
  return Math.exp(arr.reduce((a, b) => a + Math.log(Math.abs(b)), 0)) * arr.reduce((a, b) => a + Math.abs(b), 0);
};