The digits in the integer should be extracted and multiplied. If the digit is even, return 0. If the digit is odd, multiply the result with the digit. Here is a JavaScript solution:

```javascript
const digits = (n) => {
    let product = 1;
    let allEven = true;
    while (n > 0) {
        let digit = n % 10;
        if (digit % 2 === 0) {
            return 0;
        } else {
            product *= digit;
            allEven = false;
        }
        n = Math.floor(n / 10);
    }
    if (allEven) return 0;
    return product;
}
```
In this solution, we are checking each digit of the number and if it is even, we immediately return 0. If the digit is odd, we multiply it with the product and continue with the next digit. If all digits are even, we return 0.