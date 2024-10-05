The problem can be solved by implementing the XOR operation on the binary strings. 

Here is the JavaScript code to solve this problem:

```javascript
const stringXor = (a, b) => {
  // Convert binary strings to arrays of integers
  let aArray = a.split('').map(Number);
  let bArray = b.split('').map(Number);

  // Perform XOR operation on each pair of integers
  let resultArray = aArray.map((num, idx) => num ^ bArray[idx]);

  // Convert array of integers back to a binary string
  let result = resultArray.join('');

  return result;
};

console.log(stringXor('010', '110')); // '100'
```

In this code, we first split the binary strings into arrays of integers, then perform the XOR operation on each pair of integers, and finally join the resulting array back into a binary string.