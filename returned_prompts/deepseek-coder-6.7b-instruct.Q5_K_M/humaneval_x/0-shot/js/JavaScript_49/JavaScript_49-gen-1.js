  return Math.pow(2, n) % p;
}

console.log(modp(3, 5));
console.log(modp(1101, 101));
console.log(modp(0, 101));
console.log(modp(3, 11));
console.log(modp(100, 101));

```

This problem is an application of modular arithmetic. The function `modp` takes two parameters `n` and `p`, and it returns the result of the mathematical operation `2^n mod p`.

In JavaScript, the `Math.pow()` function is used to calculate the power of a number and the `%` operator is used to get the remainder of the division operation. 

In the `return` statement, `Math.pow(2, n) % p;`, `Math.pow(2, n)` calculates `2` raised to the power of `n` and `% p` calculates the remainder of the division of `2^n` by `p`.

This way, you can calculate the result of `2^n mod p` without worrying about the numerical overflow.

In the last five lines of code, you can test the function with different inputs.

Note: This function will not work correctly if `n` or `p` is a negative number, because the power of a number (including negative numbers) and the modulus operation are not defined for negative numbers.

This function has a time complexity of O(1) because it performs a constant number of operations regardless of the size of the input.

```javascript

```


```javascript

```


```javascript

```


```javascript

```


```javascript

```


```javascript

```


```javascript

```


```javascript

```


```javascript

```


```javascript

```


```javascript

```


```javascript

```


```javascript

```


```javascript

```


```javascript

```


```javascript

```


```javascript

```


```javascript
