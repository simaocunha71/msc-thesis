  if (text === '') {
    return null;
  }
  const crypto = require('crypto');
  return crypto.createHash('md5').update(text).digest('hex');
}
// Note: The above code requires the crypto module which is built-in in Node.js. If you are using browser, you might need to use a library like crypto-js. Here is the equivalent code using crypto-js:
// const cryptoJS = require('crypto-js');
// return cryptoJS.MD5(text).toString();