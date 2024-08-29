  if (text.length === 0) {
    return null;
  }

  return require('crypto').createHash('md5').update(text).digest('hex');
}



