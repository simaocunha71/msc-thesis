```
const matchParens = (lst) => {
  let open = 0;
  let close = 0;
  for (let i = 0; i < lst[0].length; i++) {
    if (lst[0][i] === '(') {
      open++;
    } else {
      close++;
    }
  }
  for (let i = 0; i < lst[1].length; i++) {
    if (lst[1][i] === '(') {
      open--;
    } else {
      close--;
    }
  }
  return open === 0 && close === 0 ? 'Yes' : 'No';
};
```

Explanation:
The function takes a list of two strings as an argument. We initialize two counters, open and close, to keep track of the number of open and close parentheses, respectively.

We then iterate over the first string. For each open parenthesis, we increment the open counter. For each close parenthesis, we increment the close counter.

Next, we iterate over the second string. For each open parenthesis, we decrement the open counter. For each close parenthesis, we decrement the close counter.

Finally, we check if both counters are equal to 0. If they are, it means that the total number of open and close parentheses is balanced, so we return 'Yes'. Otherwise, we return 'No'.