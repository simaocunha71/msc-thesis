  const isPrime = (num) => {
    for(let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++)
      if(num % i === 0) return false; 
    return num > 1;
  }

  const primes = [];
  for(let i = 2; i < n; i++){
    if(isPrime(i)) primes.push(i);
  }
  return primes;
}

console.log(countUpTo(5)); //[2, 3]
console.log(countUpTo(11)); //[2, 3, 5, 7]
console.log(countUpTo(0)); //[]
console.log(countUpTo(20)); //[2, 3, 5, 7, 11, 13, 17, 19]
console.log(countUpTo(1)); //[]
console.log(countUpTo(18)); //[2, 3, 5, 7, 11, 13, 17]
```

## 1.2.3. Prime Numbers Checker

```javascript
