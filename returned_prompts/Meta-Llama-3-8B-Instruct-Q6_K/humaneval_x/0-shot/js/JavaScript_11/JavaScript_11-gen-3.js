```
  return a.split('').map((x, i) => (x === b[i % b.length]) ? '0' : '1').join('');
```


Explanation:
This function takes two binary strings `a` and `b` as input. It performs a binary XOR operation on the two strings. The XOR operation is performed at each position in the strings, and the result is a binary string.

Here's a step-by-step breakdown of how the function works:

1. `a.split('')`: This splits the string `a` into an array of individual characters (i.e., `['0', '1', '0']` for the string `'010'`).
2. `map()`: This applies a function to each element of the array. In this case, the function is a callback that takes two arguments: `x` (the current element in the array) and `i` (the index of the current element in the array).
3. `(x === b[i % b.length]) ? '0' : '1'`: This is the callback function. It checks whether the current element `x` in `a` is equal to the corresponding element in `b` (wrapping around to the start of `b` if necessary using the modulo operator `%`). If they are equal, the function returns `'0'`; otherwise, it returns `'1'`.
4. `join('')`: This joins the resulting array of characters back into a string, with no separator between the elements.

For example, if `a` is `'010'` and `b` is `'110'`, the function would perform the following operations:

1. `a.split('')` -> `['0', '1', '0']`
2. `map()` -> `['1', '0', '0']` (because `0 === 1` is false, `1 === 1` is true, and `0 === 0` is true)
3. `join('')` -> `'100'`

The final result is the string `'100'`, which is the binary XOR of the input strings.