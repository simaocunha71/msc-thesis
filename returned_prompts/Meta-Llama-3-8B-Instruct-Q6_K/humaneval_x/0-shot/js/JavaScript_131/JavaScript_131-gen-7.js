```
let product = 1;
let oddDigits = 0;
while (n > 0) {
  let digit = n % 10;
  if (digit % 2 !== 0) {
    product *= digit;
    oddDigits++;
  }
  n = Math.floor(n / 10);
}
return oddDigits > 0 ? product : 0;
```


Explanation:

1. Initialize the product to 1 and the count of odd digits to 0.
2. Loop through the digits of the number from right to left (using the modulus operator to extract the last digit, and then floor division to remove it).
3. For each digit, check if it's odd (using the modulus operator). If it is, multiply the product by the digit and increment the count of odd digits.
4. If no odd digits were found, return 0. Otherwise, return the product.

This solution has a time complexity of O(log n), where n is the input number, since we're looping through the digits of the number. The space complexity is O(1), since we're using a constant amount of space to store the product and the count of odd digits.