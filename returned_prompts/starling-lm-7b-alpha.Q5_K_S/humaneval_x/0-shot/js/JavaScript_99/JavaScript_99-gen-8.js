const number = parseFloat(value);

const integer = Math.round(number);

if (number > 0 && number - integer > 0.5) {
  return integer + 1;
} else if (number < 0 && integer - number > 0.5) {
  return integer - 1;
}

return integer;
};

// Tests
console.log(closestInteger("10"));  // 10
console.log(closestInteger("15.3"));  // 15
console.log(closestInteger("-14.5"));  // -15

*/

*/

const closestInteger = (value) => {
  const number = parseFloat(value);
  const integer = Math.round(number);
  if (number > 0 && number - integer >