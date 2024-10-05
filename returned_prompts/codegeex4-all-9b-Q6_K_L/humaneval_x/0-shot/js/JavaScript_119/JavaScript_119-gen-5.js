```java
const matchParens = (lst) => {
  const str1 = lst[0]
  const str2 = lst[1]
  const str3 = str1 + str2
  const str4 = str2 + str1
  const balancedStr1 = str1.split('(').length === str1.split(')').length
  const balancedStr2 = str2.split('(').length === str2.split(')').length
  const balancedStr3 = str3.split('(').length === str3.split(')').length
  const balancedStr4 = str4.split('(').length === str4.split(')').length
  if (balancedStr1 || balancedStr2 || balancedStr3 || balancedStr4) { return 'Yes' }
  return 'No'
}
```
