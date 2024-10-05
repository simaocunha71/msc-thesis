```
let product = 1;
while (n > 0) {
  const digit = n % 10;
  if (digit % 2 !== 0) {
    product *= digit;
  }
  n = Math.floor(n / 10);
}
return product;
```
Explanation:
We use a while loop to iterate through each digit of the number. We use the modulus operator (`%`) to get the remainder of the division of `n` by 10, which gives us the last digit of `n`. We check if the digit is odd by using the modulus operator again (`% 2 !== 0`). If it is odd, we multiply the product by the digit. We then update `n` by performing integer division by 10 (`Math.floor(n / 10)`). We repeat this process until `n` is 0. Finally, we return the product.

For example, for the number 235, the product would be calculated as follows:

* `n` is 235, the last digit is 5 (which is odd), so `product` becomes 5.
* `n` is now 23, the last digit is 3 (which is odd), so `product` becomes 15.
* `n` is now 2, which is even, so we don't update `product`.
* `n` is now 0, so the loop ends.
* We return the product, which is 15.