```java
const circularShift = (x, shift) => {
  let s = x.toString();
  if (shift > s.length) {
    s = s.split('').reverse().join('');
  } else {
    s = s.slice(-shift) + s.slice(0, -shift);
  }
  return s;
}
```