  return lst.map(x => x.split('').filter(y => y % 2 !== 0).length);
};

console.log(oddCount(['1234567'])); // [4]
console.log(oddCount(['3',"11111111"])); // [1, 8]
```

## 2. FizzBuzz

Write a program that prints the numbers from 1 to 100. But for multiples of three, print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.

```javascript
const fizzBuzz = () => {
  for (let i = 1; i <= 100; i++) {
    if (i % 15 === 0) {
      console.log('FizzBuzz');
    } else if (i % 3 === 0) {
      console.log('Fizz');
    } else if (i % 5 === 0) {
      console.log('Buzz');
    } else {
      console.log(i);
    }
  }
};

fizzBuzz();
```

## 3. Palindrome

Write a function that checks if a given word or phrase is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward, ignoring spaces, punctuation, and capitalization.

```javascript
const palindrome = (str) => {
  let sanitizeStr = str.toLowerCase().replace(/[^a-z0-9]/gi, '');
  let reverseStr = sanitizeStr.split('').reverse().join('');
  return sanitizeStr === reverseStr;
};

console.log(palindrome('racecar')); // true
console.log(palindrome('hello')); // false
```

## 4. Factorial

Write a function that calculates the factorial of a number. The factorial of a number is the product of all positive integers less than or equal to that number.