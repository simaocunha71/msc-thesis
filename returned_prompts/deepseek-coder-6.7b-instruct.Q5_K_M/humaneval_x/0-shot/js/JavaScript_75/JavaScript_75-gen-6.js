
    // Function to check if a number is prime
    const isPrime = (num) => {
        for(let i = 2; i < num; i++)
            if(num % i === 0) return false;
        return num > 1;
    }

    // Function to calculate the number of primes in the multiplication
    const numPrimes = (num) => {
        let count = 0;
        for(let i = 2; i <= num; i++) {
            if(num % i === 0 && isPrime(i)) {
                count++;
                while(num % i === 0) {
                    num /= i;
                }
            }
        }
        return count;
    }

    return numPrimes(a) === 3;

};

console.log(isMultiplyPrime(30)) // true
console.log(isMultiplyPrime(100)) // false
console.log(isMultiplyPrime(30030)) // true

/*
  The function isMultiplyPrime works by first checking if a number is prime. 
  If the number is prime, it increments a count.
  The function numPrimes calculates the number of distinct primes in a given number.
  We then check if the number of primes in the number is equal to 3.
  If it is, we return true, otherwise we return false.
*/

```











































































































































































