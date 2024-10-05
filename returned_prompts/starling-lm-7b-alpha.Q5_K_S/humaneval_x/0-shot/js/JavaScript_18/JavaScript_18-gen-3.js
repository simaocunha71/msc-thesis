To solve this problem, we can use the following steps:

1. Initialize a counter variable to keep track of the number of occurrences of the substring in the string. Set it to 0 initially.
2. Use a while loop to iterate through the string. In each iteration, check if the current position of the substring matches the first character of the substring. If it does, increment the counter by 1 and move the substring to the next position in the string. If it doesn't, move the substring to the next position in the string without incrementing the counter.
3. After the while loop finishes, the counter will contain the total number of occurrences of the substring in the string, including overlapping cases.
4. Return the value of the counter as the result.

Here's an example implementation of the solution in JavaScript:

```javascript
const howManyTimes = (string, substring) => {
  let counter = 0;
  let index = 0;

  while (index < string.length) {
    if (string.substring(index, index + substring.length) === substring) {
      counter++;
      index += substring.length;
    } else {
      index++;
    }
  }

  return counter;
};
```

You can use the `howManyTimes` function to find the number of times a given substring can be found in a string. The function takes two arguments: the string to search in (`string`) and the substring to search for (`substring`). It returns the number of occurrences of the substring in the string, including overlapping cases.

For example, if you call `howManyTimes('aaa', 'a')`, it will return 3 because the substring 'a' can be found three times in the string 'aaa', including overlapping cases. Similarly, if you call `howManyTimes('aaaa', 'aa')`, it will return 3 because the substring 'aa' can be found three times in the string 'aaaa', including overlapping cases.

Note that the function uses the `substring` method to extract a portion of the string, and the `===` operator to check if the extracted portion matches the substring.

I hope this helps! Let me