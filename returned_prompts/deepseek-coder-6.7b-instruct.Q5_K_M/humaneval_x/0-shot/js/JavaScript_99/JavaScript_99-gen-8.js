  const num = parseFloat(value);
  return (num < 0) ? Math.floor(num - 0.5) : Math.floor(num + 0.5);

};

console.log(closestInteger("10")); // 10
console.log(closestInteger("15.3")); // 15
console.log(closestInteger("14.5")); // 15
console.log(closestInteger("-14.5")); // -15

/*
The function takes a string value, converts it into a number, and rounds it to the nearest integer using Math.floor() method. 
If the number is negative, the subtraction by 0.5 is used to round towards negative infinity. If the number is positive, the addition by 0.5 is used to round towards positive infinity. 
This method works because for positive numbers, adding 0.5 before using Math.floor() effectively rounds the number up, and for negative numbers, subtracting 0.5 rounds the number down.
*/
```

## JavaScript

```javascript
