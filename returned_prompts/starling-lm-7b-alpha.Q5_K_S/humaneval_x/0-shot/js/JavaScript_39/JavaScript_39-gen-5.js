
const fib = (n) => {
  if (n <= 2) return 1;
  return fib(n - 1) + fib(n - 2);
};

while (true) {
  const num = fib(n);
  if (isPrime(num)) return num;
  n++;
}
};

function isPrime(num) {
  if (num <= 1) return false;
  if (num <= 3) return true;

  if (num % 2 === 0 || num % 3 === 0) return false;

  for (let i = 5; i * i <= num; i += 6) {
    if (num % i === 0 || num % (i + 2) === 0) return false;
  }

  return true;
}

console.log(primeFib(1)); // => 2
console.log(primeFib(2)); // => 3
console.log(primeFib(3)); // => 5
console.log(primeFib(4)); // => 13
console.log(primeFib(5)); // => 89







/*
  The function isPalindrome checks if a string is a palindrome.
  A palindrome is a string that is the same forwards and backwards.
  >>> isPalindrome("racecar")
  true
  >>> isPalindrome("hello")
  false
  >>> isPalindrome("madam")
  true
  >>> isPalindrome("rotator")
  false
  >>> isPalindrome("level")
  true
  >>> isPalindrome("banana")
  true
  >>> isPalindrome("orange")
  false
  */

function isPalindrome(str) {
  let i = 0;
  let j = str.length - 1;
  while (i < j) {
    if (str[i] !== str[j]) {
      return false;
    }
    i++;
    j--;
  }
  return true;
}

console.log(isPalindrome("r