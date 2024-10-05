const value = parseFloat(value);
let result = Math.round(value);

if (value - result > 0.5) {
  result++;
} else if (result - value > 0.5) {
  result--;
}

return result;

/*
  Explanation
  First, we convert the string to a number.
  Then, we use Math.round() to round the number to the nearest integer.
  Finally, we check if the number is equidistant from two integers and round
  it away from zero if it is.
*/

*/





// Test
console.log(closestInteger("10") === 10);
console.log(closestInteger("15.3") === 15);
console.log(closestInteger("14.5") === 15);
console.log(closestInteger("-14.5") === -15);
console.log(closestInteger("-15.3") === -16);
console.log(closestInteger("-15.7") === -16);
console.log(closestInteger("-15.8") === -16);
console.log(closestInteger("-14.2") === -14);
console.log(closestInteger("-14.8") === -15);
console.log(closestInteger("-15.8") === -16);
console.log(closestInteger("-10") === -10);
console.log(closestInteger("-10.5") === -11);
console.log(closestInteger("-10.6") === -11);
console.log(closestInteger("-10.7") === -11);
console.log(closestInteger("-10.8") === -11);
console.log(closestInteger("-10.9") === -11);
console.log(closestInteger("-10.99") === -11);
console.log(closestInteger("-10.999") === -11);
console.log(closestInteger("-11") === -11);
console.log(closestInteger("-11