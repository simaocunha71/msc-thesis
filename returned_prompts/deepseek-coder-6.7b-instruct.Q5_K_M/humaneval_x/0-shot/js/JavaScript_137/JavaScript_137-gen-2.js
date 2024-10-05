  if (typeof a === 'string') a = parseFloat(a.replace(',', '.'));
  if (typeof b === 'string') b = parseFloat(b.replace(',', '.'));

  if (a > b) return a;
  if (a < b) return b;
  return null;
}

console.log(compareOne(1, 2.5)); // 2.5
console.log(compareOne(1, "2,3")); // "2,3"
console.log(compareOne("5,1", 6)); // 6
console.log(compareOne("1", 1)); // null


*/


// Solution 
const compareOne = (a, b) => {

  if (typeof a === 'string') a = parseFloat(a.replace(',', '.'));
  if (typeof b === 'string') b = parseFloat(b.replace(',', '.'));

  if (a > b) return a;
  if (a < b) return b;
  return null;
}

console.log(compareOne(1, 2.5)); // 2.5
console.log(compareOne(1, "2,3")); // "2,3"
console.log(compareOne("5,1", 6)); // 6
console.log(compareOne("1", 1)); // null

// Here we've created a function that takes in two arguments, a and b. 
// We're checking if the types of a and b are strings. 
// If they are, we parse them into floats and replace the commas with periods for the float parsing. 
// Then, we compare the values of a and b. 
// If a is greater than b, we return a. If a is less than b, we return b. 
// If a and b are equal, we return null.






































































