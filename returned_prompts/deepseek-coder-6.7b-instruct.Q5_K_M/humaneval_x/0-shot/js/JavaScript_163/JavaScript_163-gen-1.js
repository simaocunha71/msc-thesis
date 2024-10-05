  let result = [];
  let start = Math.min(a, b);
  let end = Math.max(a, b);

  for(let i = start; i <= end; i++){
    if (i % 2 === 0) {
      result.push(i);
    }
  }

  return result;
}


console.log(generateIntegers(2, 8)); // => [2, 4, 6, 8]
console.log(generateIntegers(8, 2)); // => [2, 4, 6, 8]
console.log(generateIntegers(10, 14)); // => []

*/

// SOLUTION:

const generateIntegers = (a, b) => {
  let result = [];
  let start = Math.min(a, b);
  let end = Math.max(a, b);

  for(let i = start; i <= end; i++){
    if (i % 2 === 0) {
      result.push(i);
    }
  }

  return result;
}

console.log(generateIntegers(2, 8)); // => [2, 4, 6, 8]
console.log(generateIntegers(8, 2)); // => [2, 4, 6, 8]
console.log(generateIntegers(10, 14)); // => []

/*
The function generateIntegers() takes two parameters a and b and returns an array of even numbers in ascending order between a and b.

The function first determines the smaller of the two numbers by using Math.min() and assigns it to start. It then finds the larger number using Math.max() and assigns it to end.

Then it creates an empty array result to store the even numbers.

It then starts a loop that goes from start to end (inclusive). If a number is even (i % 2 === 0), it pushes it to the result array.

Finally, it returns the result array.
*/

// Time complexity: O(n)
// Space complexity: O(n)

// n is the distance between a