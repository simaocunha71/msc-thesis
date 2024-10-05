  const isPrime = num => {
    for(let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++)
      if(num % i === 0) return false; 
    return num > 1;
  }

  let primeNumbers = [];
  for(let i = 2; i < n; i++){
    if(isPrime(i)){
      primeNumbers.push(i);
    }
  }
  return primeNumbers;
}

console.log(countUpTo(5)); // [2, 3]
console.log(countUpTo(11)); // [2, 3, 5, 7]
console.log(countUpTo(0)); // []
console.log(countUpTo(20)); // [2, 3, 5, 7, 11, 13, 17, 19]
console.log(countUpTo(1)); // []
console.log(countUpTo(18)); // [2, 3, 5, 7, 11, 13, 17]

/*Explanation:
The function "countUpTo" checks each number from 2 to n-1 to see if it is prime. It does this by using a helper function "isPrime" which checks if the number is prime by checking if it has any divisors other than 1 and itself. If the number is prime, it is added to the array primeNumbers. This array is then returned.
*/
























































































































































