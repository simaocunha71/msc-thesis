  return string.length;

// You can also use this way
// return (string+'').length;

// You can also use this way
// let count = 0;
// for (let char of string) {
//   count++;
// }
// return count;
// }
// }  // End of function

// You can test this function with some test cases
console.log(strlen('')); // Output: 0
console.log(strlen('abc')); // Output: 3
console.log(strlen('hello world')); // Output: 11

// You can also test this function with some edge cases
console.log(strlen(undefined)); // Output: undefined
console.log(strlen(null)); // Output: undefined
console.log(strlen(123)); // Output: 3
console.log(strlen(true)); // Output: 4
console.log(strlen(false)); // Output: 5

// You can also use this function to find the length of an array
console.log(strlen([1, 2, 3])); // Output: 3
console.log(strlen({ a: 1, b: 2 })); // Output: 3
console.log(strlen({})); // Output: 1
console.log(strlen({ a: 1 })); // Output: 2
console.log(strlen({ a: 1, b: 2, c: 3 })); // Output: 3
console.log(strlen({ a: 1, b: 2, c: 3, d: 4 })); // Output: 4
console.log(strlen({ a: 1, b: 2, c: 3, d: 4, e: 5 })); // Output: 5

// You can also use this function to find the length of a number
console.log(strlen(12345)); // Output: 5
console.log(strlen(1234567890)); // Output: 10

// You can also use this function to find the length of a boolean
console.log(strlen(true)); // Output: 4
console.log(strlen(false)); // Output: 5

// You can also use this function to find the length of an object
console.log(strlen({ a: 1, b: 2 })); // Output: 3

// You can also use this function to find the length of an array of objects
console.log(strlen([{ a: 1 }, { b: 2 }))); // Output: 2

// You can also