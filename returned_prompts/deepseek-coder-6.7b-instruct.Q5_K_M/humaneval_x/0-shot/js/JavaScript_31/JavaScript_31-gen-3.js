  if (n < 2) {
    return false;
  }
  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0) {
      return false;
    }
  }
  return true;
}

module.exports = isPrime;

//Explanation:
//The function first checks if the number is less than 2. If it is, the function returns false because numbers less than 2 are not prime.
//Then, the function sets up a for loop to check if the number is divisible by any numbers up to the square root of the number. This is because a larger factor of the number would be a multiple of some smaller factor that has already been checked.
//If the number is divisible by any of these smaller factors, the function returns false because the number is not prime. If the number is not divisible by any of these smaller factors, the function returns true because the number is prime.
//The Math.sqrt function is used to limit the range of potential factors to check, as any factor larger than the square root would have a corresponding factor smaller than the square root.
//The modulo operator (%) is used to check for divisibility. If n % i is equal to 0, then n is divisible by i and the function returns false. Otherwise, the function returns true after checking all possible factors up to the square root of n.

//