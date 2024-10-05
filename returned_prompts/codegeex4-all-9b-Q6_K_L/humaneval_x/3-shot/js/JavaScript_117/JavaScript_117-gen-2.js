  var words = s.split(' ');
  var result = [];

  for (const word of words) {
    var consonants = 0;
    for (const c of word) {
      if (c.match(/[bcdfghjklmnpqrstvwxyz]/i)) {
        consonants += 1;
      }
    }
    if (consonants == n) {
      result.push(word);
    }
  }

  return result;
}