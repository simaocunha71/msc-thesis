```
const crypto = require('crypto');

const stringToMd5 = (text) => {
  if (!text) return null;
  const hash = crypto.createHash('md5');
  hash.update(text);
  return hash.digest('hex');
};
```


Explanation:
The provided solution uses the 'crypto' module in Node.js to create a new MD5 hash object. It then updates the hash object with the given string 'text' using the 'update' method. Finally, it returns the hexadecimal representation of the hash using the 'digest' method. If the input string is empty, it returns null as per the problem statement.