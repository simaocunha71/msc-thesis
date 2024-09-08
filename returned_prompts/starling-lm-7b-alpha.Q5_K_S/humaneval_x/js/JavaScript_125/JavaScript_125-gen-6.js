  var words = txt.split(' ');
  if (words.length == 0) {
    var chars = txt.split(',');
    if (chars.length == 0) {
      var count = 0;
      for (var c of txt) {
        if (c == c.toLowerCase() && (c - 'a') % 2 == 1) {
          count += 1;
        }
      }
      return count;
    } else {
      return chars;
    }
  } else {
    return words;
  }
}



