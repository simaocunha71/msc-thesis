  let num = parseFloat(value);
  return (num < 0) ? Math.floor(num - 0.5) : Math.floor(num + 0.5);

};

console.log(closestInteger("10")); // 10
console.log(closestInteger("15.3")); // 15
console.log(closestInteger("14.5")); // 15
console.log(closestInteger("-14.5")); // -15

*/

//  Solution:

const closestInteger = (value) => {
  let num = parseFloat(value);
  return (num < 0) ? Math.floor(num - 0.5) : Math.floor(num + 0.5);
};

console.log(closestInteger("10")); // 10
console.log(closestInteger("15.3")); // 15
console.log(closestInteger("14.5")); // 15
console.log(closestInteger("-14.5")); // -15

//  The function works by parsing the value string to a floating-point number. Then it rounds this number to the nearest integer. If the number is negative, it subtracts 0.5 before rounding, otherwise it adds 0.5. This effectively rounds away from zero if the number is equidistant from two integers.

//  Finally, the result is returned.

//  Note: The function assumes that the input value string can be parsed to a floating-point number. If this is not the case, the function may not work as expected.

//  Also note that this function uses the Math.floor function to round the number, which always rounds down. This means that if the number is equidistant from two integers, it rounds towards zero.

/*
closestInteger("10") returns 10
closestInteger("15.3") returns 15
closestInteger("14.5") returns 15
closestInteger("-14.5") returns -15
*/

//  This function works as expected and is a simple way to round a string representing a number to the nearest integer.
//  It handles positive and negative