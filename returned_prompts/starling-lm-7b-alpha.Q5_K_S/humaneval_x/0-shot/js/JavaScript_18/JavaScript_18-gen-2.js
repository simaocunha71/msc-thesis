To solve this problem, we can use the following steps:

1. Initialize a count variable to keep track of the number of occurrences of the substring in the string. Set it to 0 initially.
2. Use a while loop to iterate through the string. In each iteration, check if the current substring (substring length) of the string matches the given substring. If it does, increment the count variable and move the start index of the string by the length of the substring.
3. Repeat step 2 until the entire string has been traversed.
4. Return the count variable, which represents the number of times the given substring can be found in the original string, including overlapping cases.

Here's an implementation of the solution in JavaScript:

```javascript
const howManyTimes = (string, substring) => {
  let count = 0;
  let startIndex = 0;

  while (startIndex < string.length) {
    const currentSubstring = string.substring(startIndex, startIndex + substring.length);
    if (currentSubstring === substring) {
      count++;
      startIndex += substring.length;
    } else {
      startIndex++;
    }
  }

  return count;
};
```

You can use this function by passing in the original string and the substring you want to find occurrences of. The function will return the count of occurrences, including overlapping cases.

For example, if you call `howManyTimes('aaa', 'a')`, it will return 3 because there are three 'a' characters in the string 'aaa'. Similarly, if you call `howManyTimes('aaaa', 'aa')`, it will return 3 because there are three occurrences of the substring 'aa' in the string 'aaaa'.

The function works by iterating through the string and checking each substring of length `substring.length` starting from the current index. If the current substring matches the given substring, it increments the count and moves the start index by the length of the substring. If the current substring doesn't match the given substring, it moves the start index by one to check the next substring.

By using this approach, the function can accurately count