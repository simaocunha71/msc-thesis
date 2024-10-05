  var words = txt.split(/\s+/);

  if (words.length > 0) {
    return words;
  } else {
    return txt.split(',').length;
  }
}



