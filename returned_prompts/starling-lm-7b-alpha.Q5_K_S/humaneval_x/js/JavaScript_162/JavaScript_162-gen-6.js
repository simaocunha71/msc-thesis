  if (text == "") return null;

  let hash = require('crypto').createHash('md5');
  hash.update(text);
  return hash.digest('hex');
}



