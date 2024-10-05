  let length = string.length;

  for (let i = 2; i < length; i++) {
    if (length % i === 0) {
      return false;
    }
  }
  return true;
};

primeLength('Hello'); // true
primeLength('abcdcba'); // true
primeLength('kittens'); // true
primeLength('orange'); // false

*/





/*
  Write a function that takes a string as an argument and returns the length of the string
  Examples:
  lengthString('Hello') == 5
  lengthString('abcdcba') == 7
  lengthString('kittens') == 7
  lengthString('orange') == 6


  */


const lengthString = (string) => {
  return string.length;
};

lengthString('Hello'); // 5
lengthString('abcdcba'); // 7
lengthString('kittens'); // 7
lengthString('orange'); // 6


/*
  Write a function that takes a string as an argument and returns the last character of the string
  Examples:
  lastChar('Hello') == 'o'
  lastChar('abcdcba') == 'a'
  lastChar('kittens') == 's'
  lastChar('orange') == 'e'


  */

const lastChar = (string) => {
  return string[string.length - 1];
};

lastChar('Hello'); // 'o'
lastChar('abcdcba'); // 'a'
lastChar('kittens'); // 's'
lastChar('orange'); // 'e'


/*
  Write a function that takes a string as an argument and returns true if the string is a palindrome, otherwise returns false
  Examples:
  palindrome('abba') == true
  palindrome('abcde') == false
  palindrome('kayak') == true
  palindrome('orange') == false

  */

const palindrome = (string) => {
  let reversed = string.split('').reverse().join('');
 