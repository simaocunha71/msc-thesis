```
const howManyTimes = (string, substring) => {
  let count = 0;
  let index = 0;
  while (index < string.length) {
    index = string.indexOf(substring, index);
    if (index === -1) {
      break;
    }
    count++;
    index++;
  }
  return count;
};
```


Explanation:
The function takes two parameters: `string` and `substring`. It returns the number of times the `substring` can be found in the `string`. The function uses a while loop to iterate over the `string`. Inside the loop, it uses the `indexOf` method to find the position of the `substring` in the `string`, starting from the current `index`. If the `substring` is not found, the `indexOf` method returns `-1`, and the loop breaks. If the `substring` is found, the `count` is incremented, and the `index` is incremented to continue the search from the next position. The function returns the final `count`. The `substring` can be overlapping, so the `index` is incremented by `1` in each iteration to ensure that the same position is not counted multiple times.