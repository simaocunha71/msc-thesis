  var result = [];
  var words = s.split(' ');

  for (const word of words) {
    var count = 0;
    for (const c of word) {
      if (c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u') {
        count += 1;
      }
    }
    if (count == n) {
      result.push(word);
    }
  }

  return result;
}