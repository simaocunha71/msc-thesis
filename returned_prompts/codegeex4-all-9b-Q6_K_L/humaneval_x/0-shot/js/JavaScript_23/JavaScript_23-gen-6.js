The function `strlen` is defined to take a single argument `string`. It returns the length of the string by using the `length` property of the string.

Here is the complete code:

```javascript
const strlen = (string) => {
  return string.length;
};
```

The function can be tested with the following code:

```javascript
console.log(strlen('')); // 0
console.log(strlen('abc')); // 3
```