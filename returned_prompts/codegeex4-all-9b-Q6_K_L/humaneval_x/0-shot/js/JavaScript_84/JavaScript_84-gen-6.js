```javascript
const solve = (N) => {
  // convert N to binary string
  let binary = N.toString(2);
  // initialize sum to 0
  let sum = 0;
  // iterate through binary string
  for (let i = 0; i < binary.length; i++) {
    // add each digit to sum
    sum += parseInt(binary[i]);
  }
  // return sum in binary form
  return sum.toString(2);
}
```
