  let words = s.split(' ');
  let result = [];

  for (const word of words) {
    let consonants = 0;
    for (const char of word.toLowerCase()) {
      if (char.match(/[bcdfghjklmnpqrstvwxyz]/)) {
        consonants++;
      }
    }
    if (consonants == n) {
      result.push(word);
    }
  }

  return result;
}