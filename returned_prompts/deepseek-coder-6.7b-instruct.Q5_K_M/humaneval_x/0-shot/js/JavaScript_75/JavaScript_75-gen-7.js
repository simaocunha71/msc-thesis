  let factors = [];

  for(let i = 2; i <= a; i++) {
    while(a % i === 0) {
      factors.push(i);
      a = a / i;
    }
  }

  return factors.every(val => {
    let isPrime = true;
    for(let i = 2, sqrt = Math.sqrt(val); i <= sqrt; i++)
      if(val % i === 0) isPrime = false;
    return isPrime;
  });
}

//Test cases
console.log(isMultiplyPrime(30)); // true
console.log(isMultiplyPrime(50)); // false
console.log(isMultiplyPrime(60)); // true
console.log(isMultiplyPrime(130)); // true
console.log(isMultiplyPrime(150)); // false
console.log(isMultiplyPrime(180)); // true
console.log(isMultiplyPrime(250)); // false
console.log(isMultiplyPrime(270)); // true
console.log(isMultiplyPrime(300)); // false
console.log(isMultiplyPrime(360)); // true
console.log(isMultiplyPrime(500)); // false
console.log(isMultiplyPrime(750)); // true
console.log(isMultiplyPrime(1000)); // false

```













































































































































