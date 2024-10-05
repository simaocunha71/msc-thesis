  const isPrime = (num) => {
    for(let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++)
      if(num % i === 0) return false; 
    return num > 1;
  }

  let primes = [];
  for(let i = 2; i < n; i++){
    if(isPrime(i)) primes.push(i);
  }
  return primes;
}

console.log(countUpTo(5)); // [2, 3]
console.log(countUpTo(11)); // [2, 3, 5, 7]
console.log(countUpTo(0)); // []
console.log(countUpTo(20)); // [2, 3, 5, 7, 11, 13, 17, 19]
console.log(countUpTo(1)); // []
console.log(countUpTo(18)); // [2, 3, 5, 7, 11, 13, 17]

//The function isPrime is a helper function that checks if a given number is a prime number. It does so by iterating from 2 to the square root of the number, and checking if the number is divisible by any of these numbers. If it is divisible, it returns false, indicating that the number is not a prime. If it is not divisible by any of these numbers, it returns true, indicating that the number is a prime.

//The main function countUpTo takes an integer n as its argument. It initializes an empty array primes to store the prime numbers. It then iterates from 2 to n (not inclusive), and for each number, it checks if the number is a prime. If it is a prime, it adds the number to the primes array. Finally, it returns the primes array.

//This solution has a time complexity of O(n*sqrt(n)), as for each number up to n, it checks if it is a prime by iterating up to the square root of that number. The space complexity is O(n), as in the worst case, all numbers up to n are prime and stored in the pr