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
}
```


Explanation:
The function `howManyTimes` takes two parameters, `string` and `substring`. It returns the number of times `substring` can be found in `string`, counting overlapping cases.

The function uses a while loop to iterate through the `string`. It uses the `indexOf` method to find the index of the `substring` in the `string`, starting from the current index. If `substring` is not found, `indexOf` returns `-1` and the loop breaks.

The function increments the `count` variable each time it finds `substring` and adds the length of `substring` to the current index to continue searching from the next position.

Finally, the function returns the `count` variable, which represents the number of times `substring` can be found in `string`.