To solve this problem, we can use the built-in `crypto` module in Node.js, which provides functions to generate cryptographic hashes. Specifically, we can use the `createHash` method to create a hash object, set the hashing algorithm to 'md5', and then update it with the input string. Finally, we can convert the hash object to a hexadecimal string using the `digest` method and return it.

Here's the implementation:

```javascript
const crypto = require('crypto');

const stringToMd5 = (text) => {
  if (text === '') {
    return null;
  }

  const hash = crypto.createHash('md5');
  hash.update(text);
  return hash.digest('hex');
};
```

Let's test the function with the provided test case:

```javascript
console.log(stringToMd5('Hello world'));
```

The output should be:
```
3e25960a79dbc69b674cd4ec67a72c62
```