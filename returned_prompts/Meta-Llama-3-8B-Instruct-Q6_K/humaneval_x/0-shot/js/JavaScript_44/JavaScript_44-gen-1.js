```
const changeBase = (x, base) => {
  let result = '';
  while (x > 0) {
    result = String(x % base) + result;
    x = Math.floor(x / base);
  }
  return result;
};
```



Explanation: 

This function takes two parameters: x, the number to be converted, and base, the new base to convert to. 

The function initializes an empty string `result` to store the converted number. 

It then enters a while loop that continues until `x` is 0. 

Inside the loop, it calculates the remainder of `x` divided by `base` using the modulus operator (`%`). This remainder is converted to a string using `String()` and concatenated to the beginning of `result` using the `+` operator. 

Then, it updates `x` by performing integer division of `x` by `base` using `Math.floor()` and the `/` operator. 

Once the loop finishes, `result` contains the converted number in the new base. 

Finally, the function returns `result`. 

This function works for any base less than 10, as required by the problem statement. 

For example, if you call `changeBase(8, 3)`, it will return `'22'`, which is the base-3 representation of the number 8. If you call `changeBase(8, 2)`, it will return `'1000'`, which is the base-2 representation of the number 8. If you call `changeBase(7, 2)`, it will return `'111'`, which is the base-2 representation of the number 7. 

Note that this function does not handle invalid inputs, such as non-integer values of `x` or `base` values greater than or equal to 10. You may want to add error handling code to deal with these cases if necessary. 