Here is the solution:
```
const isNested = (string) => {
  let nestingLevel = 0;
  for (let char of string) {
    if (char === '[') {
      nestingLevel++;
    } else if (char === ']') {
      if (nestingLevel === 0) return false;
      nestingLevel--;
    }
  }
  return nestingLevel > 0;
};
```
Explanation:

* We initialize a `nestingLevel` variable to keep track of the current nesting level of brackets.
* We iterate through each character in the input string.
* When we encounter a '[' character, we increment the `nestingLevel`.
* When we encounter a ']' character, we decrement the `nestingLevel`. If the `nestingLevel` becomes 0, it means we have just closed a bracket and there is no nested bracket, so we return `false`.
* If we reach the end of the string and the `nestingLevel` is greater than 0, it means there is a valid subsequence of brackets with at least one nested bracket, so we return `true`.

This solution works by keeping track of the nesting level of brackets and checking if there is at least one nested bracket at the end of the string. It does not care about the order of brackets, only about the nesting level. This is why it returns `true` for inputs like '[[][]]' and '[[]][['.