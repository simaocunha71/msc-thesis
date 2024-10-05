```
function matchParens(lst) {
  let open = 0;
  let close = 0;
  for (let str of lst) {
    for (let char of str) {
      if (char === '(') {
        open++;
      } else if (char === ')') {
        close++;
      }
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
This function takes a list of two strings as input, each string contains only open and close parentheses. It counts the number of open and close parentheses in each string, and then checks if the counts are equal. If they are equal, it returns 'Yes', meaning it's possible to concatenate the strings to form a good string. If the counts are not equal, it returns 'No', meaning it's not possible to form a good string by concatenating the strings.

The function uses two variables, open and close, to count the number of open and close parentheses respectively. It iterates over each string in the list, and then over each character in the string. If the character is an open parenthesis, it increments the open count. If the character is a close parenthesis, it increments the close count. After counting the parentheses, it checks if the counts are equal. If they are, it returns 'Yes', otherwise it returns 'No'.