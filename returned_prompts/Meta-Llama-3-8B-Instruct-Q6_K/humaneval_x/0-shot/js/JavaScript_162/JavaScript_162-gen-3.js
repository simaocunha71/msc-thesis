```
const crypto = require('crypto');

const stringToMd5 = (text) => {
  if (!text) return null;
  const hash = crypto.createHash('md5');
  hash.update(text);
  return hash.digest('hex');
};

console.log(stringToMd5('Hello world')); // 3e25960a79dbc69b674cd4ec67a72c62
```



Explanation:

1. We import the `crypto` module, which provides a variety of cryptographic primitives, including the MD5 algorithm.
2. We define the `stringToMd5` function, which takes a string `text` as input.
3. We check if the input `text` is an empty string. If it is, we return `null`.
4. We create a new MD5 hash object using `crypto.createHash('md5')`.
5. We update the hash object with the input `text` using the `update` method.
6. We get the MD5 hash as a hexadecimal string using the `digest` method with the 'hex' option.
7. We return the resulting MD5 hash as a string.