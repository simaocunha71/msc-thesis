```javascript
const howManyTimes = (string, substring) => {
  let count = 0;
  let index = 0;
  while (index < string.length) {
    index = string.indexOf(substring, index);
    if (index !== -1) {
      count++;
      index += substring.length;
    } else {
      break;
    }
  }
  return count;
};
```


Explanation:
The function `howManyTimes` takes two parameters: `string` and `substring`. It initializes a `count` variable to 0 and an `index` variable to 0. Then it enters a while loop that continues as long as `index` is less than the length of `string`.

 Inside the loop, it uses the `indexOf` method to find the index of `substring` in `string`, starting from the current `index`. If `indexOf` returns a value greater than or equal to 0, it means `substring` is found at that position. The `count` is incremented by 1 and `index` is updated to `index + substring.length` to start searching for the next occurrence from the end of the previous occurrence.

 If `indexOf` returns -1, it means `substring` is not found in `string` starting from `index`. In this case, the loop is terminated using the `break` statement.

 Finally, the function returns the `count`, which is the number of times `substring` is found in `string`. If `substring` is an empty string, the function returns 0, as per the problem statement.