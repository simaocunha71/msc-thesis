let result = [];
for(let i = 1; i <= n; i++) {
  if(i % 2 == 0) {
    result.push(fact(i));
  } else {
    result.push(sum(i));
  }
}
return result;

};

const sum = (n) => {
  let sum = 0;
  for(let i = 1; i <= n; i++) {
    sum += i;
  }
  return sum;
};

const fact = (n) => {
  let result = 1;
  for(let i = 1; i <= n; i++) {
    result *= i;
  }
  return result;
};

f(5);

/*
  Expected output:
  [1, 2, 6, 24, 15]

  Here's how it works:
  - We start by initializing an empty array result.
  - We start a for loop, with i ranging from 1 to n.
  - For each iteration of the loop, we check if i is even with i % 2 == 0.
    - If it is, we push the factorial of i in the result array.
    - If it's not, we push the sum of all numbers from 1 to i in the result array.
  - After the loop is finished, we return the result array.

  Note: The sum and fact functions are defined below the f function.
  - The sum function computes the sum of all numbers from 1 to n.
  - The fact function computes the factorial of a number.
*/

*/

// To check your solution, you can use the following code:
console.log(f(5));  // [1, 2, 6, 24, 15]
















































































