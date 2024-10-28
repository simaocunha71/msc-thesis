The function should return the MD5 hash equivalent string of the given text. If the text is an empty string, it should return null.

Here is the solution in JavaScript:
```
const crypto = require('crypto');

const stringToMd5 = (text) => {
  if (!text) return null;
  const hash = crypto.createHash('md5');
  hash.update(text);
  return hash.digest('hex');
};

console.log(stringToMd5('Hello world')); // Output: 3e25960a79dbc69b674cd4ec67a72c62
```



Explanation:
The `crypto` module in Node.js provides a way to create and manipulate cryptographic primitives, such as MD5.

1. We require the `crypto` module at the top of the file.
2. We define the `stringToMd5` function, which takes a string as an argument.
3. We check if the input string is empty. If it is, we return `null`.
4. We create an MD5 hash object using `crypto.createHash('md5')`.
5. We update the hash object with the input string using `hash.update(text)`.
6. We get the MD5 hash digest as a hexadecimal string using `hash.digest('hex')`.
7. We return the MD5 hash digest as a string.

Note: The MD5 hash is a 128-bit hash function, and its output is a 32-character hexadecimal string. This is why the output of the `stringToMd5` function is a 32-character string.