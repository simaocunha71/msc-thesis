```js
const decodeShift = (s) => {
  return s.split("").map(ch => String.fromCharCode(
    ((ch.charCodeAt(0) + 21 - "a".charCodeAt(0)) % 26) + "a".charCodeAt(0)
  )).join("");
}
```