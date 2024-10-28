  let count = 0;
  let position = 0;

  // Loop through the string
  while (true) {
    position = string.indexOf(substring, position);
    if (position !== -1) {
      count++;
      position++;
    } else {
      break;
    }
  }

  return count;
};

console.log(howManyTimes('', 'a')); // 0
console.log(howManyTimes('aaa', 'a')); // 3
console.log(howManyTimes('aaaa', 'aa')); // 3
console.log(howManyTimes('ababab', 'ab')); // 3
console.log(howManyTimes('abcabcabc', 'abc')); // 3

```



### 3. Create a function that takes two strings and returns the longest common substring.

