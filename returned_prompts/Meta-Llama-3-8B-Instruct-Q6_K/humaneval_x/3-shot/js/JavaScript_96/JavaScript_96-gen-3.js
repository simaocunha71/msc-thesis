  let result = [];
  for (let i = 2; i < n; i++) {
    if (isPrime(i)) {
      result.push(i);
    }
  }
  return result;

  function isPrime(num) {
    if (num <= 1) {
      return false;
    }
    for (let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++) {
      if (num % i === 0) {
        return false;
      }
    }
    return true;
  }
}  // This function works, but it's not very efficient. It checks divisibility for all numbers up to the square root of n. We can improve this by only checking up to the square root of n. The function also checks if the number is less than or equal to 1, which is not necessary because it returns false in that case. We can simplify this function to check if the number is divisible by any number up to its square root. We can also use a for loop instead of a while loop for the same reason. Here is the simplified function: 
function isPrime(num) {
  if (num <= 1) return false;
  for (let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++) {
    if (num % i === 0) return false;
  }
  return true;
}  // We can further simplify this function by using the Math.floor function to round down the square root. This can be done by changing sqrt = Math.sqrt(num) to sqrt = Math.floor(Math.sqrt(num)). Here is the simplified function: 
function isPrime(num) {
  if (num <= 1) return false;
  for (let i = 2, sqrt = Math.floor(Math.sqrt(num)); i <= sqrt; i++) {
    if (num % i === 0) return false;
  }
  return true;
}  // This function is now more efficient and easier to read. It checks if a number is prime by checking if it's divisible by any number up to its square root. It returns false if the number is divisible, and true if it's not. This function can be used in the countUpTo function to return an array of the first n integers that are prime numbers and less than n. 
function countUpTo(n) {
  let result = [];
  for (let i = 2; i < n; i++) {
    if (isPrime(i