  let i = string.length;
  
  while (i > 0) {
    if (isPalindrome(string.slice(0, i))) {
      return string + string.slice(i).split('').reverse().join('');
    }
    i--;
  }
}
```

## Exercise 2

The following JavaScript function returns the number of occurrences of a substring within a string.

```javascript
