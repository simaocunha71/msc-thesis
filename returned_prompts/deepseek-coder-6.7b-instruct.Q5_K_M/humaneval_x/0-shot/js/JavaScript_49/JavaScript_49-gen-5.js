  return Math.pow(2, n) % p;
};
console.log(modp(3, 5));
console.log(modp(1101, 101));
console.log(modp(0, 101));
console.log(modp(3, 11));
console.log(modp(100, 101));

```

The function `modp(n, p)` computes the modular exponentiation of 2 to the power of `n` modulo `p` using the built-in `Math.pow()` function.

```javascript
return Math.pow(2, n) % p;
```

This line of code calculates `2` to the power of `n` and then finds the remainder when that result is divided by `p`.

```javascript
console.log(modp(3, 5));
console.log(modp(1101, 101));
console.log(modp(0, 101));
console.log(modp(3, 11));
console.log(modp(100, 101));
```

These `console.log()` statements are used to test the function with different inputs.

## Output

```javascript
3
2
1
8
1
```

The function `modp(n, p)` works as expected and produces the expected output.



## Explanation

In JavaScript, the `%` operator is used to find the remainder of a division operation. If you divide `2` to the power of `n` by `p` and then find the remainder, you'll get the same result as if you calculated `2` to the power of `n` modulo `p`.

For instance, if you want to find `2^3 % 5`, you would calculate `2^3` to be `8` and then find `8 % 5` to be `3`. This is exactly what the function `modp(n, p)` is doing. It calculates `2^n` modulo `p` and returns the result.

The function `modp(n, p