let primes = [];

  for(let i = 2; i < n; i++) {
    if(isPrime(i)) {
      primes.push(i);
    }
  }

  return primes;
};

const isPrime = (num) => {
  for(let i = 2; i < num; i++)
    if(num % i === 0) return false;
  return num > 1;
}

console.log(countUpTo(5));
console.log(countUpTo(11));
console.log(countUpTo(0));
console.log(countUpTo(20));
console.log(countUpTo(1));
console.log(countUpTo(18));

```

