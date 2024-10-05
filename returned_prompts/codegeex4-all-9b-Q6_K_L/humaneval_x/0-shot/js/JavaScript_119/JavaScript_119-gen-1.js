To solve this problem, we need to check if the total number of open parentheses '(' is equal to the total number of close parentheses ')' in either of the two strings. If they are equal, then it is possible to concatenate the two strings in some order to get a good string. Otherwise, it is not possible.

Here is the implementation of the matchParens function:

```javascript
const matchParens = (lst) => {
  let openCount = 0;
  let closeCount = 0;

  for (let i = 0; i < lst.length; i++) {
    for (let j = 0; j < lst[i].length; j++) {
      if (lst[i][j] === '(') {
        openCount++;
      } else if (lst[i][j] === ')') {
        closeCount++;
      }
    }
  }

  if (openCount === closeCount) {
    return 'Yes';
  } else {
    return 'No';
  }
};
```

Let's test the function with the provided examples:

```javascript
console.log(matchParens(['()(', ')'])); // 'Yes'
console.log(matchParens([')', ')'])); // 'No'
```

The output of the above code will be:

```
Yes
No
```

As expected, the function returns 'Yes' for the first example and 'No' for the second example.