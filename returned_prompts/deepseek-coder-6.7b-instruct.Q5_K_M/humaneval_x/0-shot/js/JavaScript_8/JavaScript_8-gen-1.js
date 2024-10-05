let sum = 0;
let product = 1;

for (let i = 0; i < numbers.length; i++) {
  sum += numbers[i];
  product *= numbers[i];
}

return (sum, product);
}
*/

const sumProduct = (numbers) => {

  let sum = 0;
  let product = 1;

  for (let i = 0; i < numbers.length; i++) {
    sum += numbers[i];
    product *= numbers[i];
  }

  return (sum, product);
}

console.log(sumProduct([1, 2, 3, 4]));
console.log(sumProduct([]));
console.log(sumProduct([5, 3, 1]));
console.log(sumProduct([10, 20, 30]));
console.log(sumProduct([2, 5, 6]));

// Test cases
// sumProduct([1, 2, 3, 4]) should return (10, 24)
// sumProduct([]) should return (0, 1)
// sumProduct([5, 3, 1]) should return (9, 15)
// sumProduct([10, 20, 30]) should return (60, 6000)
// sumProduct([2, 5, 6]) should return (13, 60)

// This solution will work for any array of numbers.
// If the array is empty, the sum will be 0 and the product will be 1.
// If the array contains numbers, the function will calculate the sum and the product of all numbers in the array.













































































































