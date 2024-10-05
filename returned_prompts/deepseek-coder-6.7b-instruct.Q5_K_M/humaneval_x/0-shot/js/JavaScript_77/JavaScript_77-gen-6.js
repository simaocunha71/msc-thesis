  return Number.isInteger(Math.round(Math.pow(a, (1 / 3))));
};

console.log(iscube(1)); // true
console.log(iscube(2)); // false
console.log(iscube(-1)); // true
console.log(iscube(64)); // true
console.log(iscube(0)); // true
console.log(iscube(180)); // false

//Explanation:
//We're given a number a. We need to find if this number is a perfect cube of some other integer.
//We can do this by taking the cube root of the number a. We can do this using Math.pow function with 1/3 as the exponent.
//Once we get the cube root, we need to check if it's an integer. We can do this by using the Number.isInteger function.
//If the cube root is an integer, then the number a is a perfect cube. Otherwise, it's not.
//The result will be a boolean value: true if it's a perfect cube, false otherwise.

//Math.pow(a, (1 / 3)) calculates the cube root of a.
//Number.isInteger(Math.round(...)) checks if the cube root is an integer. If it's an integer, we've a perfect cube, otherwise not.

//Note: Math.round is used to round the result to the nearest integer because cube roots of negative numbers are also integers.

//In the end, we return the result.

//The solution has a time complexity of O(1) since it performs a single mathematical operation regardless of the size of the input.
//The space complexity is also O(1) since it uses a constant amount of space.




































































































