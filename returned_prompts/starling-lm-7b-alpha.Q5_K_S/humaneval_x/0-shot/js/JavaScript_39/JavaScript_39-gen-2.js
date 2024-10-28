  let fib = [2, 3];
  let i = 3;
  let j = 0;
  let k = 1;
  while (j < n) {
    let l = fib[i] + fib[j];
    if (isPrime(l)) {
      fib.push(l);
      if (fib[i] === fib[j]) {
        i++;
      }
      j++;
      k++;
    } else {
      j++;
      k++;
    }
  }
  return fib[n];
};

const isPrime = (num) => {
  for (let i = 2; i < num; i++) {
    if (num % i === 0) {
      return false;
    }
  }
  return true;
};

module.exports = {
  primeFib
};



/*
  The task is to write a function primeFib that takes an integer n as input and returns the nth number in the sequence of Fibonacci numbers that is also prime. The first number in this sequence is 2, the second is 3, the third is 5, the fourth is 13, and so on.

  Here are some test cases to help you get started:

  primeFib(1) should return 2.
  primeFib(2) should return 3.
  primeFib(3) should return 5.
  primeFib(4) should return 13.
  primeFib(5) should return 89.
*/















































































































































