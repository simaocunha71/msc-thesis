The unit digit of an integer can be found by taking the modulus of the integer by 10. This operation will give the last digit of the number. 

So, to solve this problem, you can find the unit digits of the two input integers, multiply them together and return the result.

Here is the JavaScript code for this approach:
```javascript
const multiply = (a, b) => {
    let unitDigitA = Math.abs(a) % 10;
    let unitDigitB = Math.abs(b) % 10;
    return unitDigitA * unitDigitB;
};
```
This function first finds the unit digits of the two integers by taking the modulus of the integers by 10. Then it multiplies these unit digits together and returns the result. The Math.abs() function is used to ensure that the function works correctly with both positive and negative input integers.