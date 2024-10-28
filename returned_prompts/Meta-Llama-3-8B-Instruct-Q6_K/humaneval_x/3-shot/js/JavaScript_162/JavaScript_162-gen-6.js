  if (!text) return null;
  const hash = crypto.createHash('md5');
  hash.update(text);
  return hash.digest('hex');
} // This function requires the 'crypto' module, which is built-in in Node.js but not in browser environments. For browser environments, you might need to use a library like crypto-js.



