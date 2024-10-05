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
```



Explanation:
We're using the `crypto` module in Node.js to create a hash object with the MD5 algorithm. We then update the hash object with the input string and finally get the digest of the hash object in hexadecimal format.

If the input string is empty, we return null as per the problem statement. Otherwise, we return the MD5 hash equivalent string.