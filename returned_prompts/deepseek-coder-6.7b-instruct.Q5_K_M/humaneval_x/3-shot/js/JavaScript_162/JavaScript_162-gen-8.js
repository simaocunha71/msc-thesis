  if  (text.length  != ’’)  {
    return crypto.createHash('md5').update(text).digest('hex');
  }
  else  {
    return null;
  }
}



