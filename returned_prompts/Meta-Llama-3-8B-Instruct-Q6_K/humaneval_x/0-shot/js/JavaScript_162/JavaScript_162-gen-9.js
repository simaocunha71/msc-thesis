```
const crypto = require('crypto');

const stringToMd5 = (text) => {
  if (!text) return null;
  return crypto.createHash('md5').update(text).digest('hex');
};
```


Explanation:
In this solution, we use the `crypto` module in Node.js to create an MD5 hash of the input string. The `createHash` function is used to create an MD5 hash object, and the `update` method is used to update the hash object with the input string. The `digest` method is used to get the digest (i.e., the hash value) of the hash object, and the `hex` encoding is used to convert the digest to a hexadecimal string.

In the code, we first check if the input string `text` is empty. If it is, we return `null`. Otherwise, we create an MD5 hash object, update it with the input string, and get the digest. We then convert the digest to a hexadecimal string and return it.

The unit test `>>> stringToMd5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'` checks if the function correctly returns the MD5 hash of the input string 'Hello world'. The expected output is the MD5 hash value of 'Hello world'. The test passes if the function returns the correct hash value.