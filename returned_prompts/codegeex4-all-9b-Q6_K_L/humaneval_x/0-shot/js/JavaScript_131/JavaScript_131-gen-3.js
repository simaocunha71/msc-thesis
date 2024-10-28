You can solve this problem by converting the number to a string and then iterating over each character. If the character is an odd digit, multiply it to a result variable. If all digits are even, return 0. Here is an example solution in JavaScript:

```javascript
const digits = (n) => {
  let product = 1;
  let isAllEven = true;
  
  // Convert the number to a string
  let numString = n.toString();
  
  // Iterate over each character
  for (let i = 0; i < numString.length; i++) {
    // Check if the character is an odd digit
    if (numString[i] % 2 !== 0) {
      product *= numString[i];
      isAllEven = false;
    }
  }
  
  // Return 0 if all digits are even
  if (isAllEven) {
    return 0;
  } else {
    return product;
  }
}
```

This solution has a time complexity of O(n), where n is the number of digits in the input number.