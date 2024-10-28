  const fib = (n) => {
    let a = 1, b = 1;
    for (let i = 3; i <= n; i++) {
      [a, b] = [b, a + b];
    }
    return b;
  }

  const isPrime = (n) => {
    for(let i = 2, sqrt = Math.sqrt(n); i <= sqrt; i++)
      if(n % i === 0) return false; 
    return n > 1;
  }

  let count = 0;
  let i = 1;
  
  while(count < n){
    if(isPrime(fib(i))){
      count++;
    }
    i++;
  }
  return fib(i-1);
}

console.log(primeFib(1)); // 2
console.log(primeFib(2)); // 3
console.log(primeFib(3)); // 5
console.log(primeFib(4)); // 13
console.log(primeFib(5)); // 89
```

- 위의 코드에서 우선 피보나치 수를 계산하는 함수 `fib(n)`을 만들었다.
- 그리고 피보나치 수가 소수인지 확인하는 함수 `isPrime(n)`을 만들었다.
- `primeFib(n)` 함수는 `n`번째 소수 피보나치 수를 반환한