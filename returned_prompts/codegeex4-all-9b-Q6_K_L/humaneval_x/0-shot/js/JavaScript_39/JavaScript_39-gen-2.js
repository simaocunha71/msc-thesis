```java
const primeFib = (n) => {
  const isPrime = (num) => {
    if (num <= 1) return false;
    for (let i = 2; i <= Math.sqrt(num); i++) {
      if (num % i === 0) return false;
    }
    return true;
  };

  let fibSeq = [0, 1];
  let primeFibSeq = [];

  while (primeFibSeq.length < n) {
    let nextFib = fibSeq[fibSeq.length - 1] + fibSeq[fibSeq.length - 2];
    fibSeq.push(nextFib);
    if (isPrime(nextFib)) {
      primeFibSeq.push(nextFib);
    }
  }

  return primeFibSeq[primeFibSeq.length - 1];
}
```
