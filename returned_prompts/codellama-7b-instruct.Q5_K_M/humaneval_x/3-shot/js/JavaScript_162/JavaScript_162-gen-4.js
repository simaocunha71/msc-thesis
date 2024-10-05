  if (text == '') {
    return null;
  } else {
    return crypto.createHash('md5').update(text).digest('hex');
  }
}



