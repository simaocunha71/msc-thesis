```java
const reverseDelete = (s, c) => {
  let out = s.split('').filter(x => !c.includes(x)).join('')
  let rev = out.split('').reverse().join('')
  return [out, out == rev]
}
```
