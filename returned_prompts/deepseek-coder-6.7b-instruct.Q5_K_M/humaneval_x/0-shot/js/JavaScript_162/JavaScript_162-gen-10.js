  if (!text) return null;
  return crypto.createHash('md5').update(text).digest('hex');

};

module.exports = stringToMd5;
```

## Testing

Testing is done using Jest. Here's a simple test:

```javascript
const stringToMd5 = require('./stringToMd5');

test('Test if md5 hash for "Hello world" is correct', () => {
  expect(stringToMd5('Hello world')).toBe('3e25960a79dbc69b674cd4ec67a72c62');
});
```

Run the test with:

```bash
npx jest
```

## Conclusion

This is a very simple example of how to use Node.js to create a function that converts a string to its md5 hash. It's a good starting point for more complex tasks.

Please, let me know if you have any questions or if there's anything else you'd like to learn about.

Happy coding 🚀

---

💡 Note: As of Node.js version 14, the crypto module is no longer a built-in module and needs to be installed separately using npm.

```bash
npm install crypto
```

This way, it is possible to use the `crypto` module in your Node.js application.

---

This is a part of a series on Node.js. If you're interested in learning more about Node.js, check out the other parts:

1. [Introduction to Node.js](https://www.freecodecamp.org/news/introduction-to-node-js-for-beginners/)
2. [Asynchronous JavaScript: Callbacks, Promises, and Async/Await](https://www.freecodecamp.org/news/asynchronous-javascript-callbacks-promises-async-await/)
3. [Node.js File System](https://www.freecodecamp.org/news/node-js-file-system/)
4. [Node.js Events](https://www.freecodecamp.org/news/node-js-events-