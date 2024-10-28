```javascript
const crypto = require('crypto');

const stringToMd5 = (text) => {
  if (!text) return null;
  const hash = crypto.createHash('md5');
  hash.update(text);
  return hash.digest('hex');
};
``` 