  let b = Math.cbrt(a);
  return Math.round(b) === b;
};

/*
  Write a function that takes an integer a and returns true if
  this integer is a prime number. A prime number is an integer
  with exactly two distinct positive divisors: 1 and itself.
  Note: you may assume the input is always valid.
  Examples:
  isPrime(0) ==> false
  isPrime(2) ==> true
  isPrime(3) ==> true
  isPrime(4) ==> false
  isPrime(5) ==> true
  isPrime(6) ==> false
  isPrime(7) ==> true
  isPrime(8) ==> false
  isPrime(9) ==> false
  isPrime(10) ==> false
  isPrime(11) ==> true
  isPrime(12) ==> false
  isPrime(13) ==> true
  isPrime(14) ==> false
  isPrime(15) ==> false
  isPrime(16) ==> false
  isPrime(17) ==> true
  isPrime(18) ==> false
  isPrime(19) ==> true
  isPrime(20) ==> false
  isPrime(21) ==> false
  isPrime(22) ==> false
  isPrime(23) ==> true
  isPrime(24) ==> false
  isPrime(25) ==> false
  isPrime(26) ==> false
  isPrime(27) ==> false
  isPrime(28) ==> false
  isPrime(29) ==> true
  isPrime(30) ==> false
  isPrime(31) ==> true
  isPrime(32) ==> false
  isPrime(33) ==> false
  isPrime(34) ==> false
  isPrime(35) ==> false
  isPrime(36) ==> false
  isPrime(37) ==> true
  isPrime(38) ==> false
  isPrime(39) ==> false
 