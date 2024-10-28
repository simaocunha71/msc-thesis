```javascript
const longest = (strings) => {
  if (strings.length === 0) {
    return null;
  }
  return strings.reduce((max, current) => {
    return current.length > max.length ? current : max;
  }, strings[0]);
};
```
Explanation:
The function `longest` takes a list of strings as an argument. It first checks if the list is empty. If it is, the function returns `null`. If the list is not empty, it uses the `reduce` method to iterate over the list of strings. The `reduce` method takes two arguments: an initial value (`strings[0]`) and a callback function. The callback function is called for each element in the list, and it takes two arguments: the accumulator (`max`) and the current element (`current`). If the length of the current element is greater than the length of the accumulator, the accumulator is updated to be the current element. If the lengths are equal, the accumulator remains the same. The `reduce` method returns the final value of the accumulator, which is the longest string in the list. If there are multiple strings of the same length, the function returns the first one it encounters.