const crypto = require('crypto');

module.exports = (text) => {
  if (text === '') {
    return null;
  }
  return crypto.createHash('md5').update(text).digest('hex');
};
