Here is a possible implementation of the `longest` function in JavaScript:
```
const longest = (strings) => {
  if (strings.length === 0) return null;
  let longestStr = strings[0];
  for (let i = 1; i < strings.length; i++) {
    if (strings[i].length > longestStr.length) {
      longestStr = strings[i];
    }
  }
  return longestStr;
};
```
Here's an explanation of the code:

1. We first check if the input list `strings` is empty. If it is, we return `null`.
2. We initialize a variable `longestStr` to the first element of the list.
3. We loop through the rest of the list (starting from the second element).
4. For each element, we check if its length is greater than the current `longestStr`. If it is, we update `longestStr` to the current element.
5. Finally, we return the `longestStr` at the end of the loop.

You can test this implementation with the examples you provided:
```
console.log(longest([])); // null
console.log(longest(['a', 'b', 'c'])); // 'a'
console.log(longest(['a', 'bb', 'ccc'])); // 'ccc'
```
I hope this helps! Let me know if you have any questions. 😊

**Alternative Solution:**

You can use the `reduce()` method to achieve the same result in a more concise way:
```
const longest = (strings) => strings.reduce((acc, current) => current.length > acc.length ? current : acc, strings[0]);
```
This solution uses the `reduce()` method to iterate over the list of strings, starting with the first element as the initial value `acc`. For each element, it checks if the current string is longer than the accumulated longest string `acc`. If it is, it updates `acc` to the current string. Finally, it returns the accumulated longest string. 😊

Let me know if you have any questions or if you'd like me to explain further! 😊