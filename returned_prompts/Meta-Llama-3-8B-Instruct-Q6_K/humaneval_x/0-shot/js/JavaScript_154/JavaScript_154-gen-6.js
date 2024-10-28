Here is the solution to the problem:

```javascript
const cycpatternCheck = (a, b) => {
  for (let i = 0; i < a.length; i++) {
    if (a.slice(i).includes(b) || a.slice(i).includes(b + a.slice(0, i))) {
      return true;
    }
  }
  return false;
};
```

This function iterates over the first string `a` and checks if the second string `b` is a substring of the slice of `a` starting from the current index `i`. It also checks if `b` is a substring of the slice of `a` starting from `i` and ending at the length of the original string (which is equivalent to rotating the slice to the right by `i` positions). If either condition is true, the function returns `true`. If the function has checked all slices of `a` and none of them contain `b` or its rotation, it returns `false`.