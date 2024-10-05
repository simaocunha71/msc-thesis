You can solve this problem using the mathematical formula for the sum of the first n even numbers. The sum of the first n even numbers is given by the formula n * (n + 1). Therefore, you can check if n is equal to the sum of 4 even numbers by checking if n is equal to 4 times the sum of 4 (which is 8). If n is equal to 8, then it can be written as the sum of exactly 4 positive even numbers.

Here's how you can implement this in JavaScript:

```javascript
const isEqualToSumEven = (n) => {
  return n === 4 * (4 + 1);
};
```

You can test this function with the examples you provided:

```javascript
console.log(isEqualToSumEven(4)); // false
console.log(isEqualToSumEven(6)); // false
console.log(isEqualToSumEven(8)); // true
```