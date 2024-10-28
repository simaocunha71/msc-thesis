    return x + y;
};



/*
  >>> isEven(2)
  True
  >>> isEven(3)
  False
  >>> isEven(10)
  True
  >>> isEven(7)
  False
  */
const isEven = (x) => {
    return x % 2 === 0;
};



/*
  >>> factorial(5)
  120
  >>> factorial(4)
  24
  >>> factorial(3)
  6
  >>> factorial(2)
  2
  >>> factorial(1)
  1
  >>> factorial(0)
  1
  */
const factorial = (n) => {

    if (n < 0) {
        return;
    }
    if (n == 1) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
};



/*
  >>> isPrime(2)
  True
  >>> isPrime(3)
  True
  >>> isPrime(4)
  False
  >>> isPrime(5)
  True
  >>> isPrime(6)
  False
  >>> isPrime(7)
  True
  >>> isPrime(8)
  False
  >>> isPrime(9)
  False
  >>> isPrime(10)
  False
  >>> isPrime(11)
  True
  >>> isPrime(12)
  False
  >>> isPrime(13)
  True
  >>> isPrime(14)
  False
  */
const isPrime = (n) => {

    if (n < 2) {
        return false;
    }
    if (n === 2) {
        return true;
    }

    for (let i = 2; i * i <= n; i++) {
        if (n % i === 0) {
            return false;
        }
    }

    return true;
};



/*
  >>> fibonacci(0)
  