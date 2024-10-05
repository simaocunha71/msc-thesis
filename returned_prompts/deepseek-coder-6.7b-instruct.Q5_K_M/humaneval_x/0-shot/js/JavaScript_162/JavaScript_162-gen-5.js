  if (!text)
    return null;

  return crypto.createHash('md5').update(text).digest('hex');
};

module.exports = stringToMd5;

// Test
console.log(stringToMd5('Hello world'));
```

## Solution

```javascript
const crypto = require('crypto');

const stringToMd5 = (text) => {
  if (!text)
    return null;

  return crypto.createHash('md5').update(text).digest('hex');
};

module.exports = stringToMd5;

// Test
console.log(stringToMd5('Hello world')); // '3e25960a79dbc69b674cd4ec67a72c62'
```

## Explanation

This code creates a function `stringToMd5` that takes a string `text` as an argument. If `text` is an empty string (i.e., falsy), the function returns `null`. Otherwise, it creates an md5 hash of `text` using `crypto.createHash('md5')`. The `update()` method is used to provide the data to be hashed, and the `digest()` method is used to generate the final hash as a hexadecimal string. The hashed string is then returned by the function.

The `crypto` module is a built-in module in Node.js, which provides cryptographic functionality that includes a set of wrappers for OpenSSL's hash, HMAC, cipher, decipher, sign, and verify functions.

The test at the end of the code calls the function with the string 'Hello world' as argument, and logs the returned hash to the console.

Please note that this code must be run in an environment where Node.js is installed and available.

---
[⬆ Back to top](#contents)
<!-- END -->























































