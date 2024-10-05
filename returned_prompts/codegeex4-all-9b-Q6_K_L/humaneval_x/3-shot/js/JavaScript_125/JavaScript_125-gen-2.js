  var words = txt.split(' ');
  if (words.length == 1) {
    words = txt.split(',');
    if (words.length == 1) {
      var count = 0;
      for (const c of words[0]) {
        if (c >= 'a' && c <= 'z') {
          if ((c.charCodeAt(0) - 'a'.charCodeAt(0)) % 2 == 1) {
            count += 1;
          }
        }
      }
      return count;
    }
  }
  return words;
}