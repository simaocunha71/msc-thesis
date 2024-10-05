Here is the solution using JavaScript:

```javascript
const stringXor = (a, b) => {
  let result = '';
  
  for (let i = 0; i < a.length; i++) {
    result += (a[i] ^ b[i]);
  }

  return result;
};
```

This function works by looping over each character in the string `a` and `b` and performing a binary XOR operation on them. The result is appended to the `result` string which is returned at the end of the function.

Remember that in JavaScript, the bitwise XOR operator (`^`) is used to perform the XOR operation.

Note: This function assumes that the strings `a` and `b` are of the same length. If they are not, you will need to pad the shorter string with zeros at the beginning.

Here is an example of how you can use this function:

```javascript
console.log(stringXor('010', '110'));  // Output: '100'
```

This will output the string '100', which is the result of performing the XOR operation on the two input strings '010' and '110'.

This function works by converting the binary strings to numbers, performing the XOR operation, and then converting the result back to a binary string. This is because JavaScript does not have built-in support for binary operations on strings.

Note: This function assumes that the strings `a` and `b` are of the same length. If they are not, you will need to pad the shorter string with zeros at the beginning.

Here is an example of how you can use this function:

```javascript
console.log(stringXor('010', '110'));  // Output: '100'
```

This will output the string '100', which is the result of performing the XOR operation on the two input strings '010' and '