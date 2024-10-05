The function `iscube` checks if the given integer `a` is a cube of some integer number. A number is a cube if it can be expressed as the cube of an integer. For example, 1 is a cube of 1 (1^3 = 1), 8 is a cube of 2 (2^3 = 8), and so on.

Here's the implementation of the `iscube` function:

```javascript
const iscube = (a) => {
  if (a < 0) {
    a = -a;
  }
  for (let i = 0; i <= Math.sqrt(a) + 1; i++) {
    if (i * i * i === a) {
      return true;
    }
  }
  return false;
}
```

Explanation:
1. The function first checks if the given integer `a` is negative. If it is, it converts it to a positive number by taking its absolute value.
2. It then iterates from 0 to the square root of `a` plus 1 (inclusive). This is because a cube root of a number cannot be greater than its square root.
3. For each iteration, it checks if the cube of the current number (i * i * i) is equal to `a`.
4. If a match is found, the function returns `true`.
5. If no match is found after iterating through all possible numbers, the function returns `false`.

Example usage:
```javascript
console.log(iscube(1)); // true
console.log(iscube(2)); // false
console.log(iscube(-1)); // true
console.log(iscube(64)); // true
console.log(iscube(0)); // true
console.log(iscube(180)); // false
```

The output of the above code will be:
```
true
false
true
true
true
false
```