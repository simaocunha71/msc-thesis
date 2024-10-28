  if (text === "") {
    return null;
  } else {
    var hash = crypto.createHash('md5');
    hash.update(text);
    return hash.digest('hex');
  }
}  // Note: This code requires the crypto module, which is not available in all environments (e.g., browser-side JavaScript). If you need a browser-compatible solution, consider using a library like crypto-js.



