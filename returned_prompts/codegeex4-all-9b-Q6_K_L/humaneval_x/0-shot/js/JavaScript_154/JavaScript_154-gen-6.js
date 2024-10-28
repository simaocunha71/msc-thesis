The function `cycpatternCheck` should be implemented as follows:

```javascript
const cycpatternCheck = (a, b) => {
  for (let i = 0; i < b.length; i++) {
    let rotated = b.slice(i) + b.slice(0, i);
    if (a.includes(rotated)) {
      return true;
    }
  }
  return false;
}
```

The function `cycpatternCheck` takes two arguments, `a` and `b`, which are both strings. It returns `true` if the second string `b` or any of its rotations is a substring in the first string `a`, and `false` otherwise.

The function uses a for-loop to generate all possible rotations of `b` and checks if any of them is a substring in `a` using the `includes` method. If a match is found, the function returns `true`. If no match is found after checking all rotations, the function returns `false`.