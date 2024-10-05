  let count = 0;
  let position = 0;
  
  // Loop through the string
  while (true) {
    position = string.indexOf(substring, position);
    if (position === -1) break;
    count++;
    position++;
  }
  
  return count;
};

console.log(howManyTimes('', 'a')); // 0
console.log(howManyTimes('aaa', 'a')); // 3
console.log(howManyTimes('aaaa', 'aa')); // 3
```

## 2. Write a JavaScript function that checks if a string is a palindrome.

