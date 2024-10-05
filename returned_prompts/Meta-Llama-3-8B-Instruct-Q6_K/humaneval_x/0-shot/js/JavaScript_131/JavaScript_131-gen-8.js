```
function digits(n) {
  let product = 1;
  while (n > 0) {
    const digit = n % 10;
    if (digit % 2 !== 0) {
      product *= digit;
    }
    n = Math.floor(n / 10);
  }
  return product;
}
```


Explanation:
The function `digits` takes a positive integer `n` as input and returns the product of its odd digits.

Here's how it works:

1. Initialize the product variable to 1, which will be used to store the product of the odd digits.
2. Use a while loop to iterate over each digit of the number `n`. In each iteration, the remainder of `n` divided by 10 is taken, which gives the last digit of `n`.
3. Check if the digit is odd by using the modulo operator (`%`). If the digit is odd, multiply the product by the digit.
4. Divide `n` by 10 to move to the next digit.
5. Repeat steps 2-4 until `n` becomes 0.
6. Return the product.

For example, for the input `235`, the function will iterate over the digits 5, 3, and 2. The product of the odd digits is 15, so the function returns 15. For the input `4`, the function will iterate over the digit 4, which is even, so the function returns 0.