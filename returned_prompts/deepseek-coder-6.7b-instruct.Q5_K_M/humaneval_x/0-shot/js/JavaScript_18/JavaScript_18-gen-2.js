  let count = 0;
  let position = 0;

  // Check if substring is not empty
  if (!substring) {
    return count;
  }

  // While the position of the substring is found within the string
  while ((position = string.indexOf(substring, position)) !== -1) {
    count++;
    position++;
  }

  return count;
};

// Test cases
console.log(howManyTimes('', 'a')); // 0
console.log(howManyTimes('aaa', 'a')); // 3
console.log(howManyTimes('aaaa', 'aa')); // 3
console.log(howManyTimes('abcabcabcabc', 'abc')); // 4
console.log(howManyTimes('aaaaaa', 'aaa')); // 4
console.log(howManyTimes('ababab', 'ab')); // 3

```


```


[tests]
```

