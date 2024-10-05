const crypto = require('crypto');

const stringToMd5 = (text) => {
  if (text === '') return null;
  const hash = crypto.createHash('md5');
  hash.update(text);
  return hash.digest('hex');
};

B:
const crypto = require('crypto');

const stringToMd5 = (text) => {
  if (text === '') return null;
  return crypto.createHash('md5').update(text).digest('hex');
};

C:
const crypto = require('crypto');

const stringToMd5 = (text) => {
  if (text === '') return null;
  const hash = crypto.createHash('md5');
  return hash.update(text).digest('hex');
};

D:
const crypto = require('crypto');

const stringToMd5 = (text) => {
  if (text === '') return null;
  return crypto.createHash('md5').update(text).digest('hex').toString();
};