const crypto = require('crypto');

const md5 = (text) => {
  return crypto.createHash('md5').update(text).digest('hex');
};

const stringToMd5 = (text) => {
  if (text === '') {
    return null;
  }
  return md5(text);
};

module.exports = { stringToMd5 };
