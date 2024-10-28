```javascript
const isPrime = (num) => {
  if (num <= 1) return false;
  for (let i = 2; i < num; i++) {
    if (num % i === 0) return false;
  }
  return true;
};

const countUpTo = (n) => {
  const result = [];
  for (let i = 2; i < n; i++) {
    if (isPrime(i)) result.push(i);
  }
  return result;
};
```