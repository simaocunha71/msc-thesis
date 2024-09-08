  if (text === '') {
    return null;
  } else {
    return require('crypto').createHash('md5').update(text).digest('hex');
  }
}



