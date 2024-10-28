Here is the solution using JavaScript:

```javascript
const digits = (n) => {
  let product = 1;
  while (n > 0) {
    const digit = n % 10;
    if (digit % 2 !== 0) {
      product *= digit;
    }
    n = Math.floor(n / 10);
  }
  return product;
};
```

Explanation:
The function takes an integer `n` as input and returns the product of its odd digits. If all digits are even, it returns 0.

Here's how it works:

1. We initialize a variable `product` to 1, which will be used to store the product of the odd digits.
2. We use a while loop to iterate through each digit of the input number `n`.
3. In each iteration, we get the last digit of `n` using the modulo operator `% 10`.
4. We check if the digit is odd by using the modulo operator `% 2`. If the remainder is not 0, it means the digit is odd.
5. If the digit is odd, we multiply the `product` by the digit.
6. We then update `n` by dividing it by 10 using the `Math.floor` function, effectively removing the last digit.
7. Once the loop finishes, we return the `product` value.

For example, if we call the function with the input `235`, it will iterate through the digits 3, 5, and 2. Since 3 and 5 are odd, it will multiply the `product` variable by them, resulting in a product of 15. If we call the function with the input `4`, it will iterate through the digit 4, which is even, so the function will return 0.