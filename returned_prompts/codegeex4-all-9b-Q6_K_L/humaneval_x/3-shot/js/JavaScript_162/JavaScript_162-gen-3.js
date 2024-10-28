  if (text == '') {
    return null;
  }
  var hash = CryptoJS.MD5(text);
  return hash.toString();
}



