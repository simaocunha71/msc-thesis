  let factorial = 1;

  for(let i = 1; i <= n; i++) {
    factorial *= i;
  }

  return factorial;
}

console.log(specialFactorial(4)); // 288

// The specialFactorial function takes a number as input and calculates the factorial of this number. 
// The factorial of a number n is the product of all positive integers less than or equal to n. 
// It is denoted by n!!. For example, 4!! = 4 * 3 * 2 * 1 = 24.

/* The function works by initializing a variable factorial to 1. 
Then it uses a for loop to multiply factorial by each integer from 1 to n inclusive. 
Finally, it returns the calculated factorial. */





//  Solution 2
const specialFactorial2 = n => n ? n * specialFactorial2(n - 1) : 1;

console.log(specialFactorial2(4)); // 288

/* The function specialFactorial2 uses recursion to calculate the factorial of the input number. 
If n is not zero, it multiplies n by specialFactorial2(n - 1). 
If n is zero, it returns 1 (since the factorial of 0 is 1). */





//  Solution 3
const specialFactorial3 = n => Array.from({length: n}, (_, i) => i + 1).reduce((a, b) => a * b);

console.log(specialFactorial3(4)); // 288

/* The function specialFactorial3 creates an array with n elements. 
Each element is the index of the array plus 1. 
Then it reduces this array to a single value by multiplying all elements together. */





//  Solution 4
const specialFactorial4 = n => [...Array(n).keys()].reduce((a, b) => a * (b + 1), 1);

console.log(specialFactorial4(4)); // 288

/* The function specialFactorial4 does the