One of the numbers is equal to the sum of the other two if and only if one of the following conditions is true:

- x = y + z
- y = x + z
- z = x + y

In other words, if one of these conditions is true, then we can assign the value of one of the three numbers as the sum of the other two.

To solve this problem, we can use the modulo operator in JavaScript. The modulo operator returns the remainder of a division. So, if we divide x by the sum of y and z, we should get a remainder of 0 if x is equal to the sum of y and z.

Here's the JavaScript function that checks if one of the numbers is equal to the sum of the other two:

```javascript
function anyInt(x, y, z) {
  return (x % (y + z) === 0) || (y % (x + z) === 0) || (z % (x + y) === 0);
}
```

This function checks if the remainder of x divided by the sum of y and z is equal to 0, or if the remainder of y divided by the sum of x and z is equal to 0, or if the remainder of z divided by the sum of x and y is equal to 0. If any of these conditions is true, the function returns true; otherwise, it returns false.

You can use this function to check if one of the numbers is equal to the sum of the other two:

```javascript
console.log(anyInt(5, 2, 7));  // true
console.log(anyInt(3, 2, 2));  // false
console.log(anyInt(3, -2, 1)); // true
console.log(anyInt(3.6, -2.2, 2));  // false
```

In the first example, 5 is equal to the sum of 2 and 7, so the function returns true. In the second example, none of the numbers is equal to the sum of the other two, so the function returns false. In the third example, 1 is equal to the sum of 3 and -2, so the function returns true. In the fourth example, none of the numbers is