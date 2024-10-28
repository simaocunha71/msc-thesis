  const fib = (n) => {
    let arr = [0, 1];
    for(let i = 2; i <= n; i++) {
      arr.push(arr[i - 2] + arr[i - 1]);
    }
    return arr[n];
  }

  const isPrime = (num) => {
    for(let i = 2; i <= Math.sqrt(num); i++)
      if(num % i === 0) return false;
    return num > 1;
  }

  let count = 0;
  let i = 1;
  while (count < n) {
    if(isPrime(fib(i))) {
      count++;
    }
    i++;
  }
  return fib(i - 1);
}

console.log(primeFib(1)); // 2
console.log(primeFib(2)); // 3
console.log(primeFib(3)); // 5
console.log(primeFib(4)); // 13
console.log(primeFib(5)); // 89
```

### Problem 3:

