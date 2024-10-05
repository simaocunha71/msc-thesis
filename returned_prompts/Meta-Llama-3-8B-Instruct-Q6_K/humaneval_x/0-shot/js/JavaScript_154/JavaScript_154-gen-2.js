```javascript
const cycpatternCheck = (a, b) => {
  for (let i = 0; i < b.length; i++) {
    if (a.includes(b.slice(i) + b.slice(0, i))) {
      return true;
    }
  }
  return false;
};
```


Explanation:

This function takes two strings `a` and `b` as input. It iterates over the length of `b` and checks if `b` is a substring of `a` by rotating `b` by `i` characters. If `b` is a substring of `a`, it returns `true`. If it doesn't find any match after checking all rotations, it returns `false`.

The line `if (a.includes(b.slice(i) + b.slice(0, i)))` is checking if `b` is a substring of `a` by concatenating the rotated `b` with itself. This is done by using the `slice` method to get a part of the string and then concatenating it with the rest of the string using the `+` operator. The `includes` method is then used to check if the resulting string is a substring of `a`. If it is, the function returns `true`. If not, it continues to the next iteration. If it doesn't find any match after checking all rotations, it returns `false`.