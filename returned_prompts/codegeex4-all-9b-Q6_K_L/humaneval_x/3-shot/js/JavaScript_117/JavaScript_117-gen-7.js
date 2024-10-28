  var words = s.split(' ');
  var result = [];

  for (const word of words) {
    var count = 0;
    for (const c of word) {
      if (c.toLowerCase() != 'a' && c.toLowerCase() != 'e' && c.toLowerCase() != 'i' && c.toLowerCase() != 'o' && c.toLowerCase() != 'u') {
        count += 1;
      }
    }
    if (count == n) {
      result.push(word);
    }
  }

  return result;
}



