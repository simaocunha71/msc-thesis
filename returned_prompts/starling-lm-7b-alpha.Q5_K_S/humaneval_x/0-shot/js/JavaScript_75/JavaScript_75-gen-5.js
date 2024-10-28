    const isPrime = (n) => {
      for (let i = 2; i < n; i++) {
        if (n % i === 0) {
          return false;
        }
      }
      return true;
    };
    if (a < 100) {
      let result = true;
      let counter = 0;
      while (result && counter < 3) {
        let index = Math.floor(Math.random() * a);
        if (isPrime(index)) {
          result = result && index;
          counter++;
        }
      }
      return result;
    }
    return false;
  };




/* Write a function that returns true if the given number is the multiplication of 3 prime numbers
  and false otherwise.
  Knowing that (a) is less then 100.
  Example:
  isMultiplyPrime(30) == true
  30 = 2 * 3 * 5
  */


const isMultiplyPrime = (a) => {
    const isPrime = (n) => {
      for (let i = 2; i < n; i++) {
        if (n % i === 0) {
          return false;
        }
      }
      return true;
    };
    if (a < 100) {
      let result = true;
      let counter = 0;
      while (result && counter < 3) {
        let index = Math.floor(Math.random() * a);
        if (isPrime(index)) {
          result = result && index;
          counter++;
        }
      }
      return result;
    }
    return false;
  };

  

  console.log(isMultiplyPrime(30)); // true
  console.log(isMultiplyPrime(31)); // false
  console.log(isMultiplyPrime(20)); // false

  // console.log(isMultiplyPrime(3)); // true
  // console.log(isMultiplyPrime(4)); // false
