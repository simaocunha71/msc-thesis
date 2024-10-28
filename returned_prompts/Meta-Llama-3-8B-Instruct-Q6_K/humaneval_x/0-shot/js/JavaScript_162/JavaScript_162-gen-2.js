```
const crypto = require('crypto');

const stringToMd5 = (text) => {
  if (!text) return null;
  const hash = crypto.createHash('md5');
  hash.update(text);
  return hash.digest('hex');
};

// Test
console.log(stringToMd5('Hello world')); // Output: 3e25960a79dbc69b674cd4ec67a72c62
```


Explanation:
This problem asks to create a function that takes a string as input and returns its MD5 hash equivalent string. If the input string is empty, the function should return null.

To solve this problem, we can use the Node.js crypto module. We create a new hash object using `crypto.createHash('md5')`, then update the hash object with the input string using the `update` method. Finally, we get the hash digest using the `digest` method and convert it to a hexadecimal string using the 'hex' option.

In the test case, we call the `stringToMd5` function with the input 'Hello world' and verify that it returns the expected MD5 hash string. If the input string is empty, the function will return null as expected.