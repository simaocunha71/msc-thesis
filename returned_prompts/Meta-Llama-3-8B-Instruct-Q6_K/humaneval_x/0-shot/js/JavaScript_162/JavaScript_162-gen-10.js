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

// Test
console.log(stringToMd5('Hello world')); // Output: 3e25960a79dbc69b674cd4ec67a72c62
```


The code above defines a function `stringToMd5` that takes a string `text` as input and returns its MD5 hash equivalent string. 

The function first checks if the input `text` is empty. If it is, the function returns `null`. 

If the input `text` is not empty, the function creates a new MD5 hash object using `crypto.createHash('md5')`. 

It then updates the hash object with the input `text` using the `update` method. 

Finally, it returns the hexadecimal representation of the hash object using the `digest` method with 'hex' as the argument. 

The test at the end of the code shows that the function correctly calculates the MD5 hash of the string 'Hello world'. 

Note that the `crypto` module is built into Node.js, so you don't need to install any additional dependencies to use it. 

However, if you are running this code in a browser, you will need to use a library like `js-md5` to calculate the MD5 hash. 

Here's how you can modify the code to use `js-md5`:

```
const md5 = require('js-md5');

const stringToMd5 = (text) => {
  if (!text) {
    return null;
  }
  return md5(text);
};

// Test
console.log(stringToMd5('Hello world')); // Output: 3e25960a79dbc69b674cd4ec67a72c62
```


In this modified code, we import the `js-md5` library and use its `md5` function to calculate the MD5 hash of the input `text`. 

The rest of the code remains the same. 

This modified code can be run in a browser, whereas the original code can only be run in Node.js. 