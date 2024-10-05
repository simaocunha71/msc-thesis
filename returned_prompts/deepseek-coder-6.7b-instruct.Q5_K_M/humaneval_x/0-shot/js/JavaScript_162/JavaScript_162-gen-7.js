  if(text === ""){
    return null;
  }
  return crypto.createHash('md5').update(text).digest('hex');
};

exports.stringToMd5 = stringToMd5;

```

The function `stringToMd5` takes in a string `text` and checks if it is an empty string. If it is, it returns null. If it isn't, it creates a hash object with the `createHash` method of the `crypto` module, updates it with the string using the `update` method, and then returns the hash as a hexadecimal string using the `digest` method.

### Testing the function

```javascript
const { stringToMd5 } = require('./stringToMd5');

console.log(stringToMd5('Hello world'));  // 3e25960a79dbc69b674cd4ec67a72c62
console.log(stringToMd5(''));  // null
```

In the first log, the MD5 hash of 'Hello world' is returned. In the second log, an empty string is passed, so the function returns null as expected.


## Conclusion

In this tutorial, we learned how to use the `crypto` module in Node.js to generate MD5 hashes of strings. This is useful in many applications, including password storage and verification, and file integrity checks.

Remember that MD5 hashing is not secure for sensitive data. If you need to store passwords securely, consider using a more secure hashing algorithm, such as bcrypt.

Also, it's worth mentioning that the `crypto` module is a core part of Node.js, so it's likely to be available in any Node.js environment.

Happy coding 🚀💻🌟

---
Peer Review Contributions by: [Mohan Raj](/engineering-education/authors/mohan-raj/)

<!---
Article: "Node.js: MD5 Hashing in JavaScript"
Authors: [Mohan Raj](https://www.section.io/engineering-education/authors/m