```
const crypto = require('crypto');

const stringToMd5 = (text) => {
  if (!text) {
    return null;
  }
  const hash = crypto.createHash('md5');
  hash.update(text);
  return hash.digest('hex');
};

module.exports = stringToMd5;
```

Explanation:
We're using the `crypto` module in Node.js to create an MD5 hash of the given string. If the string is empty, we return `null`. Otherwise, we create a new `crypto` hash object with the algorithm 'md5', update it with the given text, and then return the digest as a hexadecimal string. The `digest` method returns the hash value as a string, and we specify 'hex' as the encoding to get the hexadecimal representation of the hash.