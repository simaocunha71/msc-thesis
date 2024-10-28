  if(arr.length === 0) return null;
  let sum = 0;
  let signProduct = 1;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] < 0) signProduct *= -1;
    sum += Math.abs(arr[i]);
  }
  return sum * signProduct;
}

// Test cases
console.log(prodSigns([1, 2, 2, -4])); // Expected output: -9
console.log(prodSigns([0, 1])); // Expected output: 0
console.log(prodSigns([])); // Expected output: null

*/


// Solution:

function prodSigns(arr) {
  if(arr.length === 0) return null;
  let sum = 0;
  let signProduct = 1;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] < 0) signProduct *= -1;
    sum += Math.abs(arr[i]);
  }
  return sum * signProduct;
}

console.log(prodSigns([1, 2, 2, -4])); // Expected output: -9
console.log(prodSigns([0, 1])); // Expected output: 0
console.log(prodSigns([])); // Expected output: null


/*
  The function takes an array of integers as argument.
  If the array is empty, it returns null.
  Otherwise, it calculates the sum of absolute values of array elements,
  and the product of signs of array elements.
  Then, it returns the product of sum and product.
*/






































































































