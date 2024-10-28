  const isPrime = (n) => {
    if (n < 2) return false;
    for (let i = 2; i <= Math.sqrt(n); i++)
      if (n % i === 0) return false;
    return true;
  }

  const sumDigits = (n) => {
    let sum = 0;
    while (n) {
      sum += n % 10;
      n = Math.floor(n / 10);
    }
    return sum;
  }

  let maxPrime = -Infinity;
  for (let i = 0; i < lst.length; i++)
    if (isPrime(lst[i])) maxPrime = Math.max(maxPrime, lst[i]);

  return sumDigits(maxPrime);
}

console.log(skjkasdkd([0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3])) // 10
console.log(skjkasdkd([1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1])) // 25
console.log(skjkasdkd([1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3])) // 13
console.log(skjkasdkd([0,724,32,71,99,32,6,0,5,91,83,0,5,6])) // 11
console.log(skjkasdkd([0,81,12,3,1,21])) // 3
console.log(skjkasdkd([0,8,1,2,1,7])) // 7

```













