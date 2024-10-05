```javascript
const cycpatternCheck = (a, b) => {
  for(let i = 0; i < b.length; i++) {
    let rotated = b.substring(i) + b.substring(0, i);
    if(a.includes(rotated)) {
      return true;
    }
  }
  return false;
};
```
This solution iterates over the characters in the second word `b` and checks if any of its rotations is a substring in the first word `a`. It does this by creating a new string `rotated` which is the rotation of `b` and then checking if `a` includes `rotated`. If it does, the function returns `true`. If it doesn't, the function returns `false` after checking all rotations of `b`. The function uses the `includes` method to check if `a` includes `rotated`. The `includes` method returns a boolean indicating whether the string includes the specified value. If the string includes the specified value, the method returns `true`; otherwise, it returns `false`. The function returns `false` if no rotation of `b` is a substring of `a`. This solution has a time complexity of O(n*m) where n is the length of `a` and m is the length of `b`. This is because in the worst case, we have to iterate over all characters in `a` and `b`. The space complexity is O(1) because we are not using any extra space that scales with the input size.