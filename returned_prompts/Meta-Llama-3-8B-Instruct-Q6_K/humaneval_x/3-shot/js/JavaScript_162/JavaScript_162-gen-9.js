  if (text === '') {
    return null;
  }
  var hash = crypto.createHash('md5');
  hash.update(text);
  return hash.digest('hex');
} // This will only work in a Node.js environment, where the crypto module is available.