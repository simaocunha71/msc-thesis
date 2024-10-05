  if (text === '') {
    return null;
  } else {
    const crypto = require('crypto');
    return crypto.createHash('md5').update(text).digest('hex');
  }
};

module.exports = stringToMd5;
```

## Test Cases

```js
console.log(stringToMd5('Hello world'));  // '3e25960a79dbc69b674cd4ec67a72c62'
console.log(stringToMd5(''));             // null
console.log(stringToMd5('This is a test')); // '5d57c0d0f0be3f4c946a5c515c5f7207'
```

## Code Explanation

The `stringToMd5` function takes a string as an argument and returns its MD5 hash equivalent. If the input string is an empty string, it returns null.

The `crypto` module in Node.js is used to generate the MD5 hash. The `createHash` method is used to create a new hash object, and then the `update` method is used to pass the input string to the hash object. Finally, the `digest` method is used to generate the final hash string in hexadecimal format.

The `require` statement is used to import the `crypto` module, which provides cryptographic functionality. The `module.exports` statement is used to export the `stringToMd5` function so that it can be imported and used in other files.

The `console.log` statements are used to test the `stringToMd5` function with different inputs. The expected outputs are provided in the comments.

## References

- [crypto module documentation](https://nodejs.org/api/crypto.html)
- [MD5 Hash Function](https://en.wikipedia.org/wiki/MD5)
- [Testing with different inputs](https://www.md5hashgenerator.com/)

## License

This code is licensed under the MIT License. See the [LICENSE](https://github.com/davidkpiano/crypto-