Here is the solution:
```
const longest = (strings) => {
  if (strings.length === 0) return null;
  let longestString = strings[0];
  for (let i = 1; i < strings.length; i++) {
    if (strings[i].length > longestString.length) {
      longestString = strings[i];
    }
  }
  return longestString;
};
```
Explanation:

1. We first check if the input list `strings` is empty. If it is, we return `null`.
2. We initialize a variable `longestString` to the first element of the list.
3. We iterate through the list starting from the second element (index 1).
4. For each element, we check if its length is greater than the length of the current `longestString`. If it is, we update `longestString` to the current element.
5. After iterating through the entire list, we return the `longestString`.

This solution has a time complexity of O(n), where n is the length of the input list, because we only need to iterate through the list once. The space complexity is O(1), because we only use a constant amount of space to store the `longestString` variable.