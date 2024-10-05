Here is the solution:
```
const longest = (strings) => {
  if (strings.length === 0) return null;
  let longestStr = strings[0];
  for (let str of strings) {
    if (str.length > longestStr.length) longestStr = str;
  }
  return longestStr;
};
```
Explanation:

1. We first check if the input list is empty. If it is, we return null.
2. We initialize the `longestStr` variable with the first string in the list.
3. We iterate through the list of strings. For each string, we check if its length is greater than the current `longestStr`. If it is, we update `longestStr` with the current string.
4. After iterating through the entire list, we return the `longestStr`, which is the longest string in the list.

Note: This solution has a time complexity of O(n), where n is the length of the input list, since we iterate through the list once. The space complexity is O(1), since we only use a constant amount of space to store the `longestStr` variable.