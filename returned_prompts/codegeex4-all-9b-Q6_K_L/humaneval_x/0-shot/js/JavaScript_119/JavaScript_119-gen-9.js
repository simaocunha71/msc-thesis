```java
const matchParens = (lst) => {
  let s = lst[0] + lst[1];
  let stack = [];
  for (let i = 0; i < s.length; i++) {
    if (s[i] == '(') {
      stack.push('(');
    } else {
      if (stack.length == 0) {
        return 'No';
      }
      stack.pop();
    }
  }
  if (stack.length == 0) {
    return 'Yes';
  }
  return 'No';
}
```
