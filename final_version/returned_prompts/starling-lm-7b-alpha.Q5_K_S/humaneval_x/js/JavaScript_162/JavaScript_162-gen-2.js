  if (text.length == 0) {
    return null;
  }

  let hash = crypto.createHash('md5');
  hash.update(text);
  return hash.digest('hex');
}



