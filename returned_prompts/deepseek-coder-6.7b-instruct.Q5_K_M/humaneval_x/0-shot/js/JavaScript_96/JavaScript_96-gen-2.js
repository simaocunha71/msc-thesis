let primes = [];

const isPrime = (num) => {
  for(let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++)
    if(num % i === 0) return false; 
  return num > 1;
}

for(let i = 2; i < n; i++){
  if(isPrime(i)){
    primes.push(i);
  }
}

return primes;
}

console.log(countUpTo(5));
console.log(countUpTo(11));
console.log(countUpTo(0));
console.log(countUpTo(20));
console.log(countUpTo(1));
console.log(countUpTo(18));

The function isPrime checks if a number is prime by iterating from 2 to the square root of the number,
and checks if the number is divisible by any of the numbers in this range. If it is, the function returns false,
indicating that the number is not prime. If the number is not divisible by any of the numbers in this range, the function returns true.
The function countUpTo iterates from 2 up to n (exclusive), and checks if each number is prime. If it is, it is added to the primes array. Finally, the function returns the primes array.


A: Here's a simple way to do this using JavaScript:

```javascript
function countUpTo(n) {
    let primes = [];

    function isPrime(num) {
        for(let i = 2; i < num; i++)
            if(num % i === 0) return false;
        return num > 1;
    }

    for(let i = 2; i < n; i++)
        if(isPrime(i)) primes.push(i);

    return primes;
}

console.log(countUpTo(5));  // [2, 3]
console.log(countUpTo(11)); // [2, 3, 5, 7]
console.log(countUpTo(0));  // []
console.log(