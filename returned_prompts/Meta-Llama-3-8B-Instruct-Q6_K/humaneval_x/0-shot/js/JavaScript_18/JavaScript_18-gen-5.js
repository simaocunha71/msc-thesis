Here is the solution for the problem:

```javascript
const howManyTimes = (string, substring) => {
  let count = 0;
  let index = 0;
  
  while (index < string.length) {
    index = string.indexOf(substring, index);
    if (index === -1) break;
    count++;
    index += substring.length;
  }
  
  return count;
};
```


Explanation:
The function `howManyTimes` takes two parameters: `string` and `substring`. It initializes a counter `count` to 0 and an index `index` to 0.

The function then enters a loop that continues until `index` is no longer less than the length of `string`. Inside the loop, it uses the `indexOf` method to find the position of the `substring` in `string`, starting from the current `index`. If `substring` is not found, `indexOf` returns -1, and the loop breaks.

If `substring` is found, `count` is incremented, and `index` is updated to be `index` plus the length of `substring`. This ensures that the next iteration of the loop starts searching for `substring` from the position just after the previous occurrence.

Finally, the function returns the total count of occurrences of `substring` in `string`.