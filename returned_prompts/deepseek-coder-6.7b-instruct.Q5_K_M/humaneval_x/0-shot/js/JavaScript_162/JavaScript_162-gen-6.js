if (!text) return null;

return crypto.createHash('md5').update(text).digest('hex');

};

module.exports = stringToMd5;

*/


A: This problem can be solved by using the crypto module in Node.js. Here is a JavaScript function that takes a string as input and returns its MD5 hash.

```javascript
const crypto = require('crypto');

function stringToMd5(text) {
  if (text === "") return null;

  let md5 = crypto.createHash('md5');
  let hash = md5.update(text, 'utf-8');

  return hash.digest('hex');
}

console.log(stringToMd5("Hello world"));  // Outputs: 3e25960a79dbc69b674cd4ec67a72c62
```

This function first checks if the input string is an empty string. If it is, the function returns null. Then it creates a new MD5 hash object using the crypto module. It updates the hash with the input string and returns the result as a hexadecimal string.

This solution assumes that the input string is valid UTF-8. If the input string can contain characters outside the UTF-8 range, you should use `hash.digest('base64')` instead of `hash.digest('hex')`.

Also, make sure to handle exceptions in a production-level code, in case the input is not a string.

Please note that MD5 has been cracked and it's not recommended to use it for any security-related tasks. If you need a secure hash function, you should use a stronger one like SHA-256 or SHA-3.

































































































