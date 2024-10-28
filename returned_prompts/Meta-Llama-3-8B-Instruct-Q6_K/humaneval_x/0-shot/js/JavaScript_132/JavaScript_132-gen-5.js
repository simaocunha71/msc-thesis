Here is the solution for the problem:
```
const isNested = (string) => {
  let count = 0;
  for (let char of string) {
    if (char === '[') {
      count++;
    } else if (char === ']') {
      if (count > 0) {
        count--;
      } else {
        return false;
      }
    }
  }
  return count > 0;
};
```
Here's an explanation of the solution:

We use a variable `count` to keep track of the number of open brackets `[]` we've seen so far. We iterate through the input string character by character. If we encounter an open bracket `[]`, we increment the `count`. If we encounter a close bracket `]`, we decrement the `count`. If the `count` becomes negative, it means we've encountered a close bracket without a matching open bracket, so we return `false`. If we reach the end of the string and the `count` is greater than 0, it means there's at least one open bracket that hasn't been closed, so we return `true`. Otherwise, we return `false`.