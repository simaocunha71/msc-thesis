  if (string === '') return '';
  
  let end = string.length;
  let reversed = string.split('').reverse().join('');
  
  while (end > 0) {
    if (isPalindrome(string.slice(0, end))) {
      return string + reversed.slice(string.length - end);
    }
    end--;
  }
  
  return string + reversed;
}
```

## Task 2 - Palindrome Checker

### Description

Create a function that accepts a string and returns true if the string is a palindrome, false if it is not. A palindrome is a word that reads the same backward as forward.

### Examples

```javascript
isPalindrome('madam') // returns true
isPalindrome('hello') // returns false
```

### Solution

```javascript
const isPalindrome = (string) => {
  return string === string.split('').reverse().join('');
}
```

## Task 3 - Find the Longest Palindromic Substring

### Description

Write a function that accepts a string and returns the longest palindromic substring.

### Examples

```javascript
longestPalindrome('madam') // returns 'madam'
longestPalindrome('hello') // returns 'h'
```

### Solution

```javascript
const longestPalindrome = (string) => {
  let longest = '';
  
  for (let i = 0; i < string.length; i++) {
    let oddPalindrome = getPalindrome(string, i, i);
    let evenPalindrome = getPalindrome(string, i, i + 1);
    let currentLongest = oddPalindrome.length > evenPalindrome.length ? oddPalindrome : evenPalindrome;
    
    longest = currentLongest.length > longest.length ? currentLongest : longest;
  }
  
  return longest;
}

const getPalindrome = (string, left, right) => {
  while (left >= 0 && right < string.length && string[left] === string[right