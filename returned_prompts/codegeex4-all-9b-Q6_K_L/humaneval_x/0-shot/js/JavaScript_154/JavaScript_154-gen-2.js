You can solve this problem by checking if the second word is a substring in the first word and its rotations. Here's how you can do it in JavaScript:

```javascript
const cycpatternCheck = (a, b) => {
  // Check if b is a substring in a
  if (a.includes(b)) {
    return true;
  }

  // Create rotations of b
  let rotations = [];
  for (let i = 0; i < b.length; i++) {
    rotations.push(b.slice(i) + b.slice(0, i));
  }

  // Check if any rotation of b is a substring in a
  for (let rotation of rotations) {
    if (a.includes(rotation)) {
      return true;
    }
  }

  // If no rotation of b is a substring in a, return false
  return false;
};
```

This function first checks if `b` is a substring in `a`. If it is, the function returns `true`. Otherwise, the function creates all rotations of `b` and checks if any of them is a substring in `a`. If any of the rotations is a substring in `a`, the function returns `true`. If none of the rotations is a substring in `a`, the function returns `false`.