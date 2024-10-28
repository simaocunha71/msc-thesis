  const isPrime = (num) => {
    for(let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++)
      if(num % i === 0) return false; 
    return num > 1;
  }

  return isPrime(string.length);
}

console.log(primeLength('Hello')) // true
console.log(primeLength('abcdcba')) // true
console.log(primeLength('kittens')) // true
console.log(primeLength('orange')) // false

// The function isPrime checks if a number is a prime number or not.
// It does so by checking if the number has any divisors in the range from 2 to the square root of the number.
// If it has, it returns false. If not, it returns true.
// The function primeLength first calculates the length of the string using the string.length property.
// It then passes this length to the isPrime function to check if it is a prime number or not.
// If it is, it returns true. If not, it returns false.

// The function primeLength then returns the result of this check.
// It does this using the return statement.
// The console.log statements are used to test the function with the given examples.
// They print out the result of calling primeLength with the given string.
// If the result is true, it means that the length of the string is a prime number.
// If the result is false, it means that the length of the string is not a prime number.

// The function primeLength is a pure function because it always returns the same result for the same input.
// It does not have any side effects, it does not modify any global state or change any external variables.
// It only depends on the input to calculate its output.
// Therefore, it can be easily tested and verified.

// The function primeLength is a high-order function because it takes another function as an argument and returns a function as a result.
// In this case, it takes the isPrime function as an argument and returns a new function that uses it to check if a string's length is a prime number.
// This allows it to be easily reused in other parts of the program.