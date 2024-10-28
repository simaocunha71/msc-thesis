  return (
    typeof(x) === "number" &&
    typeof(y) === "number" &&
    typeof(z) === "number" &&
    [x, y, z].some(v => v === Math.floor(x + y + z - v))
  );
};

console.log(anyInt(5, 2, 7)); // true
console.log(anyInt(3, 2, 2)); // false
console.log(anyInt(3, -2, 1)); // true
console.log(anyInt(3.6, -2.2, 2)); // false

This solution works by first checking if the inputs are all numbers. Then it calculates the sum of the three numbers and subtracts the value of the current number being checked from it. If this value is equal to one of the other numbers, the function returns true. If it doesn't find any such number, it returns false. The Math.floor function is used to ensure that the sum is an integer.
*/

const anyInt = (x, y, z) => {
  return (
    typeof(x) === "number" &&
    typeof(y) === "number" &&
    typeof(z) === "number" &&
    [x, y, z].some(v => v === Math.floor(x + y + z - v))
  );
};

console.log(anyInt(5, 2, 7)); // true
console.log(anyInt(3, 2, 2)); // false
console.log(anyInt(3, -2, 1)); // true
console.log(anyInt(3.6, -2.2, 2)); // false




















































































































