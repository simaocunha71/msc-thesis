```
function matchParens(lst) {
  let open = 0;
  let close = 0;
  for (let i = 0; i < lst.length; i++) {
    if (lst[i] === '(') {
      open++;
    } else {
      close++;
    }
  }
  if (open === close) {
    return 'Yes';
  } else {
    return 'No';
  }
}
```


Explanation:
This function counts the number of open and close parentheses in the given list. If the number of open and close parentheses is equal, then it is possible to concatenate the two strings to form a good string (i.e., a string with balanced parentheses). In this case, the function returns 'Yes'. Otherwise, it returns 'No'. The time complexity is O(n), where n is the length of the input list. The space complexity is O(1), as we only use a constant amount of space to store the counts of open and close parentheses.