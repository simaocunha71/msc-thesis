  if (text === '') {
    return null;
  }

  return crypto.createHash('md5').update(text).digest('hex');
}



