```java
const primeFib = (n) => {
  var isPrime = function (num) {
    if (num <= 1) return false;
    for (let i = 2; i <= Math.sqrt(num); i++) {
      if (num % i === 0) return false;
    }
    return true;
  };

  var fib = function (num) {
    if (num <= 1) return num;
    return fib(num - 1) + fib(num - 2);
  };

  var count = 0;
  var i = 0;
  while (count < n) {
    var value = fib(i);
    if (isPrime(value)) count++;
    if (count === n) return value;
    i++;
  }
}
```
