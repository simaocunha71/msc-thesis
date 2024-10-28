  // First, we split the string into an array of groups.
  let groups = paren_string.split(' ');

  // Then, we map through each group and use reduce to count the maximum depth of nesting.
  return groups.map(group => {
    return [...group].reduce((max, char) => {
      return char === '(' ? max + 1 : max - 0.5;
    }, 0)
  });
}

console.log(parseNestedParens('(()())  ((()))  ()  ((())()())'));

*/

// Solution:
const parseNestedParens = (paren_string) => {
  let groups = paren_string.split(' ');

  return groups.map(group => {
    return [...group].reduce((max, char) => {
      return char === '(' ? max + 1 : max - 0.5;
    }, 0)
  });
}

console.log(parseNestedParens('(()())  ((()))  ()  ((())()())'));

// Output: [2, 3, 1, 3]

// Explanation: 
// - In '(()())', there are 2 levels of nesting.
// - In '((()))', there are 3 levels of nesting.
// - In '()', there is 1 level of nesting.
// - In '((())()())', there are 3 levels of nesting.

// The solution works by splitting the input string into groups of parentheses,
// then for each group, reducing the string to count the maximum depth of nesting.
// The depth of nesting is increased by 1 for each '(' encountered and decreased by 0.5 for each ')' encountered.
// The final result is an array of depths for each group.



// END SOLUTION
```

## Solution 2

```javascript
// Solution:
const parseNestedParens = (paren_string) => {
  return paren_string.split(' ').map(group => {
    let count = 0, max = 0;
    for(let i = 0