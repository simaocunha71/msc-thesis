  if (text === '') {
    return null;
  } else {
    const crypto = require('crypto');
    const hash = crypto.createHash('md5');
    hash.update(text);
    return hash.digest('hex');
  }
}
