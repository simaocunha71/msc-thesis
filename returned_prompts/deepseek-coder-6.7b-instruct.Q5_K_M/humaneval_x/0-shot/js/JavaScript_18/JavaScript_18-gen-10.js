  let count = 0;
  let position = 0;

  // Loop through the string
  while (true) {
    position = string.indexOf(substring, position);
    if (position !== -1) {
      count++;
      position = position + 1;
    } else {
      break;
    }
  }

  return count;
};

console.log(howManyTimes('', 'a')); // 0
console.log(howManyTimes('aaa', 'a')); // 3
console.log(howManyTimes('aaaa', 'aa')); // 3

```

This code defines a function called `howManyTimes` that takes a string and a substring as parameters and returns the count of how many times the substring can be found in the string. It uses the `indexOf` method of the String object to find the position of the substring in the string. It then increments the count and continues the search from the next position. If `indexOf` returns -1, it means the substring is not found and the search ends.

The time complexity of this function is O(n), where n is the length of the string. This is because the `indexOf` method may need to be called n times in the worst case scenario, where the substring is not found in the string.

The space complexity of this function is O(1), which means it uses a constant amount of space to store the count and the position.

Note: If you want to count overlapping occurrences, you can just start searching from the same position as the previous occurrence.
*/
























































































































































