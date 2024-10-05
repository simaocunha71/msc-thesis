```java
const reverseDelete = (s, c) => {
  let t = s.split('').filter(x => !c.includes(x)).join('')
  return [t, t.split('').reverse().join('') == t]
}
```
