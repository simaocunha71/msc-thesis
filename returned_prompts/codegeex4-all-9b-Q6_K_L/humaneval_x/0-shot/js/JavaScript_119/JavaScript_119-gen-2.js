```java
const matchParens = (lst) => {
  let s = lst[0] + lst[1]
  let open = 0
  for (let i = 0; i < s.length; i++) {
    if (s[i] == '(')
      open++
    else
      open--
    if (open < 0)
      return 'No'
  }
  return open == 0 ? 'Yes' : 'No'
}
```
