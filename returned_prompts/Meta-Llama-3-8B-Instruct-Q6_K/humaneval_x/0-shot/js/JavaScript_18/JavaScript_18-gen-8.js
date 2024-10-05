```javascript
const howManyTimes = (string, substring) => {
  if (!substring) return 0;
  let count = 0;
  let index = 0;
  while (index < string.length) {
    index = string.indexOf(substring, index);
    if (index === -1) break;
    count++;
    index++;
  }
  return count;
};
```


Here's an explanation of the code:

1. If the substring is empty, return 0.
2. Initialize a count variable to 0 and an index variable to 0.
3. Use a while loop to iterate through the original string, starting from the beginning.
4. Inside the loop, use the `indexOf` method to find the first occurrence of the substring starting from the current index.
5. If the substring is not found, break out of the loop.
6. If the substring is found, increment the count variable and increment the index to continue searching from the next position.
7. Return the count variable, which represents the number of times the substring can be found in the original string.