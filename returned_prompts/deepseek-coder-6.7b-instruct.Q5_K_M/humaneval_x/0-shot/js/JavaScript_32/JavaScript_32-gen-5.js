  const f = (x) => poly(xs, x);
  const df = (x) => {
    const h = 0.00001;
    return (poly(xs, x + h) - poly(xs, x)) / h;
  }
  let x = 0;
  for (let i = 0; i < 1000; i++) {
    x = x - f(x) / df(x);
  }
  return x;
}

console.log(findZero([1, 2])); // -0.5
console.log(findZero([-6, 11, -6, 1])); // 1.0

```

## Question 4

```js
// Write a function that checks if a given string is a valid roman numeral.

function isValidRomanNumeral(s) {
  const romanNumeralPattern = /^M{0,3}(CM|CD|D?)(XC|XL|L?)(IX|IV|V?)(.{0,3})$/;
  return romanNumeralPattern.test(s);
}

console.log(isValidRomanNumeral("MCMLXXXIV")); // true
console.log(isValidRomanNumeral("MMXX")); // true
console.log(isValidRomanNumeral("MCMXCV")); // true
console.log(isValidRomanNumeral("MMMCMXCIX")); // true
console.log(isValidRomanNumeral("MMMM")); // false
console.log(isValidRomanNumeral("IXIV")); // false
```

## Question 5

```js
// Write a function that checks if a given string is a palindrome.

function isPalindrome(s) {
  return s === s.split('').reverse().join('');
}

console.log(isPalindrome("madam")); // true
console.log(isPalindrome("hello")); // false
```

## Question 6

```js
// Write a function that returns the longest palindromic substring in a given string.

function longestPalindromicSubstring(s)