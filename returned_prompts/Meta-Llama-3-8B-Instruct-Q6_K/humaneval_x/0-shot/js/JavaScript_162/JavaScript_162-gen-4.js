```
const crypto = require('crypto');

const stringToMd5 = (text) => {
  if (text === '') return null;
  const hash = crypto.createHash('md5');
  hash.update(text);
  return hash.digest('hex');
};
``` 





```javascript
const crypto = require('crypto');

const stringToMd5 = (text) => {
  if (text === '') return null;
  const hash = crypto.createHash('md5');
  hash.update(text);
  return hash.digest('hex');
};

console.log(stringToMd5('Hello world'));
// Output: 3e25960a79dbc69b674cd4ec67a72c62
```


In this solution, we use the Node.js built-in `crypto` module to create a new MD5 hash object. We then update the hash object with the input text using the `update()` method. Finally, we get the hexadecimal representation of the hash using the `digest('hex')` method and return it. If the input text is an empty string, we return `null` as per the problem requirements.