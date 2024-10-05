Here is the solution:
```
const iscube = (a) => {
  let root = Math.cbrt(a);
  return Math.floor(root) === root;
}
```
Explanation:

* We use the `Math.cbrt` function to calculate the cube root of the input number `a`. This gives us the value of `x` such that `x^3 = a`.
* We then check if the result is an integer by comparing it to its own floor value using the `Math.floor` function. If the result is an integer, then `a` is a cube of some integer number, and we return `true`. Otherwise, we return `false`.

Note: This function assumes that the input is always valid, as specified in the problem statement. If the input can be invalid, additional error handling may be necessary.